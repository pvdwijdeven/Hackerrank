# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import random
#filename=open("H:\R\Hackerrank\MachineLearning\Medium\Snakes&Ladders\input.txt")
filename=sys.stdin
line = filename.readline()
ntests=int(line)
random.seed(50)
def getdice(dice):
    r=random.random()
    i=1
    x=-1
    y=0
    while (x<0):
        y=y+dice[i]
        if r<y:
            x=i
        i=i+1
  #  print x
    return x

for i in range(0,ntests):
    diceval=map(float, filename.readline().split(","))
    dicekeys=[1,2,3,4,5,6]
    dice=dict(zip(dicekeys,diceval))
    dice2=dict(zip([1,2,3,4,5,6],[0.0,0.0,0.0,0.0,0.0,0.0]))
    x,y=(int(x) for x in filename.readline().split(","))
    ladlist=filename.readline().split(" ")
    ladvals=[]
    ladkeys=[]
    for k in range(0,x):
        ladvals.append(map(int,ladlist[k].split(","))[0])
        ladkeys.append(map(int,ladlist[k].split(","))[1])
        ladders=dict(zip(ladvals,ladkeys))
    snakelist=filename.readline().split(" ")
    snakevals=[]
    snakekeys=[]
    for k in range(0,y):
        snakevals.append(map(int,snakelist[k].split(","))[0])
        snakekeys.append(map(int,snakelist[k].split(","))[1])
        snakes=dict(zip(snakevals,snakekeys))
    board=dict(zip(range(1,107),range(1,107)))
    board.update(snakes)
    board.update(ladders)
    #print(board)
    #play game 5000 times
    timesrun=5000
    total=0
    totalrun=0
    while totalrun<timesrun:
        n=0
        cur=1
        while(cur<100):
            x=getdice(dice)
            n=n+1
            newcur=board[cur+x]
            if (newcur<=100):
                cur=newcur
        if (n<= 1000):
            total=total+n
            totalrun=totalrun+1
    print(int(total/timesrun))