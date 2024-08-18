# Concepts in Robotics

## Topics Covered in This Repo:

- **Angular Velocity**
- **Distance to Goal**  
    - Euclidean Distance  
    - Manhattan Distance
- **Angle to Goal**
- **Go-to-Goal Node**
- **Complex Numbers**
- **Quaternion Angles**
- **Euler Angles**
- **Conversion of Quaternions to Euler Angles**
- **Conversion of Euler Angles to Quaternions**
- **Differential Drive**
- **Sensor Fusion Algorithms**
- **Graph Theory**
- **Grid Maps**
- **Path Planning Algorithms**

### Contributing

If you have any suggestions for additional topics to include in this repository, please create an issue or fork this repository and submit a pull request (PR) with the added content.

Thanks in advance,  
**Deivaprakash K**   
*Junior Robotics Software Engineer*

# Repo Usage:
## For Angular velocity
#### Requirements :
- Ubuntu 22.04 or newer
- Ros2 humble
- Turtlesim package (which will be installed default in ros2 installation)

Step 1: To run the turtlesim node

       ros2 run turtlesim turtlesim_node

Step 2: To run the python script in which the linear velocity and radius are inputs from the command line arguments.
  
        python3 angular_velocity.py <linear_velocity(speed)> <radius>

        Eg. python3 angular_velocity.py 1 0.5

## For Distance to goal

#### Requirement :
- Python3

### For Euclidean distance

        python3 euclidean_distance.py <x1> <y1> <x2> <y2>

        Eg. python3 euclidean_distance.py 1 2 2 3
        # which means (1,2) as (x1,y1) and (2,3) as (x2,y2)

### For manhattan distance

        python3 manhattan_distance.py <x1> <y1> <x2> <y2>

        Eg. python3 manhattan_distance.py 1 2 2 3
        # which means (1,2) as (x1,y1) and (2,3) as (x2,y2)

## For Angle to Goal (ATG)

        python3 angle_to_goal.py <x_robot> <y_robot> <x_goal> <y_goal>

        Eg.python3 angle_to_goal.py 1 2 2 3
        # which means (1,2) as (x_robot,y_robot) and (2,3) as (x_goal,y_goal)

