#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 7 16:19:59 2022

@author: Shareef Shaik
"""

#####################################################
###### Practice Problem 12.10, Page 435 #############
#####################################################

# 12.10 Write SQLqueries on table Weather Data in Figure 12.16 that return:
# (a) All the records for the city of London
# (b) All the summer records
# (c) The city, country, and season for which the average temperature is less than 20 
# (d) The city, country, and season for which the average temperature is greater than 20  and the total rainfall is less than 10 mm
# (e) The maximum total rainfall
# (f) The city, season, and rainfall amounts for all records in descending order of rainfall
# (g) The total yearly rainfall for Cairo, Egypt
# (h) The city name, country, and total yearly rainfall for every distinct city



#####################################################
###### Practice Problem 12.11, Page 436 #############
#####################################################

# 12.11 Using module sqlite3, create a database file weather.db and table WeatherData in it. 
# Define the column names and types to match those in the table in Figure 12.16; 
# then enter all the rows shown into the table. 


import sqlite3
con = sqlite3.connect("weather.db")
cur=con.cursor()

cur.execute ( """CREATE TABLE WeatherData (City text, 
             Country text, 
             Season int, 
             Temperature float, 
             Rainfall float)""" )

cur.execute (""" INSERT INTO WeatherData 
             VALUES ('Mumbai', 'India', 1, 24.8, 5.9) """)

cur.execute (""" INSERT INTO WeatherData 
             VALUES ('Mumbai', 'India', 2, 28.4, 16.2) """)
             
cur.execute (""" INSERT INTO WeatherData 
             VALUES ('Mumbai', 'India', 3, 27.9, 1549.4) """)
            
cur.execute (""" INSERT INTO WeatherData 
             VALUES ('Mumbai', 'India', 4, 27.6, 346.0) """)
             
cur.execute (""" INSERT INTO WeatherData 
             VALUES ('London', 'United Knigdom', 1, 4.2, 207.7) """)
             
cur.execute (""" INSERT INTO WeatherData 
             VALUES ('London', 'United Knigdom', 2, 8.3, 169.6) """)
             
cur.execute (""" INSERT INTO WeatherData 
             VALUES ('London', 'United Knigdom', 3, 15.7, 157.0) """)             
             
cur.execute (""" INSERT INTO WeatherData 
             VALUES ('London', 'United Knigdom', 4, 10.4, 218.5) """)             
             
cur.execute (""" INSERT INTO WeatherData 
             VALUES ('Cairo', 'Egypt', 1, 13.6, 16.5) """)             
             
cur.execute (""" INSERT INTO WeatherData 
             VALUES ('Cairo', 'Egypt', 2, 20.7, 6.5) """)             

cur.execute (""" INSERT INTO WeatherData 
             VALUES ('Cairo', 'Egypt', 3, 27.7, 0.1) """)
             
cur.execute (""" INSERT INTO WeatherData 
             VALUES ('Cairo', 'Egypt', 3, 22.2, 4.5) """)

con.commit()
             
#####################################################
###### Practice Problem 12.12, Page 436 #############
#####################################################

# 12.12 Using sqlite3 and within the interactive shell, open the database file weather.db you 
# created in Problem 12.11 and execute the queries from Problem 12.10 by running appropriate Python statements. 

# (a) All the records for the city of London

sql1 = "SELECT * FROM WeatherData WHERE City = 'London'"
cur.execute(sql1)
a = cur.fetchall()

# (b) All the summer records

# Winter (1), Spring (2), Summer (3), and Fall (4)

sql2 = "SELECT * FROM WeatherData WHERE Season = 3"
cur.execute(sql2)
b = cur.fetchall()

# (c) The city, country, and season for which the average temperature is less than 20 

sql3 = "SELECT City, Country, Season FROM WeatherData WHERE Temperature < 20 "
cur.execute(sql3)
c = cur.fetchall()

# (d) The city, country, and season for which the average temperature is greater than 20  and the total rainfall is less than 10 mm

sql4 = "SELECT City, Country, Season FROM WeatherData WHERE Temperature > 20 and Rainfall < 10"
cur.execute(sql4)
d = cur.fetchall()

# (e) The maximum total rainfall

sql5 = "SELECT MAX(Rainfall) FROM WeatherData"
cur.execute(sql5)
e = cur.fetchall()

# (f) The city, season, and rainfall amounts for all records in descending order of rainfall

sql6 = "SELECT City, Season, Rainfall FROM WeatherData ORDER BY Rainfall DESC"
cur.execute(sql6)
f = cur.fetchall()

# (g) The total yearly rainfall for Cairo, Egypt

sql7 = "SELECT SUM(Rainfall) FROM WeatherData WHERE City = 'Cairo' "
cur.execute(sql7)
g = cur.fetchall()

# (h) The city name, country, and total yearly rainfall for every distinct city

sql8 = "SELECT DISTINCT City, Country, Sum(Rainfall) FROM WeatherData Group by City "
cur.execute(sql8)
h = cur.fetchall()

cur.close()   
con.close()
