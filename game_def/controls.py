from map import *
from msvcrt import getch
# rb_loc=gamemap[rr][rc]
############ Check radar #############

def move():
    key=getch()
    gamemap[rr][rc]=0
    if key ==b"a" and rc in range(1,10):
                rc-=1
    if key==b"d" and rc in range(0,9):
                rc+=1
    if key==b"w" and rr in range(1,10):
                rr-=1
    if key==b"s" and rr in range(0,9):
                rr+=1
    gamemap[rr][rc]=2


