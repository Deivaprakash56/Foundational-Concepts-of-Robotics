## Goal

* A **goal** in robotics refers to a specific target position that a robot aims to reach within its operating environment. 

* This target is typically defined by coordinates in a 2D or 3D space, such as (x, y) or (x, y, z), and may also include orientation angles depending on the application requirements.

Defining a clear goal is essential for planning and executing movements, 
* As it allows the robot to calculate the **Necessary path** and actions needed to navigate from its current position to the **desired destination (Goal)** effectively and efficiently.

## Go to Goal

To move a robot towards a specific goal position, it's essential to calculate two key parameters:
- **Distance to the goal** and 
- **Angle to the goal**

### Distance to Goal
The distance between the robot's current position (x_robot, y_robot) and the goal position (x_goal, y_goal) can be calculated using the Euclidean distance formula:


     Distance = sqrt [(x2-x1) ^ 2 + (y2-y1 ) ^ 2]


### Angle to Goal
The angle (theta) to the goal is the angle between the robot's current orientation and the line connecting the robot to the goal position. It is calculated as follows:

        ATG = {atan2(y_goal - y_robot, x_goal - x_robot)}

### Further Reading
For a more detailed explanation of **distance to goal** and **angle to goal**, please refer to the corresponding sections in the [Distance to Goal](../Distance_to_Goal/README.md) and [Angle to Goal](../Angle_to_Goal/README.md) directories within this repository.

These concepts are fundamental to the "Go to Goal" behavior and form the basis for the control algorithms that will guide the robot towards its goal.
