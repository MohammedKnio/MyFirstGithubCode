"""
AubNet: mak109
ID: 201804131
Name: Mohamad Knio
"""
import sys

p= int(sys.argv[1])
q= int(sys.argv[2])

def gcd(p,q):
    if(q==0):
        return p
    else:
        return gcd(q, p%q)



print(gcd(p,q))