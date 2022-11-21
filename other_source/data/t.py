import math
from math import log2 as l
from math import pow as p
from fractions import Fraction as f
from sympy import *
import numpy as np
a=[1,2,2,3]
b=[2,2,2,3,4,4]
ans=0
j=0 
for i in a:
  ans+=2**(-i)

print(ans)
# print(f(1,3)*f(5,8)+f(7,24)*f(4,7)+f(3,8)*f(1,3)) 
# print(f(1,4)*f(1,3)+f(1,4)*f(1,2)+f(1,2)*f(1,6)) 



