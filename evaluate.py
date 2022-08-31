from const import SpecialForm
from parser import Cons


def evaluate(structure: list):
    operator = structure[0]
    operands = structure[1:]
    if operator in (SpecialForm.AR_ADD, SpecialForm.AR_SUB):
        result = 0
    elif operator in (SpecialForm.AR_MUL, SpecialForm.AR_DIV):
        result = 1
    elif operator in (SpecialForm.CONS,):
        result = Cons()
    else:
        result = 0
    for item in operands:
        if type(item) == list and operator is SpecialForm.AR_ADD:
            result += evaluate(item)
        elif type(item) == list and operator is SpecialForm.AR_SUB:
            result -= evaluate(item)
        elif operator is SpecialForm.AR_ADD:
            result += item
        elif operator is SpecialForm.AR_SUB:
            result -= item
        if type(item) == list and operator is SpecialForm.AR_MUL:
            result *= evaluate(item)
        elif type(item) == list and operator is SpecialForm.AR_DIV:
            result /= evaluate(item)
        elif operator is SpecialForm.AR_MUL:
            result *= item
        elif operator is SpecialForm.AR_DIV:
            result /= item
        elif type(item) == list and operator is SpecialForm.CONS:
            result.append(evaluate(item))
        elif operator is SpecialForm.CONS:
            result.append(item)

    return result
