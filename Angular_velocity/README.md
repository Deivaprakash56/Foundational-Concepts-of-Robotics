# Understanding Angular Velocity

## What is Angular Velocity?

Angular velocity is all about how fast something is spinning (Rotating) around a particular point or axis.

Example : 
 Imagine a wheel spinning on a bike. Angular velocity tells us how quickly (Magnitude) that wheel is rotating and in what direction(Direction).

 * Since angular velocity includes both the information about  Magnitude and Direction, it is a **Vector Quantity**



## The Basics

Angular velocity measures the rate at which an angle changes over time. [ delta(theta) / delta(time) ]

Simply put, it’s how quickly an object rotates.

### The Formula:

![image](https://github.com/user-attachments/assets/7d1ad76f-f7ac-4b1c-9cde-b4aaac0f93a2)

This formula means:

- **ω** is the angular velocity (how fast the object is rotating) (in radians per second, rad/s).
- **Δθ** is the change in angle (how much the object has rotated).
- **Δt** is the change in time (how long it took for the object to rotate).

## Connecting Angular Velocity to Linear Speed

Angular velocity isn’t just about rotation – it also relates to how fast something is moving in a straight line. If you know how fast something is spinning (angular velocity) and the distance from the center (radius), you can figure out how fast a point on the edge is moving (linear velocity):

![image](https://github.com/user-attachments/assets/acb415e9-9dd2-4e03-a5a2-521465a88c1e)

From the above picture we can get to know that, 
* Linear velocity (v) = Angular velocity (ω) * Radius (r) 

By rearranging ,

* **Angular velocity (ω) = Linear velocity (v) / Radius (r)**


This formula means:

- **ω** is the angular velocity (how fast the object is rotating)(in radians per second, rad/s).
- **v** is the linear velocity (in meters per second, m/s)
- **r** is the radius (in meters, m)

## Why It’s Important

Angular velocity is a key concept in many areas, 
 - Especially in robotics, where it’s used to control the rotation of wheels, joints, and other moving parts. For instance, when a robot turns, angular velocity helps determine how fast each wheel should spin to make the turn smooth and accurate.



## Angular Velocity in Different Situations

### 2D (Flat Surface):

On a flat surface, like a spinning disk, angular velocity is simple. It’s just a measure of how fast the disk is spinning, clockwise or counterclockwise.

### 3D (In Space):

In 3D, things get a bit more complex. Angular velocity becomes a vector, which means it has both a speed and a direction. For example, think of how Earth spins around its axis – that’s 3D angular velocity.




## Why You Should Care

If you’re into robotics, understanding angular velocity is crucial. It helps you control how robots move, whether they’re turning corners, rotating joints, or balancing on wheels. It’s also useful in designing systems where precise control of rotation is needed.


## Wrap-Up

Angular velocity might sound complicated, but it’s really just a way to describe how fast something is spinning. Whether you’re working on a robot or just curious about how things move, understanding angular velocity is a handy skill to have.

![image](https://github.com/user-attachments/assets/daa0314d-9a88-4ab8-b949-c79dc20f9781)

---

If you have questions or want to suggest changes, feel free to create an issue or submit a pull request!
