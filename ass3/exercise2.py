'''
Descripttion: 111
version: 
Author: xxh
Date: 2021-11-13
'''
from z3 import *


class Todo(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

    def __repr__(self):
        return self.__str__()

# In Exercise 1, we've learned how to use z3 to obtain the solutions that
# satisfy a given proposition.
# We must point out that the validity of Z3 is capable to prove
# lies into the boundary of classical logic:


# Besides "And", "Or" and "Not" constructors (functions), there
# is some also the "Implies" and "Xor" constructors, which
# can be used to construct propositions. For instance:
# P->P
P = Bool('P')
Q = Bool('Q')
R = Bool('R')
F = Implies(P, P)

# Now think of what we do in previous exercise about using Coq. If we
# use Coq to prove P -> P, we will use tactic apply P.
# Then P -> P is proved.
# Now we use a different way, to prove it via z3.
# This time we don't use z3 to obtain the solution for P->P, we just
# try to find solution for its opposite, aka. Not(F):
solve(Not(F))

# Z3 output the following:
# "no solution"
# which indicates that the proposition F is valid.

# Then the following
# double negation law:
# ~~P -> P
F = Implies(Not(Not(P)), P)
solve(Not(F))

# TODO: Exercise 2-1
# Now it's your turn, try to prove the exclusive middle law if also valid:
# P \/ ~P
print('2-1 Started')
F = Or(P,Not(P))
solve(Not(F))
print('2-1 Finished')
# raise Todo("Exercise 2-1: try to prove the exclusive middle law if also valid")


# TODO: Exercise 2-2
# Prove the validity of the Pierce's law:
# ((P->Q)->P)->P)
print('2-2 Started')
F = Implies(Implies(Implies(P,Q),P),P)
solve(Not(F))
print('2-2 Finished')
# raise Todo("Exercise 2-2: try to prove the validity of the Pierce's law")


# Note that the Pierce's law only holds in classical logic, but
# not in constructive logic, for
# interested readers, please refer to the background reading:
# https://en.wikipedia.org/wiki/Peirce%27s_law


# TODO: Exercise 2-3
# In previous exercise about use Coq, we ever give you an challenge
# (P -> Q) -> (~Q -> ~P).
# Now try to prove it's valid via z3
print('2-3 Started')
F = Implies(Implies(P,Q),Implies(Not(Q),Not(P)))
solve(Not(F))
print('2-3 Finished')
# raise Todo("Exercise 2-3: try to prove the validity of the proposition: (P -> Q) -> (~Q -> ~P)")


# TODO: Exercise 2-4
# Once more, try to prove that validity of :
# (P -> Q /\ R) -> ((P -> Q) /\ (P -> R))
# Be carefully when you process the priority of operations cause
# there is no intros. which can process it automatically for you
# to use.
print('2-4 Started')
F = Implies(And(Implies(P,Q),R),And(Implies(P,Q),Implies(P,R)))
solve(Not(F))
print('2-4 Finished')

# raise Todo("Exercise 2-4: try to prove the validity of the proposition: (P -> Q /\\ R) -> ((P -> Q) /\\ (P -> R))")


# Well done, you complete Exercise 2, remember to save your code for handing in.
