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
### For Angular velocity
#### Requirement :
- Ubuntu 22.04 or newer
- Ros2 humble
- Turtlesim package (which will be installed default in ros2 installation)

Step 1: To run the turtlesim node

       ros2 run turtlesim turtlesim_node

Step 2: To run the python script in which the linear velocity and radius are inputs from the command line arguments.
  
        python3 angular_velocity.py <linear_velocity(speed)> <radius>

        Eg. python3 angular_velocity.py 1 0.5