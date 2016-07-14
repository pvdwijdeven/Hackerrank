# Enter your code here. Read input from STDIN. Print output to STDOUT
n,d = map(int,raw_input().split())
ar=map(int,raw_input().split())

total=0
for j in xrange(n-1):
    foundi=False
    for i in xrange(j,-1,-1):
        if ar[i]==ar[j]-d:
            foundi=True
            break
        elif ar[i]<ar[j]-d:
            break
    if foundi:
        foundk=False
        for k in xrange(j,n):
            if ar[k]==ar[j]+d:
                foundk=True
                break
            elif ar[k]>ar[j]+d:
                break
    if foundi and foundk:
        total+=1
print total