import sys
import math

x1,y1 = (float(sys.argv[1]),float(sys.argv[2]))
x2,y2 = (float(sys.argv[3]),float(sys.argv[4]))

def manhattan_distance(x1,y1,x2,y2):
    manhattan_distance = abs(x2-x1) + abs (y2-y1)
    print(f"Manhattan distance between {x1,y1} and {x2,y2} is {manhattan_distance:.3f}")
    return manhattan_distance

if __name__ == '__main__':
    manhattan_distance(x1,y1,x2,y2)