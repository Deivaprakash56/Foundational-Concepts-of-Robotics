import math,sys

x1,y1 = (float(sys.argv[1]),float(sys.argv[2])) #(x_robot,y_robot)
x2,y2 = (float(sys.argv[3]),float(sys.argv[4])) #(x_goal,y_goal)

def Angle_to_goal(x1,y1,x2,y2):
    ATG = math.atan2(y2-y1,x2-x1)
    print(f"Angle to goal between {x1,y1} and {x2,y2} is {ATG:.3f}")
    return ATG

if __name__ =='__main__':
    Angle_to_goal(x1,y1,x2,y2)