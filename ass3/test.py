'''
Descripttion: 111
version: 
Author: xxh
Date: 2021-11-13
'''
from z3 import *
P =Bool('P')
Q = Bool('Q')
F = Or(P,Q)
solve(F)
F = And(F, Not(And(P, Not(Q))))
solve(F)
F = And(F, Not(And(Not(P), Q)))
solve(F)
F = And(F, Not(And(P, Q)))
solve(F)