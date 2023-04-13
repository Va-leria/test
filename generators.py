# Generators are an iterated type, such as list or tuples.
# Generators create a sequence of items.
# Unlike lists, they can't be assigned arbitrary index, but they support for loops.
# Function range() is a generator, but range keep all items in memory, but yield keep one item,
# yield doesn't take up so much space in memory like range().
# They are created using functions and the yield statement.

# Example_1:
def countdown():
    i = 5
    while i > 0:
        yield i
        i -= 1

for i in countdown():
    print(i)
print("1-----------------")

# Example_2:
def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

print(list(numbers(11)))
print("2------------")

# Example_3:
def generator_function(num):
    for item in range(num):
        yield i

g = generator_function(100)
next(g)
next(g)
print(next(g))