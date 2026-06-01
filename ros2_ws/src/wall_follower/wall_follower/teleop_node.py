import queue
import sys
import threading

import rclpy
from geometry_msgs.msg import Twist
from rclpy.node import Node


class TeleopNode(Node):

    def __init__(self):
        super().__init__('teleop')

        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        self.commands = queue.Queue()
        self.create_timer(0.05, self.publish_pending_commands)

        self.get_logger().info(
            'Teleop ready: W forward, A left, D right, S stop, Q quit'
        )

        threading.Thread(
            target=self.read_commands,
            daemon=True
        ).start()

    def read_commands(self):
        while rclpy.ok():
            command = sys.stdin.read(1).lower()
            if not command:
                return

            self.commands.put(command)

    def publish_pending_commands(self):
        while not self.commands.empty():
            command = self.commands.get()

            if command == 'q':
                rclpy.shutdown()
                return

            msg = Twist()

            if command == 'w':
                msg.linear.x = 0.25
            elif command == 'a':
                msg.linear.x = 0.15
                msg.angular.z = 1.0
            elif command == 'd':
                msg.linear.x = 0.15
                msg.angular.z = -1.0
            elif command != 's':
                continue

            self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = TeleopNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()

        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
