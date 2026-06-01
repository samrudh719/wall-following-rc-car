import math

import rclpy
from geometry_msgs.msg import Twist
from rclpy.node import Node
from sensor_msgs.msg import Range

from wall_follower.pid_controller import PIDController
from wall_follower.utils import clamp


class WallFollower(Node):

    def __init__(self):
        super().__init__('wall_follower')

        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        self.subscription = self.create_subscription(
            Range,
            'wall_distance',
            self.distance_callback,
            10
        )

        self.pid = PIDController(kp=2.5, ki=0.02, kd=0.5)
        self.target_distance = 0.30
        self.last_time = self.get_clock().now()

    def distance_callback(self, msg):
        if not math.isfinite(msg.range):
            self.get_logger().warning('Ignoring invalid distance reading')
            return

        current_time = self.get_clock().now()
        dt = (current_time - self.last_time).nanoseconds / 1e9
        self.last_time = current_time

        correction = self.pid.compute(
            self.target_distance,
            msg.range,
            dt
        )

        cmd = Twist()
        cmd.linear.x = 0.25
        cmd.angular.z = clamp(correction, -2.0, 2.0)
        self.publisher.publish(cmd)

        self.get_logger().info(
            f'Distance: {msg.range:.2f} m '
            f'Correction: {cmd.angular.z:.2f}'
        )


def main(args=None):
    rclpy.init(args=args)
    node = WallFollower()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
