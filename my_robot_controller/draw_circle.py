#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class DrawCircleNode(Node):

    def __init__(self):
        super().__init__("draw_circle")
        self.cmd_vel_pub_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.get_logger().info("draw circle node has started")
        self.create_timer(0.2, self.send_velocity_command, )

    def send_velocity_command(self):
        msg = Twist()
        msg.linear.x = 10.0
        msg.angular.z = 4.0
        self.cmd_vel_pub_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = DrawCircleNode()
    rclpy.spin(node)
    rclpy.shutdown()

# not technically required since ros2 run directly calls main from:
#    entry_points={
#         'console_scripts': [
#             "test_node = my_robot_controller.my_first_node:main",
#             "draw_circle = my_robot_controller.draw_circle:main"
#         ],
#     },
if __name__ == '__main__':
    main()

