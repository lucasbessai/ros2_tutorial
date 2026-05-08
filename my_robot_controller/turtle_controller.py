#!/usr/bin/env python3
import rclpy
# import numpy as np
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

# bounds of turtlesim domain
x_min = 0.0
y_min = 0.0
x_mid = 5.544445
y_mid = 5.544445
x_max = x_mid * 2
y_max = y_mid * 2
bound_max = 0.9*x_max
bound_min = x_min + (x_max - bound_max)

pi = 3.14159

class TurtleControllerNode(Node):

    def __init__(self):
        super().__init__("turtle_controller")
        self.pose_subscriber_ = self.create_subscription(
            Pose, "/turtle1/pose", self.control_callback_short, 10
        )
        self.cmd_vel_publisher_ = self.create_publisher(
            Twist, "/turtle1/cmd_vel", 10
        )
        self.get_logger().info(
            "edge avoidance turtle controller has started!"
        )

    def control_callback(self, pose: Pose):
        cmd = Twist()
        # pos = [pose.x, pose.y]
        if pose.x > bound_max or pose.x < bound_min or pose.y > bound_max or pose.y < bound_min:
            cmd.linear.x = 9.0
            cmd.angular.z = 30.0
        else:
            cmd.linear.x = 10.0
            cmd.angular.z = 0.0
        self.cmd_vel_publisher_.publish(cmd)

    def control_callback_short(self, pose: Pose):
        cmd = Twist()
        # pos = [pose.x, pose.y]
        if pose.x > bound_max:
            cmd.linear.x = 9.0
            if pose.theta >= 0.0:
                cmd.angular.z = 30.0
            else:
                cmd.angular.z = -30.0
        elif pose.x < bound_min:            
            cmd.linear.x = 9.0
            if pose.theta <= 0.0:
                cmd.angular.z = 30.0
            else:
                cmd.angular.z = -30.0
        elif pose.y > bound_max:
            cmd.linear.x = 9.0
            if abs(pose.theta) >= pi / 2:
                cmd.angular.z = 30.0
            else:
                cmd.angular.z = -30.0
        elif pose.y < bound_min:
            cmd.linear.x = 9.0
            if abs(pose.theta) <= pi / 2:
                cmd.angular.z = 30.0
            else:
                cmd.angular.z = -30.0
        else:
            cmd.linear.x = 10.0
            cmd.angular.z = 0.0
        self.cmd_vel_publisher_.publish(cmd)

def main(args=None): 
    rclpy.init(args=args)
    node = TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()