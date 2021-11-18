'''
Descripttion: 111
version: 
Author: xxh
Date: 2021-11-13
'''
from z3 import *


dic = {"P1":True,"P2":False,"P4":True}
F = And(Or(Not(dic["P1"]),Not(dic["P2"])),Or(dic["P2"],dic["P4"]))
s = Solver()
s.add(Not(F))
print(s.check())