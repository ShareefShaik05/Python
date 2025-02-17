﻿#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 20:10:51 2022

@author: Shareef Shaik
"""

#####################################################
##### Practice Problem 2.1, Page 18 #################
#####################################################

# 2.1. Write Python algebraic expressions corresponding to the following statements:
# (a) The sum of the first five positive integers
1+2+3+4+5
# (b) The average age of Sara (age 23), Mark (age 19), and Fatima (age 31)
(23+19+31)/3
# (c) The number of times 73 goes into 403
403//73
# (d) The remainder when 403 is divided by 73
403%73
# (e) 2 to the 10th power
2**10
# (f) The absolute value of the di erence between Sara’s height (54 inches) and Mark’s height (57 inches)
abs(54-57)
# (g) The lowest price among the following prices: $34.99, $29.95, and $31.50
min(34.99,29.95,31.50)

#####################################################
##### Practice Problem 2.2, Page 19 #################
#####################################################

# 2.2. Translate the following statements into Python Boolean expressions and evaluate them:
# (a) The sum of 2 and 2 is less than 4.
2+2<4
# (b) The value of 7 // 3 is equal to 1 + 1
7//3 == 1+1
# (c) The sum of 3 squared and 4 squared is equal to 25
3**2+4**2==25
# (d) The sum of 2,4,and 6 is greater than 12. 
2+4+6>12
# (e) 1387 is divisible by 19.
1387%19==0
# (f) 31 is even. (Hint: what does the remainder when you divide by 2 tell you?) 
31%2==0
# (g) The lowest price among $34.99, $29.95, and $31.50 is less than $30.00.
min(34.99,29.95,31.50)<30.00

#####################################################
##### Practice Problem 2.3, Page 21 #################
#####################################################

# 2.3. Write Python statements that correspond to the actions below and execute them: 
# (a) Assign integer value 3 to variable a.
a=3
# (b) Assign 4 to variable b.
b=4
# (c) Assign to variable c the value of expression a * a + b * b.
c=a*a+b*b

#####################################################
##### Practice Problem 2.4, Page 25 #################
#####################################################

# 2.4. Start by executing the assignment statements:
# >>> s1 = 'ant' >>> s2 = 'bat' >>> s3 = 'cod'
s1='ant'
s2='bat'
s3='cod'
# Write Python expressions using s1, s2, and s3 and operators + and * that evaluate to: 
# (a) 'ant bat cod'
s1 + ' ' + s2 +' ' + s3
# (b) 'ant ant ant ant ant ant ant ant ant ant '
(s1 + ' ' )* 10
# (c) 'ant bat bat cod cod cod'
s1+(' ' + s2)*2+(' ' + s3)*3
# (d) 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat '
(s1+' '+s2+' ')*7
#(e) 'batbatcod batbatcod batbatcod batbatcod batbatcod '
(s2+s2+s3+' ')*5

#####################################################
##### Practice Problem 2.5, Page 26 #################
#####################################################
# Start by executing the assignment:
# s = '0123456789'
s='0123456789'
# Now write expressions using string s and the indexing operator that evaluate to: 
# (a) '0'
s[0]
#or
s[-10]
# (b) '1' 
s[1]
#or
s[-9]
# (c) '6' 
s[6]
# (d) '8' 
s[8]
#or
s[-2]
# (e) '9'
s[9]
#or
s[-1]

#####################################################
##### Practice Problem 2.6, Page 28 #################
#####################################################

# First execute the assignment
# words = ['bat', 'ball', 'barn', 'basket', 'badminton']
words = ['bat', 'ball', 'barn', 'basket', 'badminton']
# Now write two Python expressions that evaluate to the first and last, respectively, word in words, in dictionary order.
min(words)
max(words)
#or
words.sort()
words[0]
words[-1]

#####################################################
##### Practice Problem 2.7, Page 33 #################
#####################################################

# Given the list of student homework grades
#    >>> grades = [9, 7, 7, 10, 3, 9, 6, 6, 2]
grades = [9, 7, 7, 10, 3, 9, 6, 6, 2]
# write:
# (a) An expression that evaluates to the number of 7 grades 
grades.count(7)
# (b) A statement that changes the last grade to 4
grades[-1] = 4
#or
grades.remove(2)
grades.append(4)
print (grades)
# (c) An expression that evaluates to the maximum grade 
max(grades)
# (d) A statement that sorts the list grades
grades.sort()
# (e) An expression that evaluates to the average grade
sum(grades)/len(grades)

#####################################################
##### Practice Problem 2.8, Page 37 #################
#####################################################

# In what order are the operators in the following expressions evaluated? 
lst=[1,2,3]
# (a) 2 + 3 == 4 or a > = 5
((2 + 3) == 4) or (a >= 5)
# (b) lst [1] * -3 < -10 == 0
(((lst [1]) * -3) < -10) == 0
# (c) (lst[1] * -3 < -10) in [0, True]
(((lst[1]) * -3) < -10) in [0, True]
# (d) 2 * 3**2
2 * (3**2)
# (e) 4 / 2 in [1,2,3]
(4 / 2) in [1,2,3]

#####################################################
##### Practice Problem 2.9, Page 40 #################
#####################################################

# What is the type of the object that these expressions evaluate to? 
# (a) False + False
False + False
# (b) 2 * 3**2.0
2 * 3**2.0
# (c) 4//2+4%2
4//2 + 4 % 2
# (d) 2+3==4or5>=5
(2+3==4) or (5>=5)

#####################################################
##### Practice Problem 2.10, Page 42 #################
#####################################################

# Write Python expressions corresponding to the following:
# (a) The length of the hypotenuse in aright triangle whose other two sides have lengths a and b
h= (a**2 + b**2)**0.5
#or
import math
math.sqrt(a**2+ b**2)
# (b) The value of the expression that evaluates whether the length of the above hypotenuse is 5
h==5
#or
math.sqrt(a**2+b**2)==5
# (c) The area of a disk of radius a
math.pi* a**2
# (d) The value of the Boolean expression that checks whether a point with coordinates x and y is inside a circle with center (a, b) and radius r
r=5
x=1
y=1
math.sqrt((x-a)**2+((y-b)**2))< r






















