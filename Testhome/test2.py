n=input()
arr=[]
results=[]
nextres=-1
for _ in xrange(n):
    command=raw_input().split()
    if command[0]=="+":
        value=int(command[1])
        arr.append(value)
        if value==nextres:
            maxk+=1
            print maxk
            results.append(maxk)
            nextres = arr[maxk]
        else:
            arrl = len(arr)
            maxk = 0
            for k in xrange(arrl-2,-1,-1):
                if arr[k-1]==value:
                    if arr[:k] == arr[arrl - k:arrl]:
                        maxk = k
                        break
            print maxk
            nextres=arr[maxk]
            results.append(maxk)
    else:
        arr.pop()
        results.pop()
        xx=len(results)
        if xx==0:
            print 0
            nextres=-1
        else:
            maxk= results[xx-1]
            print maxk
            nextres = arr[maxk]