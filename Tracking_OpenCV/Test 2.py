from vpython import *
from time import *

def walls(col1, wall_2_col, wall_3_col):
    box(pos=vector(0,0,-6),color=col1, length=12, width=0.2, height=10)
    box(pos=vector(-6,0,0),color=color.wall_2_col,length=0.2, width=12, height=10)
    box(pos=vector(6,0,0),color=color.wall_3_col, length=0.2, width=12, height=10)

#myBall = sphere(color=color.red, radius=1)
#myBox = box(color=color.white,length=12,width=2,height=0.2)
#myTube = cylinder(color=color.orange,length=6,width=2,height=2)
#myTube = cylinder(color=color.orange,length=6,radius=1)
floor = box(pos=vector(0,-5,0),color=color.white, length=12, width=12, height=0.2)
celing = box(pos=vector(0,5,0),color=color.white, length=12, width=12, height=0.2)
#wall_back = box(pos=vector(0,0,-6),color=color.purple, length=12, width=0.2, height=10)
#wall_right = box(pos=vector(-6,0,0),color=color.cyan,length=0.2, width=12, height=10)
#wall_left = box(pos=vector(6,0,0),color=color.magenta, length=0.2, width=12, height=10)
myCylinder = sphere(color=color.red, radius=0.5)

while True:
    box(pos=vector(0,0,-6),color=color.yellow, length=12, width=0.2, height=10)
    box(pos=vector(-6,0,0),color=color.cyan,length=0.2, width=12, height=10)
    box(pos=vector(6,0,0),color=color.purple, length=0.2, width=12, height=10)
    sleep(2)
    box(pos=vector(0,0,-6),color=color.purple, length=12, width=0.2, height=10)
    box(pos=vector(-6,0,0),color=color.yellow,length=0.2, width=12, height=10)
    box(pos=vector(6,0,0),color=color.cyan, length=0.2, width=12, height=10)
    sleep(2)
    walls(r)