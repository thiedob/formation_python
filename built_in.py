
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

#8_AttributeError   Raised when an attribute reference or assignment fails.
class MyClass:
    pass
obj = MyClass()

try:
    obj.some_attribute
except AttributeError as e:
    print(e)

#9_IndexError   Raised when a sequence subscript is out of range
mylist = [1, 2, 3]
try:
    element = mylist[5]
except IndexError as e:
    print(e)

#10_KeyError    Raised when a dictionary Key is not found 
d = {"key1":"value1"}
try:
    val = d["key2"]
except KeyError as e:
    print(e)

#11 MemoryError     Raised when an operation runs out of memory
try:
    li = [1] * (10**10)
except MemoryError as e:
    print(e)

#12NameError      Raised when a local or global name is not found
try:
    print(var)
except NameError as e:
    print(e)

#13_OSError       Raised when a system-related operation (like file I/O) fails
try:
    open("non_existent_file.txt")
except OSError as e:
    print(e)

#14_TypeError  Raised when an operation or function is applied to an object of inappropriate type
try:
    result = '2' + 2 
except TypeError as e:
    print(e)

#15_ValueError     Raised when a function receives an argument of the right type but inappropriate value
try:
    res = int("abc")
except ValueError as e:
    print(e)

#16_importError     Raised when an import statement has issues
try:
    import mod
except ImportError as e:
    print(e)

#17_ModuleNotFoundError     Raised when a module cannot be found
try:
    import module
except ModuleNotFoundError as e:
    print(e)
"""
#18_IOError  Raised when an I/O operation (like reading or writing to a file) fails.
try:
    open("non_existent_file.txt")
except IOError as e:
    print(e)