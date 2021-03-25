# # import a package
# from random import random # this package generates random numbers
import math
#
# print(random())  # it generates random number
#
# num_float = 23.6
# print("Actual float value " + str(num_float))
# print(math.ceil(num_float))  # if number .5 round it up
# # ceil() rounds up the value
# print(math.floor(num_float)) # if number .4 or less round it down
# # floor() round down the number


# Python modules:
import os
import datetime, sys
working_directory = os.getcwd()
print(working_directory)

# print(os.uname()) #works on Linux
print((os.cpu_count())) # shows number of cpu's, counts the virtual cores
print(datetime.datetime.today()) # returns current date and time
print(datetime.date.today()) # returns just current date
print(sys.path)
print(math.pi)



