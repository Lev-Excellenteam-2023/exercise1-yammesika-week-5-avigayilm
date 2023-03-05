import random
from datetime import datetime
import time

'''
Program that returns me a random date between 2 inputted dates from the user
if the random day falls on monday it print I don't have vinaigrette!
the random date is always printed at the end.
'''

def input_date_time(number):
    '''
    get's an input from the user and checks if it's in correct dateformat
    :param number: get's what number of date it has to input
    :return: returns the date
    '''
    while True:
        try:
            dateObject=input("enter {} date (in YYYY/MM/DD)\n".format(number))
            dateObject = datetime.strptime(dateObject,"%Y/%m/%d").date()
            return dateObject
        # If the date validation goes wrong
        except ValueError:
            print("input is not correct format")

date1=input_date_time("first")
date2=input_date_time("second")
# check what date is the earlier date
if date1>date2:
    first=date2
    last=date1
else:
    first=date1
    last=date2
#gives a random date between the 2 dates
random_date = first + (last-first) * random.random()
# the weekday number of monday is 0
dat_of_week = random_date.weekday()
if day_of_week==0:
    print("I don't have vinaigrette!")
print(random_date)

