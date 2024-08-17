# For getting input from the user in the terminal
import sys

# Ros client Library for python
import rclpy
from rclpy.node import Node

#Message type for  publishing cmd_vel
from geometry_msgs.msg import Twist

class Angular_velocity(Node):

    def __init__(self):
        #Node_name : "angular_velocity_node"
        super().__init__('angular_velocity_node')

        #publisher_topic : /turtle1/cmd_vel
        self.vel_pub = self.create_publisher (Twist , '/turtle1/cmd_vel',10)
        self.timer = self.create_timer(1,self.timer_callback)

    #timer_callback will be called for 1 second.
    def timer_callback(self):
        #Msg_type: geometry_msgs/msg/Twist

        # This expresses velocity in free space broken into its linear and angular parts.
        # Vector3  linear
        # 	float64 x
        # 	float64 y
        # 	float64 z
        # Vector3  angular
        # 	float64 x
        # 	float64 y
        # 	float64 z

        msg = Twist()

        # ang_velocity = linear_velocity / radius

        #Getting the linear velocity as a input from the user
        linear_velocity = float(sys.argv[1])
        radius = float(sys.argv[2])
        
        msg.linear.x = linear_velocity
        msg.linear.y = 0.0
        #w = v/r
        msg.angular.z = linear_velocity/radius
        self.vel_pub.publish(msg)

def main(args = None):
    rclpy.init (args=args)
    node = Angular_velocity()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()




