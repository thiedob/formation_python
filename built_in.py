
"""print(locals()['__builtins__'])
>>>locals()['__builtins__']
#1_BaseEXCeption    The base class for all built-in exceptions
try:
    raise BaseException("this is a BaseException")
except BaseException as e:
    print(e)

#2_xception     The base class for all non-exit exceptions
try:
    raise Exception("This is a generix Exception")
except Exception as e:
    print(e)

#3_ArithmeticError  Base class for all errors related to arithmetic operations
try:
    raise ArithmeticError("Arithmetic Error Occured")
except ArithmeticError as e:
    print(e)

#4_ZeroDivisionError    Raised when a division or modulo operation is performed with zero as the divisor
try:
    10 / 0
except ZeroDivisionError as e:
    print(e)

#5_OverflowError    Raised when a numerical operation exceeds the maximum limit of a data type
import math
try:
    result = math.exp(1000)
except OverflowError as e:
    print(e)

#6_FloatingPointError       Raised when a floating-point operation fails

import sys
import math

sys.float_info.max = 1.79e+308  # Maximum float value

try:
      math.sqrt(-1.0)  # This doesn't raise a FloatingPointError by default
except FloatingPointError as e:
    print(e)

#7_AssertionError   Raised when an assert statement fails
try:
    assert 1 == 2, "Assertion Failed"
except AssertionError as e:
    print(e)
"""
#8_AttributeError
class MyClass:
    pass
obj = MyClass()

try:
    obj.some_attribute
except AttributeError as e:
    print(e)