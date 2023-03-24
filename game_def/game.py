from map import *
from ui import *
from msvcrt import getch
import time
############ Check Wall #############
def wall_righ(g): #g=gamemap
    if rc in range(0,9):
        if g[rr][rc+1]==1:
            return True
def wall_left(g):
    if rc in range(1,10):
        if g[rr][rc-1]==1:
            return True
def wall_up(g):
    if rr in range(1,10):
        if g[rr-1][rc]==1:
            return True
def wall_down(g):
    if rr in range(0,9):
        if g[rr+1][rc]==1:
            return True
############ Check radar #############
def mine_righ(g):
    if rc in range(0,8):
        if g[rr][rc+2]==3:
            return print("Attention ⏰Bomb⏰ 2 steps ☛")
    if rc in range(0,9):
          if g[rr][rc+1]==3:
            return print("Go AWAY!⏳Bomb⏳ next ☛")
def mine_left(g):
    if rc in range(2,10):
        if g[rr][rc-2]==3:
            return print("Attention ⏰Bomb⏰ 2 steps ☚")
    if rc in range(1,10):
          if g[rr][rc-1]==3:
            return print("Go AWAY!⏳Bomb⏳ next ☚")
def mine_up(g):
    if rr in range(2,10):
        if g[rr-2][rc]==3:
            return print("Attention ⏰Bomb⏰ 2 steps ☝")
    if rr in range(1,10):
        if g[rr-1][rc]==3:
            return print("Go AWAY!⏳Bomb⏳ next ☝")
def mine_down(g):
    if rr in range(0,8):
        if g[rr+2][rc]==3:
            return print("Attention ⏰Bomb⏰ 2 steps ☟")
    if rr in range(0,9):
        if g[rr+1][rc]==3:
            return print("Go AWAY!⏳Bomb⏳ next ☟")
def p_attention(g):
     if mine_down(g)!=None:
          print(mine_down(g))
     if mine_up(g)!=None:
          print(mine_up(g))
     if mine_left(g)!=None:
          print(mine_left(g))
     if mine_righ(g)!=None:
          print(mine_righ(g))
robo_hp=100
mine_hit=30
run_count=0
clear()
print("Move to the Gate to escape from the labinth.\nAttention, you must evade the mines!")
print("Try do do it in minimum Moves")
input("Are you ready?")
while True:
    clear()
    printmap(gamemap)
    print("Robot HP:",robo_hp,"%",end=" ")
    print("Moves:",run_count)
    p_hist()
    p_attention(gamemap)
    key=getch()
    gamemap[rr][rc]=0
    if key ==b"a" and rc in range(1,10)and wall_left(gamemap)!=True:
        rc-=1
    if key==b"d" and rc in range(0,9) and wall_righ(gamemap)!=True:
        rc+=1
    if key==b"w" and rr in range(1,10) and wall_up(gamemap)!=True:
        rr-=1
    if key==b"s" and rr in range(0,9) and wall_down(gamemap)!=True:
        rr+=1
    if key==b"x":
        print("You are loooooseer")
        break
    if gamemap[rr][rc]==3:
        gamemap[rr][rc]=0
        gamemap[rr][rc]=5
        robo_hp=robo_hp-mine_hit
        clear()
        printmap(gamemap)
        print(" "*5,"BOOOOOOM!")
        if robo_hp<=0:
            print("POTRACENO!!!")
            break
        time.sleep(4)
    if gamemap[rr][rc]==4:
        clear()
        print("Succes! You Win!\nYour result is:",run_count,"Moves","\nTry to upgrade it!")
        break
    gamemap[rr][rc]=2
    run_count+=1