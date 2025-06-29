"""
n = 10
try:
    res = n / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("can't divide by Zero")

#difference between Error and Exception
print("Hello World") #without closing parenthensis ) or " SyntaxError happens

n = 10
res = n / 0

#testing try - except - else - finally

try:
    n = 0
    res = 100 / n
except ZeroDivisionError:
    print("You can't Divide by Zero")
except ValueError:
    print("Enter a valid number")
else:
    print("Result is ", res)
finally:
    print("Execution complete")

#catching specifiq exceptions
try:
    x = int("str")
    inv = 1 / x
except ValueError:
    print("casting not Valid")
except ZeroDivisionError:
    print("Zero has no inverse!")
"""
#catching multiple exceptions
a = ["10", "twenty", 30]
try:
    total = int(a[0]) + int(a[1])
except (ValueError, TypeError) as e:
    print("Error ", e)
except IndexError:
    print("Index out of range.")