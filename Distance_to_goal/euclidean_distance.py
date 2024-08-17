import math
import sys

x1,y1 = (int(sys.argv[1]),int(sys.argv[2]))
x2,y2 = (int(sys.argv[3]),int(sys.argv[4]))

def euclidean_distance(x1, y1, x2, y2):
    euclidean_distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(f"Euclidean distance between {x1,y1} and {x2,y2} is {euclidean_distance: .3f}")
    return euclidean_distance

if __name__=='__main__':
    euclidean_distance(x1,y1,x2,y2)