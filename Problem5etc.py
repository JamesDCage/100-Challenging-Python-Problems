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

# q = lambda d: int((2 * 50 * d / 30) ** 0.5)
# numstring = "100,150,180" # input("Comma separated numbers, please: ")
# result_list = list(map(q,[int(i) for i in numstring.split(',')]))
# print (str(result_list)[1:-1].replace(' ',''))



# Author's Solution (I replaced "raw input" with my test string and 
# added parens to print statement.)

# import math
# c=50
# h=30
# value = []
# items=[x for x in numstring.split(',')]
# for d in items:
#     value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

# print (','.join(value))


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

# x, y = 7, 7
# array = []
# for i in range(x):
#     array.append([i * j for j in range(y)])
# print(array)

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

# Question: 8
# Write a program that accepts a comma separated sequence of words as input and prints the words in a 
# comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

# test_text = "without,hello,bag,world"
# test_list = sorted(test_text.split(','))
# print ",".join(test_list)


# Question 9
# Write a program that accepts sequence of lines as input and prints the lines after making all characters 
# in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

# test_lines = """

# blah blah blah blah 
# two blah
# three blah
# this is a test of the emergency broadcast system. this is only a test

# """

# print(test_lines).upper()


# Question 10
# Level 2

# Question:
# Write a program that accepts a sequence of whitespace separated words as input and prints the words after
# removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

# test_string = "hello world and practice makes perfect and hello world again"
# test_list = sorted(list(set(test_string.split())))
# print " ".join(test_list)

# Question 11:
# Write a program which accepts a sequence of comma separated 4 digit binary numbers 
# as its input and then check whether they are divisible by 5 or not. The numbers that are divisible 
# by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.

# raw_string = "0100,0011,1010,1001,0101,1111"
# bin_set = [x for x in raw_string.split(',') if int(x,2) % 5 == 0]
# print(" ".join(bin_set))

# Solution:
# value = []
# items=[x for x in raw_input().split(',')]
# for p in items:
#     intp = int(p, 2)
#     if not intp%5:
#         value.append(p)

# print ','.join(value)

# My solution is better. :-)

# Question 12:
# Write a program, which will find all such numbers between 1000 and 3000 
# (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# odds = set([c for c in "13579"])
# all_evens = []
# for i in range(1000,3001):
#     if not odds & set([c for c in str(i)]):
#         all_evens.append(str(i))
# print(','.join(all_evens))

# Solution:
# values = []
# for i in range(1000, 3001):
#     s = str(i)
#     if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
#         values.append(s)
# print ",".join(values)

# Both are good solutions, but mine is extensible for longer or shorter numbers.
    
# Question 13:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

# test_string = 'hello world! 123'
# num_letters = num_digits = 0
# for i in test_string:
#     if i.isalpha():
#         num_letters += 1
#     elif i.isdigit():
#         num_digits += 1
# print("LETTERS "+str(num_letters))
# print("DIGITS "+str(num_digits))
    

# Solution:
# s = raw_input()
# d={"DIGITS":0, "LETTERS":0}
# for c in s:
#     if c.isdigit():
#         d["DIGITS"]+=1
#     elif c.isalpha():
#         d["LETTERS"]+=1
#     else:
#         pass
# print "LETTERS", d["LETTERS"]
# print "DIGITS", d["DIGITS"]

# Offical solution - why the heck the else:pass? Why a dictionary?

# I skipped questions 14 and 15

# Question 16:
# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,3,5,7,9
# THE TEXT SAYS SQUARE, SO I'LL SQUARE EVEN IF THE EXAMPLE DOES NOT SQUARE

# test_input = "1,2,3,4,5,6,7,8,9"
# test_list = [str(int(x) ** 2) for x in test_input.split(',') if int(x) % 2 == 1]
# print ','.join(test_list)

# Solution:
# values = raw_input()
# numbers = [x for x in values.split(",") if int(x)%2!=0]
# print ",".join(numbers)

# Again, problem statement said square each number. Boo

# Question 17:
# Write a program that computes the net amount of a bank account based a transaction log 
# from console input. The transaction log format is shown as following:
# D 100
# W 200

# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500

# test_input = """D 300
# D 300
# W 200
# D 100"""

# balance = 0
# for line in test_input.splitlines():
#     if line[0] == 'D':
#         balance += int(line[2:])
#     elif line[0] == 'W':
#         balance -= int(line[2:])
# print(balance)


# Solution:
# netAmount = 0
# while True:
#     s = raw_input()
#     if not s:
#         break
#     values = s.split(" ")
#     operation = values[0]
#     amount = int(values[1])
#     if operation=="D":
#         netAmount+=amount
#     elif operation=="W":
#         netAmount-=amount
#     else:
#         pass
# print netAmount

# Again with an else-pass. I brought in all the input, which 
# was not in the spirit of the problem, so boo me. But I learned
# about splitlines.

# Question 18
# Level 3
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check 
# them according to the above criteria. Passwords that match the criteria are to be printed, each 
# separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1

valid_pws = []
specials = set(['$', '#', '@'])
test_input = 'ABd1234@1,a F1#,2w3E*,2We3345)'
for pw in test_input.split(','):
    len_good = len(pw) >=6 and len(pw) <= 13
    has_upper = has_lower = has_digit = has_special = False
    for c in pw:
        has_upper = has_upper or c.isupper
        has_lower = has_lower or c.islower
        has_digit = has_digit or c.isdigit
        has_special = has_special or c in specials
    if len_good and has_upper and has_lower and has_digit and has_special:
        valid_pws.append(pw)
print (','.join(valid_pws))
        
# Solutions:
# import re
# value = []
# items=[x for x in raw_input().split(',')]
# for p in items:
#     if len(p)<6 or len(p)>12:
#         continue
#     else:
#         pass
#     if not re.search("[a-z]",p):
#         continue
#     elif not re.search("[0-9]",p):
#         continue
#     elif not re.search("[A-Z]",p):
#         continue
#     elif not re.search("[$#@]",p):
#         continue
#     elif re.search("\s",p):
#         continue
#     else:
#         pass
#     value.append(p)
# print ",".join(value)  

# Learn - can create list like this: [a-z]
# Learn - import re, search
# And write this guy a letter about useless elses and passes
# And again: [x for x in raw_input().split(',')]. Why not just raw_input().split(',')??

# Question regarding lists - I messed around with lists on other sites
# and wrote this based on an example I found.

# class account(object):
#     def __init__(self, name, balance = 0.0):
#         self.balance = balance
#         self.name = name
        
#     def deposit(self, add_this):
#         self.balance += add_this
#         return self.balance
        
#     def withdraw(self, sub_this):
#         self.balance -= sub_this
#         return self.balance
        
# user1 = account("james", 3.0)
# user1.deposit(134000.3)
# user1.withdraw(45.2)

# print (user1.balance)
# print (user1.name)

