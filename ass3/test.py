'''
Descripttion: 111
version: 
Author: xxh
Date: 2021-11-13
'''
from z3 import *
P =Bool('P')
Q = Bool('Q')


F = Implies(Not(Not(P)), True)
solve(Not(F))