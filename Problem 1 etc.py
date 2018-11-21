"""
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""
# Problem 1
#  
# My solution: 
# print(str([x for x in range(2000,3201) if x % 7 == 0 and x % 5 != 0])[1:-1].replace(" ", ""))
#
# Slightly more readable, using join method instead of replace:
#
# l=[str(x) for x in range(2000,3201) if x % 7 == 0 and x % 5 != 0]
# print (','.join(l))


# Problem 2

def my_factorial(x):
    fact = 1
    for i in range(1, x+1):
        fact *= i
    return fact

# print(my_factorial(8))

# Problem 3

def square_dict(x):
    return {i:i**2 for i in range(1, x+1)}

# print (square_dict(8))

# problem 4

# Question:
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')


# x = input("Give me comma-separated numbers: ")

x = '4,27,19,65'
x_list = x.split(",")
x_tuple = tuple(x_list)
print (x_list, x_tuple)


y_list = [int(i) for i in x_list]


for i in range (0,len(y_list),2):
    print(y_list[i], end = " ")

# y_list is list of integers
# r = lambda x: x * 12
# # Apply r to every element in y_list
# # & print the resulting list
# print (list(map(r, y_list)))

# print (list(map(lambda x: 12 * x, y_list)))