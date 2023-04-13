#As a rule, the list contains elements of the same type, but can also contain elements of different types
#The list may be inside another list
from operator import le


number = 3
things = ['string', 0, [1, 2, number], 4.56]
print(things[1])
print(things[2][2])

#When you need to check for an item in the list, the "in" operator is used. It is assigned the value True if one character
#(or mi=ore than one) was found and False if none
words = ['spam', 'egg', 'spam', 'sausage']
print('spam' in words)
print('sausage' in words)
print('tomato' in words)
#Or you can use operator "not"
nums = [1, 2, 3]
print(4 not in nums)
print(3 not in nums)

print("-----------------------------------------------")
#-----------------------------------------------------------------------------------------------------------------------
#FUNCTIONS OF LISTS AND METHODS
#There are different methods for work with lists. You can view all the methods for a certain data type using the command:
print(dir(nums))
#For example, there is the one method "append". This is intended to add an item to the end of the list
nums.append(4)
print(nums)
#Another example is the method "insert". It allows you to insert a new item at any osition in the list, not just at the end
index = 1
words.insert(index, 'onion')
print(words)
#One more method is the method "index". Using the "index" method? you can find the first mention of an item in the list and output its index
letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))
#There are several other useful functions and methods for working with lists:
# max(list): return the list item with the highest value
# min(list): return the list item with the lowest value
# list.count(obj): returns the number of mentions of an item in the list
# list.remove(obj): removes an object from the list
# list.reverse(): arranges the items in reverse order

print("----------------------------------------------")
#----------------------------------------------------------------------------------------------------------------------------
#HOW TO COPY A LIST?
list_1 = ['a', 'b', 'c', 'd', 'e', 'f'] 
list_2 = list_1
list_2.extend(['c', 'k', 'u'])
print(list_1, "This is list_1")
print(list_2, "This is list_2")
list_3 = list_1[:] # This is how exactly we can copy a list or we can use method "copy" (list_3 = list_1.copy())
list_3.sort()
print(list_1, "This is list_1")
print(list_3, "This is list_3")

print("-----------------------------------------------")
#--------------------------------------------------------------------------------------------------------------------------
#LIST UNPACKING
a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(other)
print(d)

#----------------------------------------------------------------------------------------------------------------------------
#ARRAY
row = int(input("Enter a number of rows: "))
column = int(input("Enter a number of columns: "))
l = []
for i in range(row):
    tmp = []
    for j in range(column):
        tmp.append(i*j)
    l.append(tmp)
print(l)

