

# Distance between two points

## Overview

In robotics, computer vision, and machine learning, distance metrics are essential for tasks like navigation, clustering, and nearest neighbour search. 

Two of the most commonly used distance metrics are 
- **Euclidean Distance** and 
- **Manhattan Distance**.

## Euclidean Distance

### What is Euclidean Distance?

* Euclidean distance is the straight-line distance between two points in Euclidean space. 
* It's the most familiar concept of distance, often referred to as **"as-the-crow-flies"** distance.

*  In a 2D plane, it is the length of the line segment connecting two points.

### Mathematical Formula
### 2D (Flat Surface):
For two points  P(x1, y1)  and  Q(x2, y2)  in a 2D space, the Euclidean distance (d) between them is given by:

![image](https://github.com/user-attachments/assets/101ee087-5e8c-47d2-978e-49e291e183e4)

     Eucli_dis (D) = sqrt [ (x2-x1) ^ 2 + (y2-y1 ) ^ 2]

### 3D (In Space):
In a 3D space, for points ( P(x1, y1, z1) ) and ( Q(x2, y2, z2) ), the formula extends to:

![image](https://github.com/user-attachments/assets/abdc8c9a-052b-44eb-8787-50137ad313ee)

* So, the distance will be calculated as the square root of the sum of the squares of differences in both x and y coordinates. 

### Applications

- **Path Planning**: Used to calculate the shortest path between two points.
- **Computer Vision**: Measures similarity between pixel intensities.
- **Clustering**: Helps to group similar points in space.

**how to compute Euclidean distance in python** (additional Reference)
[https://apat.io/posts/how-to-calculate-euclidean-distance-in-python/]

## Manhattan Distance

### What is Manhattan Distance?

Manhattan distance, also known as Taxicab or L1 distance, is the distance between two points measured along the axes at right angles.
*  Imagine walking along the gridlines of a city, where you can only move horizontally or vertically; the distance you travel is the **Manhattan distance**.

### Mathematical Formula

![image](https://github.com/user-attachments/assets/a8995448-caa8-4eab-9ce4-34a1fb511ef2)

For two points \( P(x1, y1) \) and \( Q(x2, y2) \) in a 2D grid, the Manhattan distance \( d \) between them is:


    d = |x2 - x1| + |y2 - y1|

In a 3D grid, for points \( P(x1, y1, z1) \) and \( Q(x2, y2, z2) \), the formula extends to:


    d = |x2 - x1| + |y2 - y1| + |z2 - z1|


### Applications

- **Grid-based Pathfinding**: Useful in scenarios like navigating a city grid.
- **Robotics**: Helps in determining the shortest path on a grid map.


## Comparison

![image](https://github.com/user-attachments/assets/2718082e-cbc8-4bf7-8141-4589744d6a29)


- **Straight Line vs. Grid Path**: 
    * Euclidean distance gives the shortest straight-line distance, while Manhattan distance gives the path along grid lines.
- **Usage**:
    * Euclidean distance is used when diagonal movement is possible, while Manhattan distance is used in grid-based systems where only horizontal and vertical moves are allowed.

## Conclusion

Understanding the difference between Euclidean and Manhattan distances is crucial in selecting the right metric for your application. Whether you're working on robotics navigation, clustering data, or simply measuring similarity, choosing the correct distance measure can greatly affect your results.

---

For any questions or contributions to this topic, please create an issue or submit a pull request.
