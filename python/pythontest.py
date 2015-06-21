from numpy import *
from fractions import Fraction as f
set_printoptions(precision=3,suppress=True)

def printm(a):
    """Prints the array as strings 
    :a: numpy array
    :returns: prints the array
    """
    def p(x):
        return str(x)
    p = vectorize(p,otypes=[str])
    print p(a)
    
def tableau(a,W=7):
    """Returns a string for verbatim printing
    :a: numpy array
    :returns: a string
    """
    if len(a.shape) != 2:
        raise ValueError('verbatim displays two dimensions')
    rv = []
    rv+=[r'|'+'+'.join('{:-^{width}}'.format('',width=W) for i in range(a.shape[1]))+"+"]
    rv+=[r'|'+'|'.join(map(lambda i: '{0:>{width}}'.format("x"+str(i+1)+" ",width=W), range(a.shape[1]-2)) )+"|"+
         '{0:>{width}}'.format("-z ",width=W)+"|"
         '{0:>{width}}'.format("b ",width=W)+"|"]
    rv+=[r'|'+'+'.join('{:-^{width}}'.format('',width=W) for i in range(a.shape[1]))+"+"]
    for i in range(a.shape[0]-1):
        rv += [r'| '+' | '.join(['{0:>{width}}'.format(str(a[i,j]),width=W-2) for j in range(a.shape[1])])+" |"]
    rv+=[r'|'+'+'.join('{:-^{width}}'.format('',width=W) for i in range(a.shape[1]))+"+"]
    i = a.shape[0]-1
    rv += [r'| '+' | '.join(['{0:>{width}}'.format(str(a[i,j]),width=W-2) for j in range(a.shape[1])])+" |"]
    rv+=[r'|'+'+'.join('{:-^{width}}'.format('',width=W) for i in range(a.shape[1]))+"+"]
    print '\n'.join(rv)

#vector transpose
def vecT(v):
    return array([v]).T

A = array( [[1,1,0],[2,0,0],[2,1,1]])

b = array ([4,5,7])

Cn = array( [6,0,0] )

Cb = array( [3,2,0] )

An = array ( [[2,1,0],[3,0,1],[3,0,0]])

Abi = linalg.inv(A)

dot(Abi,b)

Cn - dot(dot(Cb,Abi),An)

a = array( [2,3,3] )

at = dot(Abi,a)

xb = dot(Abi,b) - at

a2 = array( [3,4,6] )

a2t = dot(Abi,a)


#print a2t

#print at

#2014 opgave 4.b
A = array( [[4,3],[2,1],[1,2],[1,1]] )
b = array( [[4,3,1,2]]).T 
c = array( [[5,4]]).T

print A
print b
print c

slack = array([[1,0],[0,1]])

dual = concatenate((A.T,slack),axis=1) 

print dual



