# Question 5 - skipped (has to do with classes)

# Question 6
# Level 2

# Question:
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24

q = lambda d: int((2 * 50 * d / 30) ** 0.5)
numstring = "100,150,180" # input("Comma separated numbers, please: ")
result_list = list(map(q,[int(i) for i in numstring.split(',')]))
print (str(result_list)[1:-1].replace(' ',''))



# Author's Solution (I replaced "raw input" with my test string and 
# added parens to print statement.)

import math
c=50
h=30
value = []
items=[x for x in numstring.split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print (','.join(value))


"""
Question 7
Level 2

Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in 
the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
"""

x, y = 10, 10
array = []
for i in range(x):
    array.append([i * j for j in range(y)])
print(array)

"""
Author's Solution

input_str = raw_input()
dimensions=[int(x) for x in input_str.split(',')]
rowNum=dimensions[0]
colNum=dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col

print multilist


My thoughts:

Getting past the raw input stuff, mine is a bit more compact. 
Interesting double-list comprehension to initialize blank array.
Problem description is a bit counter-intuitive. I think of x as number of 
columns and y as number of rows, as just one example.
"""