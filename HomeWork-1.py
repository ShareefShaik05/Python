#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 16:20:35 2022

@author: Shareef Shaik
"""

#####################################################
##### Practice Problem 2.11, Page 45 #################
#####################################################

# 2.11 Write Python expressions corresponding to these statements:
# (a) The sum of negative integers  7 through  1
-7 + -6 + -5 + -4 + -3 + -2 + -1
# (b) The average age of a group of kids at a summer camp given than 17 are 9 years old, 24 are 10 years old, 21 are 11 years old, and 27 are 12 years old
((17*9) + (24*10) + (21*11) + (27*12))/(17 + 24 + 21 + 27)
# (c) 2 to the power - 20
2** -20
# (d) The number of times 61 goes into 4356
4356 % 61
# (e) The remainder when 4365 is divided by 61
4365 // 61

#####################################################
##### Practice Problem 2.14, Page 46 #################
#####################################################

# 2.14 Start by executing s = 'goodbye'
# Note: These seven statements should evaluate to True, False, False, False, True, False, and False, respectively.
s = 'goodbye'
# Then write a Boolean expression that checks whether: 
# (a) The first character of strings is 'g'
s[0]=='g'
# (b) The seventh character of s is 'g'
s[6]=='g'
# (c) The first two characters of s are 'g' and 'a'
s[0]=='g' and s[1]=='a' 
# (d) The next to last character of s is 'x'
s[-2]=='x'
# (e) The middle character of sis 'd'
s[3]=='d'
# (f) The first and last characters of string s are equal
s[0]==s[-1]
# (g) The last four characters of string s match the string 'tion'
s[-4:-1]=='tion'

#####################################################
##### Practice Problem 2.16, Page 46 #################
#####################################################

# 2.16 Write the corresponding Python assignment statements:
# (a) Assign 6 to variable a and 7 to variable b.
a=6
b=7
# (b) Assign to variable c the average of variables a and b.
c=(a+b)/2
# (c) Assign to variable inventory the list containing strings 'paper','staples',and 'pencils'.
inventory=['paper','staples','pencils']
# (d) Assign to variables first, middle and last the strings 'John', 'Fitzgerald', and 'Kennedy'.
first='John'
middle='Fitzgerald'
last='Kennnedy'
# (e) Assign to variable fullname the concatenation of string variables first, middle, and last. Make sure you incorporate blank spaces appropriately.
fullname= first + ' ' + middle + ' ' + last

#####################################################
##### Practice Problem 2.17, Page 46 #################
#####################################################

# 2.17 Using variables defined in Exercise 2.16, write Boolean expressions corresponding to the following logical statements and evaluate the expressions:
# (a) The sum of 17 and - 9 is less than 10.
(17 + (-9))< 10
# (b) The length of list inventory is more than five times the length of string full name. 
len(inventory) > 5 * len(fullname)
# (c) c is no more than 24.
c< 24
# (d) 6.75 is between the values of integers a and b.
a < 6.75 < b 
# (e) The length of string middle is larger than the length of string first and smaller than the length string last.
len(last) > len(middle) > len(first)
# (f) Either the list inventory is empty or it has more than 10 objects in it.
len(inventory)==0 or len(inventory)>10

#####################################################
##### Practice Problem 2.22, Page 47 #################
#####################################################

# 2.22 The range of a list of numbers is the largest diff erence between any two numbers 
# in the list. Write a Python expression that computes the range of a list of numbers lst. 
# If the list lst is, say, [3, 7, -2, 12], the expression should evaluate to 14 
# (the diff erence between 12 and  2).
lst= [3, 7, -2, 12]
max(lst) - min(lst)

#####################################################
##### Practice Problem 2.29, Page 49 #################
#####################################################

# 2.29 Add one or more pairs of parentheses to each expression so that it evaluates to True. 
# (a) 0==1==2
(0) == (1==2)
# (b) 2+3==4+5==7
(2 + (3==4) +5) ==7
# (c) 1<-1==3>4
(1<-1) == (3>4)

# For each expression, explain in what order the operators were evaluated.


















