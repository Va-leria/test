# EXEPTIONS
# These are situations when something goes wrong, usually due to errors in the code
# or incorrect input. When an exeption occurs, the program stops immediately.
# The most common exeptions:
# ImportError: import failed;
# IndexError: index isn't included in the range of list items;
# NameError: attempt to use non-existent variable;
# SyntaxError: code parsing error;
# TypeError: a value of an incompatible type has been passed to the function;
# ValueError: a value of a compatible type has been passed to the function, but with an incorrect value

# Try/exept

# Example_1:
try:
    num1 = 7
    num2 = 0
    print(num1/num2)
    print('Done calculation')
except  ZeroDivisionError:
    print('An error ocurred due to zero division')
print('--------------')

# Example_2:
try:
    var = 10
    print(var + 'hello')
    print(var/2)
except ZeroDivisionError:
    print('Divided by zero')
except (ValueError, TypeError):
    print('Error occured')
print('--------------')

# Example_3:
try:
    word = 'spam'
    print(word/0)
except:
    print('An error occured')
print('--------------')

# Example_4 with finally:
try:
    print('Hello')
    print(1/0)
except ZeroDivisionError:
    print('Divided by zero')
finally:
    print('This code will run no matter what')

# ASSERTION 
# Assertion is a validation of the code; it can be turned on or off when the program is tested

# Example_5:
print(1)
assert 2 + 2 == 4
print(2)
#assert 1 + 1 == 3
#print(3)

# Example_6:
temp = -10
assert (temp >= 0), "Colder than absolute zero!"


# Example_7:
class CustomException(Exception):
    """Exeption raised for custom purpose

    Attributes:
       message -- explanation of te error    
    """
    def __init__(self, message):
        self.message = message

num = int(input())

try:
    if num < 10:
        raise CustomException("Input is less than 10")
    elif num > 10:
        raise CustomException("Input is greater than 10")
except CustomException as ce:
    print("The error raised:" + ce.message)