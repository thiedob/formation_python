
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

#18_IOError  Raised when an I/O operation (like reading or writing to a file) fails.
try:
    open("non_existent_file.txt")
except IOError as e:
    print(e)

#19_FileNotFoundError    Raised when a file or directory is requested but cannot be found
try:
    open("non_existent_file.txt")
except FileNotFoundError as e:
    print(e)

#20_StopIteration     Raised when the next() function is called and there are no more items in an iterator.
my_iter = iter([1, 2, 3])
try:
    while True:
        print(next(my_iter))
except StopIteration as e:
    print("End of Iteration") 

#21_KeyboardInterrupt   Raised when the user presses Ctrl+C or interrupts the program’s execution.
try:
    while True:
        pass
except KeyboardInterrupt as e:
    print("Program interrupted by user")

#22_SystemExit      Raised when the sys.exit() function is called to exit the program
import sys
try:
    sys.exit()
except SystemExit as e:
    print("system exit called")

#23_NotImplementedError     Raised when an abstract method that needs to be implemented is called.
class BaseClass:
    def some_method(self):
        raise NotImplementedError("This method should be overridden")
    
try:
    obj = BaseClass()
    obj.some_method()
except NotImplementedError as e:
    print(e)

#24_RuntimeError        Raised when a general error occurs in the program
try:
    raise RuntimeError("A Runtime Error Occured")
except RuntimeError as e:
    print(e)

#25_RecursionError      Raised when the maximum recursion depth is exceeded
try:
    def recursive_function():
        recursive_function()
    
    recursive_function()
except RecursionError as e:
    print(e)

#26_SyntaxError         Raised when there is an error in the syntax of the code
try:
    eval('x === 2')
except SyntaxError as e:
    print(e)

#27_IndentationError    Raised when there is an indentation error in the code
try:
    eval('def func():\n print("Hello")\n print("World")')
except IndentationError as e:
    print(e)

#28_TabError    Raised when the indentation consists of inconsistent use of tabs and spaces
try:
    eval('def func():\n\tprint("Hello")\n   print(World)')
except TabError as e:
    print(e)
"""
#29_UnicodeError    Raised when a Unicode-related encoding or decoding error occurs
try:
    'æ'.encode('ascii')
except UnicodeError as e:
    print(e)