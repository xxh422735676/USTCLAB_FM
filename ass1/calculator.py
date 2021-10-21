import unittest


class Todo(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

    def __repr__(self):
        return self.__str__()


class Exp:

    def __repr__(self):
        return self.__str__()


class ExpVar(Exp):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

# add  class
class ExpAdd(Exp):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.left} + {self.right}"

# minus class
class ExpMinus(Exp):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.left} - {self.right}"

# multi class
class ExpMulti(Exp):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.left} * {self.right}"

# div class
class ExpDiv(Exp):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.left} / {self.right}"

# parent class
class ExpPar(Exp):
    #raise Todo("Exercise 1: complete the destructure of AST and the __str__ magic method")
    def __init__(self,exp):
        self.exp = exp

    def __str__(self):
        #raise Todo("Exercise 1: complete the destructure of AST and the __str__ magic method")
        return f"({self.exp})"


def eval_value(exp: Exp):
    if isinstance(exp, ExpVar):
        return exp.value
    if isinstance(exp, ExpPar):
        return eval_value(exp.exp)
    if isinstance(exp, ExpMulti):
        return eval_value(exp.left) * eval_value(exp.right)
    if isinstance(exp, ExpDiv):
        return eval_value(exp.left) / eval_value(exp.right)
    if isinstance(exp, ExpAdd):
        return eval_value(exp.left) + eval_value(exp.right)
    if isinstance(exp, ExpMinus):
        return eval_value(exp.left) - eval_value(exp.right)
    #raise Todo("Exercise 2： complete the eval method, calculate the value of AST")


test_case_1 = ExpAdd(
    ExpMulti(ExpVar(3), ExpVar(4)),
    ExpDiv(ExpVar(10), ExpVar(2))
)

test_case_2 = ExpMinus(
    ExpMulti(
        ExpPar(ExpAdd(ExpVar(12), ExpVar(217))),
        ExpVar(3)
    ),
    ExpVar(621)
)


class TestTableau(unittest.TestCase):

    def test_print_1(self):
        self.assertEqual(str(test_case_1), "3 * 4 + 10 / 2")

    def test_print_2(self):
        self.assertEqual(str(test_case_2), "(12 + 217) * 3 - 621")

    def test_eval_1(self):
        self.assertEqual(eval_value(test_case_1), 17)

    def test_eval_2(self):
        self.assertEqual(eval_value(test_case_2), 66)


if __name__ == '__main__':
    unittest.main()
