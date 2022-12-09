#Chapter 1 - Exercise 3
#Program to display date and time
import datetime
now = datetime.datetime.now() # to get the CURRENT date and time
print("The current date and time is:")
print(now.strftime("%Y-%m-%d %H:%M:%S")) # convert to a string