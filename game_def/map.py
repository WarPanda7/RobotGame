rr=0
rc=0
gamemap=[
        [0,0,0,0,0,0,0,0,3,1],
        [1,1,1,1,1,3,3,0,0,1],
        [0,0,0,0,0,0,0,3,0,0],
        [1,0,3,1,0,0,0,0,0,1],
        [1,0,3,1,1,1,1,3,3,1],
        [0,0,0,0,0,1,0,0,0,1],
        [1,1,1,1,0,1,3,3,3,3],
        [0,0,0,0,0,1,0,0,0,4],
        [0,0,0,0,0,3,0,3,0,1],
        [0,0,0,0,0,0,0,3,0,1]]
gamemap[rr][rc]=2
def p(c):
    print(c+" ",end="")
def printmap(m):
    print("⏹ "*12)
    for ri in range(10):
        p("⏹")
        for ci in range(10):
            if m[ri][ci]==0:
                p(" ")
            if m[ri][ci]==1:
                p("⊠")
            if m[ri][ci]==3:
                p("֍")
            if m[ri][ci]==2:
                p("߷")
            if m[ri][ci]==4:
                p("ၑ")
            if m[ri][ci]==5:
                p("💥")
        print("⏹")
    print("⏹ "*12)
def p_hist():
    print("History:\n߷=ROBOT  ⊠ Wall\n֍=Mine  ၑ=Gate")
    print("Controls\na-left  d-right\nw-up    s-down")