from enum import Enum


class SpecialForm(Enum):
    AR_ADD = 1
    AR_SUB = 2
    AR_MUL = 3
    AR_DIV = 4


HASH_MAP = {
    "+": SpecialForm.AR_ADD,
    "-": SpecialForm.AR_SUB,
    "*": SpecialForm.AR_MUL,
    "/": SpecialForm.AR_DIV,
}
