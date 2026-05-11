#!/usr/bin/env python3
import rclpy
# import numpy as np
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from turtlesim.srv import SetPen
from functools import partial

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
        self.x_prev = 0.0
        self.call_set_pen_service(0, 0, 0, 0, 1)

    def control_callback(self, pose: Pose):
        cmd = Twist()
        # pos = [pose.x, pose.y]
        if pose.x > bound_max or pose.x < bound_min or pose.y > bound_max or pose.y < bound_min:
            cmd.linear.x = 2.0
            cmd.angular.z = 4.0
        else:
            cmd.linear.x = 10.0
            cmd.angular.z = 0.0
        self.cmd_vel_publisher_.publish(cmd)

        if pose.x > x_mid and self.x_prev <= x_mid:
            self.x_prev = pose.x
            self.call_set_pen_service(255, 0, 0, 3, 0)
            self.get_logger().info("Set colour to red")

        if pose.x < x_mid and self.x_prev > x_mid:
            self.x_prev = pose.x
            self.call_set_pen_service(0, 255, 0, 3, 0)
            self.get_logger().info("Set colour to green")

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

    def call_set_pen_service(self, r, g, b, width, off):
        client = self.create_client(SetPen, "/turtle1/set_pen")
        while not client.wait_for_service(1.0):
            self.get_logger().info("waiting for service ...")
        
        request = SetPen.Request()
        request.r = r
        request.g = g
        request.b = b
        request.width = width
        request.off = off

        future = client.call_async(request)
        future.add_done_callback(partial(self.set_pen_done_callback))
    
    def set_pen_done_callback(self, future):
        try:
            response = future.result()
        except Exception as e:
            self.get_logger().error("Service call failed: %r" % (e,))

def main(args=None): 
    rclpy.init(args=args)
    node = TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()