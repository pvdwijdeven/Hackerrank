import numpy as np
#print np.append([[1, 2, 3], [4, 5, 6]], [[7],[8]], axis=1)
a=[[1,2,3],[4,5,6]]
a=np.array(a)
print a
b=[[7],[8]]
b=np.array(b)
print b
print a.shape
print b.shape
print np.append(a,b,axis=1)
