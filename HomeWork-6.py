﻿#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 10:15:38 2022

@author: Shareef Shaik
"""

# Complete the following exercises from the textbook:

# 6.11, 6.21, 6.24, 6.25, 6.33

# Submit your assignment in a single .py file that uses comments to clearly label each problem. Contact the instructor ASAP if you have any questions.


#####################################################
###### Practice Problem 6.11, Page 175 ##############
#####################################################

# Implement function easyCrypto() that takes as input a string and prints its encryption defined as follows: 
# Every character at an odd position i in the alphabet will be encrypted with the character at position i + 1, and every character at an even position i will be encrypted with the character at position i   1. 
# In other words, ‘a’ is encrypted with ‘b’, ‘b’ with ‘a’, ‘c’ with ‘d’, ‘d’ with ‘c’, and so on. Lowercase characters should remain lowercase, and uppercase characters should remain uppercase.
# >>> easyCrypto('abc') 
# bad
# # >>> easyCrypto('ZOO') 
# YPP

def easyCrypto(word): 
    crypt = '' 
    length= len(word)
    for i in range(length): 
        if ord(word[i]) % 2 == 0: 
            crypt += chr(ord(word[i]) - 1) 
        else: 
            crypt += chr(ord(word[i]) + 1) 
    return crypt

easyCrypto('abc') 
easyCrypto('ZOO') 

#####################################################
###### Practice Problem 6.21, Page 195 ##############
#####################################################

# Write function ticker() that takes a string (the name of a file) as input. 
# The file will contain company names and stock (ticker) symbols. 
# In this file, a company name will occupy a line, and its stock symbol will be in the next line.
# Following this line will be a line with another company name, and so on. 
# Your program will read the file and store the name and stock symbol in a dictionary.
# Then it will provide an interface to the user so that the user can obtain the stock symbol for a given company. 
# Test your code on the NASDAQ 100 list of stock given in file nasdaq.txt.
# >>> ticker('nasdaq.txt') 
# Enter Company name: YAHOO
# Ticker symbol: YHOO
# Enter Company name: GOOGLE INC
# Ticker symbol: GOOG
# ...


def ticker(file):
    company = input("Enter Company name: ")
    file= 'nasdaq.txt'
    infile=open(file)
    content = open(file, "r")
    s= content.readline()
    infile.close()
    sym = ''
    while s:
        if s.strip() == company:
            sym = content.readline()
            sym= sym.strip()
            break
        else:
            s = content.readline()
    while sym:
        print ("Ticker symbol: {}".format(sym))
        break
  
ticker('nasdaq.txt')      

def ticker(file):
    infile= open(file)
    b=infile.readlines()
    infile.close()
    d= {}
    n=len(b)
    for i in range(0,n+1, 2):
        if len(b[i].strip()) ==0:
            continue
        else:
            d[b[i].strip()]= b[i+1].strip()
        while 1:
            tick = input("Enter Company name: ")
            if tick in d:
                print (" Ticker symbol: ", d[tick])
            else:
                break

ticker('nasdaq.txt')      

#####################################################
###### Practice Problem 6.24, Page 196 ##############
#####################################################

# Implement function names() that takes no input and repeatedly asks the user to enter the first name of a student in a class. 
# When the user enters the empty string, the function should print for every name the number of students with that name.
# >>> names()
# Enter next name: Valerie
# Enter next name: Bob
# Enter next name: Valerie
# Enter next name: Amelia
# Enter next name: Bob
# Enter next name:
# There is 1 student named Amelia
# There are 2 students named Bob
# There are 2 students named Valerie

def names():
      count = {}

      while True:
            name = input("Enter next name: ")
            if name == "":
                  break
            elif name in count:
                  count[name] += 1
            else:
                  count[name] = 1
                  
      for i in count:
          if count[i]==1:
              print("There is 1 student named {}".format(i))
          else:
              print("There are {} students named {}".format(count[i],i))

names()
            
#####################################################
###### Practice Problem 6.25, Page 197 ##############
#####################################################

# Write function different() that takes a two-dimensional table as input and returns the number of distinct entries in the table.
# >>> t = [[1,0,1],[0,1,0]]
# >>> different(t)
# 2
# >>> t = [[32,12,52,63],[32,64,67,52],[64,64,17,34],[34,17,76,98]]
# >>> different(t)
# 10

def different(t):
    num= {}
    counter=0
    for i in t:
        for j in i:
            if j not in num:
                counter +=1
                num[j]=1
    return counter

t = [[1,0,1],[0,1,0]]
different(t)

t = [[32,12,52,63],[32,64,67,52],[64,64,17,34],[34,17,76,98]]
different(t)
             
#####################################################
###### Practice Problem 6.33, Page 199 ##############
#####################################################

# Write function diceprob() that takes as input a possible result r of a roll of pair of dice 
# (i.e. an integer between 2 and 12) and simulates repeated rolls of a pair of dice until 100 rolls of r have been obtained.
# Your function should print how many rolls it took to obtain 100 rolls of r.
# >>> diceprob(2)
# It took 4007 rolls to get 100 rolls of 2
# >>> diceprob(3)
# It took 1762 rolls to get 100 rolls of 3
# >>> diceprob(4)
# It took 1058 rolls to get 100 rolls of 4
# >>> diceprob(5)
# It took 1075 rolls to get 100 rolls of 5
# >>> diceprob(6)
# It took 760 rolls to get 100 rolls of 6
# >>> diceprob(7)
# It took 560 rolls to get 100 rolls of 7

import random
def diceprob(r):
    a = 0
    counter=0
    while counter < 100:
        value = random.randrange(2, 13)
        a+= 1
        if value == r:
            counter+= 1
    print("It took {} rolls to get {} rolls of {}".format(a, counter, r))

diceprob(5)






















