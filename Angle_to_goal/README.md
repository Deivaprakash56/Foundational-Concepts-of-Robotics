# Angle to Goal

## Overview

The **Angle to Goal** is a fundamental concept in robotics, particularly in the context of path planning and navigation. 
* It refers to the angle between a robot's current orientation and the direction towards its goal.
* Accurately determining this angle is crucial for guiding the robot towards its destination efficiently.


## Mathematical Explanation

![image](https://github.com/user-attachments/assets/2cc731e0-4262-49a5-99f4-fef651f4ed95)

* Consider a robot at position  (x_robot, y_robot)  in a 2D plane and a goal at position (x_goal, y_goal) 

* Yaw_angle(β) is the angle between the robot's current orientation and the positive x-axis.

* Goal angle(α) is the angle between the goal orientation and the positive x axis.

#### To Find:
* The angle between the Robot's current orientation (β) and the goal orientation (α) which is called as the heading (δ) 
[As mentioned in the diagram]

> Note: By knowing robot's orientation (β) and goal orientation (α) we can easily find angle to goal (δ) as 
δ(heading) = α(goal_angle) + β(Yaw angle) (Refer Diagram for better understanding)



## Compute the Angle to the Goal

The Angle_To_Goal (ATG) from the robot to the goal can be calculated using the arctangent function (tan inverse function)

![image](https://github.com/user-attachments/assets/c4388c53-9d73-427c-a54a-fd98c21736e4)


    δ = {atan2(y, x)}
    y = y_goal - y_robot ; x = x_goal - x_robot
    δ = {atan2(y_goal - y_robot, x_goal - x_robot)}

### Example Calculation

Assume a robot is at position (2, 3), the goal is at (5, 7) we need to find the angle to goal.

**Angle to Goal calculation**:
  
        x_robot,y_robot = (2, 3)
        x_goal,y_goal = (5,7)
        x = x_goal - x_robot = 5 - 2 = 3
        y = y_goal - y_robot = 7 - 3 = 4
        δ = {atan2(y,x)} 
        δ = {atan2(4,3)} 

**δ (Angle to goal) = 0.927295 ~ 0.93rad or 53.28deg**

## Applications

- **Path Planning**: Helps in determining the necessary adjustments in a robot's orientation to move towards a goal.
- **Obstacle Avoidance**: Used in algorithms where the robot must steer around obstacles while heading towards a goal.
- **Control Systems**: Essential in proportional-integral-derivative (PID) controllers and other feedback systems for motion control.

## Conclusion

Understanding the Angle to Goal is fundamental in robotics for tasks that involve movement towards a target. The precise calculation of this angle enables robots to navigate effectively, avoiding obstacles, and reaching their destination with minimal error.
