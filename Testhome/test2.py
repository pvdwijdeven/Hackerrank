n = input()
children = []
for i in xrange(n):
    children.append(input())
candies = [0]
for i in xrange(1, n):
    if children[i] > children[i - 1]:
        candies.append(candies[i-1]+1)
    else:
        candies.append(candies[i-1]-1)
countup = 1-min(candies)
for i in xrange(n):
    candies[i]+=countup
#print candies
candies[n-1]=1
for i in xrange(n-2,-1,-1):
    if children[i-1]>children[i] and children[i+1]<children[i]:
        candies[i]=candies[i+1]+1


#print candies
print sum(candies)
