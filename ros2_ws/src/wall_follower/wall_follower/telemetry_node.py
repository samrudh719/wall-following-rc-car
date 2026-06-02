import re

import rclpy
import serial
from geometry_msgs.msg import Twist
from rclpy.node import Node
from sensor_msgs.msg import Range
from std_msgs.msg import Int64


TELEMETRY_PATTERN = re.compile(
    r'^DIST:(?P<distance>-?\d+(?:\.\d+)?),'
    r'LEFT:(?P<left>-?\d+),'
    r'RIGHT:(?P<right>-?\d+)$'
)
MAX_SERIAL_BUFFER_SIZE = 1024
MIN_RANGE_METERS = 0.02
MAX_RANGE_METERS = 4.0


class TelemetryNode(Node):

    def __init__(self):
        super().__init__('telemetry')

        self.declare_parameter('serial_port', '/dev/ttyUSB0')
        self.declare_parameter('baudrate', 115200)
        self.serial_connection = None
        self.serial_buffer = bytearray()
        self.last_command = 's'

        self.distance_publisher = self.create_publisher(
            Range, 'wall_distance', 10
        )
        self.left_ticks_publisher = self.create_publisher(
            Int64, 'left_encoder_ticks', 10
        )
        self.right_ticks_publisher = self.create_publisher(
            Int64, 'right_encoder_ticks', 10
        )
        self.command_subscription = self.create_subscription(
            Twist, 'cmd_vel', self.command_callback, 10
        )

        self.create_timer(1.0, self.connect_serial)
        self.create_timer(0.02, self.read_serial)
        self.create_timer(0.1, self.write_last_command)

    def connect_serial(self):
        if self.serial_connection is not None:
            return

        port = self.get_parameter('serial_port').value
        if not port:
            return

        baudrate = self.get_parameter('baudrate').value

        try:
            self.serial_connection = serial.Serial(
                port=port,
                baudrate=baudrate,
                timeout=0
            )
            self.get_logger().info(f'Connected to ESP32 on {port}')
        except serial.SerialException as error:
            self.get_logger().warning(
                f'Unable to open ESP32 serial port {port}: {error}'
            )

    def read_serial(self):
        if self.serial_connection is None:
            return

        try:
            available = self.serial_connection.in_waiting
            if not available:
                return

            self.serial_buffer.extend(self.serial_connection.read(available))

            if len(self.serial_buffer) > MAX_SERIAL_BUFFER_SIZE:
                self.get_logger().warning(
                    'Discarding oversized ESP32 serial buffer'
                )
                self.serial_buffer.clear()
                return

            while b'\n' in self.serial_buffer:
                line, _, remainder = self.serial_buffer.partition(b'\n')
                self.serial_buffer = bytearray(remainder)
                self.publish_telemetry(line.decode(errors='replace').strip())
        except serial.SerialException as error:
            self.get_logger().error(f'ESP32 serial read failed: {error}')
            self.close_serial()

    def publish_telemetry(self, line):
        match = TELEMETRY_PATTERN.match(line)
        if match is None:
            return

        distance_meters = float(match.group('distance')) / 100.0

        if MIN_RANGE_METERS <= distance_meters <= MAX_RANGE_METERS:
            distance = Range()
            distance.header.stamp = self.get_clock().now().to_msg()
            distance.header.frame_id = 'ultrasonic_sensor'
            distance.radiation_type = Range.ULTRASOUND
            distance.field_of_view = 0.26
            distance.min_range = MIN_RANGE_METERS
            distance.max_range = MAX_RANGE_METERS
            distance.range = distance_meters
            self.distance_publisher.publish(distance)
        else:
            self.get_logger().warning(
                f'Ignoring out-of-range distance: {distance_meters:.2f} m'
            )

        left_ticks = Int64()
        left_ticks.data = int(match.group('left'))
        self.left_ticks_publisher.publish(left_ticks)

        right_ticks = Int64()
        right_ticks.data = int(match.group('right'))
        self.right_ticks_publisher.publish(right_ticks)

    def command_callback(self, msg):
        if msg.linear.x <= 0.0:
            command = 's'
        elif msg.angular.z > 0.05:
            command = 'a'
        elif msg.angular.z < -0.05:
            command = 'd'
        else:
            command = 'w'

        self.last_command = command
        self.write_last_command()

    def write_last_command(self):
        if self.serial_connection is None:
            return

        try:
            self.serial_connection.write(self.last_command.encode('ascii'))
        except serial.SerialException as error:
            self.get_logger().error(f'ESP32 serial write failed: {error}')
            self.close_serial()

    def close_serial(self):
        if self.serial_connection is not None:
            try:
                self.serial_connection.write(b's')
            except serial.SerialException:
                pass

            try:
                self.serial_connection.close()
            except serial.SerialException:
                pass

            self.serial_connection = None
            self.serial_buffer.clear()
            self.last_command = 's'

    def destroy_node(self):
        self.close_serial()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = TelemetryNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
