# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 21:00:17 2022

@author: BEEMO
"""
from sqlalchemy import create_engine
import pandas as pd
import pymysql
pymysql.install_as_MySQLdb()

#Always use colons " : " after the local host specification aka before the number
cxn = "mysql+pymysql://root:root@localhost:3307/Sakila"
#Create Engine object
engine = create_engine(cxn)
#Create queries and run 



# =============================================================================
# q = ''' 
# 
# SELECT 
# FROM 
# WHERE
# ;'''
#  = pd.read_sql(q, engine)
# =============================================================================
tables ='''SHOW TABLES;'''
tables_list = pd.read_sql(tables, engine)
# =============================================================================
cityq = ''' 

SELECT *
FROM city
;'''
city_table = pd.read_sql(cityq, engine)
# =============================================================================
acq = ''' 

SELECT *
FROM address
;'''
ac = pd.read_sql(acq, engine)

acq2 = ''' 

SELECT *
FROM address
;'''
ac2 = pd.read_sql(acq2, engine)
# =============================================================================
#888888888888888888888888888888888888888888888888888888888888888888888888888888
#888888888888888888888888888888888888888888888888888888888888888888888888888888
# =============================================================================
'''Queries'''
# Get all the customers inside city_id = 312? 
# Return the customers' first name, last name, email, address, and city 
# =============================================================================
city312q = ''' 

SELECT c.first_name, c.last_name, c.email, a.address, city.city
FROM customer AS c
JOIN address AS a 
ON a.
WHERE 
;'''
city312  = pd.read_sql(city312q, engine)

# =============================================================================
# Get all comedy films? Note that the genre is called the category 
# Return film title, description, release year, rating, and special features.
# =============================================================================


# =============================================================================
# Get all the films that Johnny Lollobrigida was in? 
# Return the actor's last name, film title, and release year 
# =============================================================================


# =============================================================================
# Get the first and last names of all the actors in the movie titled "Bingo Talented"
# =============================================================================

# =============================================================================
# Get the customer_id associated with all payments greater than twice the average payment amount? 
# (HINT: use 2* in your query to get twice the amount)
# Include the customer id and the amount
# =============================================================================

# =============================================================================
# Get a list the first and last names of the 5 customers who have the highest number(count) of payments
# Title the number of payments as num_payments
# =============================================================================


