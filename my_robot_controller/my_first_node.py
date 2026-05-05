#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):

    def __init__(self):
        super().__init__("first_node")
        self.counter_ = 0
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info(f"Hello world {self.counter_}")
        self.counter_ += 1
        

def main(args=None):
    # initialize ros2 communcations and features
    rclpy.init(args=args)

    # node exists in the main program
    # object oriented programing is used for nodes
    
    # create node
    node = MyNode()

    # keep node running until user ctrl+c
    rclpy.spin(node)


    # kill ros2 communications
    rclpy.shutdown

if __name__ == '__main__':
    main()

