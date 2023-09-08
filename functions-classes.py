# PPHA 30535: Python Programming for Public Policy
# Spring 2023
# HW2: Functions & Classes
# Author: Danya Sherbini

#############

# Question 1: Write a function that takes two numbers as arguments, then
# sums them together.  If the sum is greater than 10, return the string 
# "big", if it is equal to 10, return "just right", and if it is less than
# 10, return "small".  Apply the function to each tuple of values in the 
# following list, with the end result being another list holding the strings 
# your function generates (e.g. ["big", "big", "small"]).

start_list = [(10, 0), (100, 4), (0, 0), (-15, -100), (5, 4)]

# creating the function 
def func_sum(x, y): # x and y as the two arguments
    new_sum = x + y # defining variable for the sum of x and y 
    if new_sum > 10: # using if and elif to return statements
        return 'big'
    elif new_sum == 10:
        return 'just right'
    elif new_sum < 10:
        return 'small'

# using a list comprehension to produce a new list with the function
new_list = [func_sum(x, y) for x, y in start_list]

# printing the new list
print(new_list)
        

# Question 2: The following code is fully-functional, but uses a global
# variable and a local variable.  Re-write it to work the same, but using an
# argument and a local variable.  Use no more than two lines of comments to
# explain why this new way is preferable to the old way.

# a = 10
# def my_func():
   # b = 30
   # return a + b
# x = my_func() 

# my solution:
def my_func(a): # moved a from global variable to an argument
    b = 30 # kept b as a local variable
    return a + b

x = my_func(10) # inputted 10 for a

print(x) # still yields 40

# this way is preferable because it doesn't rely on 'a' being set outside of the 
# function, making it more flexible and easier to use than if 'a' were hard-coded.



# Question 3: Write a function that can generate a random password from
# upper-case and lower-case letters, numbers, and special characters 
# (!@#$%^&*).  It should have an argument for password length, and should 
# check to make sure the length is between 8 and 16, or else warn the user 
# and exit.  Your function should also have a keyword argument named 
# "special_chars" that defaults to True.  If the function is called with the 
# keyword argument set to False instead, then the random values chosen should
# not include special characters.  Create a second similar keyword argument 
# for numbers. Use one of the two libraries below.

import random
# from numpy import random

# creating the function
def pass_func(length, special = True, num = False): # adding in args and kwargs
    length = int(length) # making length an integer
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' # defining letters
    numbers = '123456789' # defining numbers
    special_chars = '!@#$%^&*' # defining special characters
    while True:
        if length < 8 or length > 16: # if inputted length is less than 8 or more than 16
            print("Sorry, too short.") # print this
            break # and end the function
        if length >= 8 or length <= 16: # if the length is 8-16 then
            # apply these conditions depending on special and num arguments
            if special == True and num == False:
                alphabet = letters + special_chars
                # .join joins together the random symbols chosen with random.choice()
                password = ''.join(random.choice(alphabet) for i in range(length))
            elif special == True and num == True:
                alphabet = letters + special_chars + numbers
                password = ''.join(random.choice(alphabet) for i in range(length))
            elif special == False and num == True:
                alphabet = letters + numbers
                password = ''.join(random.choice(alphabet) for i in range(length))
            elif special == False and num == False:
                alphabet = letters
                password = ''.join(random.choice(alphabet) for i in range(length))
            return password


# testing out the function
pass_func(8) # with only the length argument + defaults
pass_func(8, True, True) # with letters + special chars + numbers
pass_func(12, False, True) # with only letters + numbers
pass_func(16, False, False) # with only letters


# Question 4: Create a class that requires four arguments when an instance
# is created: one for the person's name, one for which COVID vaccine they
# have had, one for how many doses they've had, and one for whether they've
# ever had COVID.  Then create instances for four people:
#
# Aaron, Moderna, 3, False
# Ashu, Pfizer, 2, False
# Alison, none, 0, True
# Asma, Pfizer, 1, True
#
# Write two methods for this class, and one function:
# The first method named "get_record", which prints out a one-sentence summary
# of a specified person's records (e.g. Ashu has two doses of Phizer and...)
#
# The second method named "same_shot", which takes as an argument another person's
# record instance, and then prints whether or not the two people have the
# same kind of vaccine or not.
#
# A function named "all_data", which takes a container holding any number of these 
# instances and returns a simple list of all of their data 
# (e.g. [name, vaccine, doses, covid], [...])


# creating the class
class CovidInfo():
    def __init__(self, name, vaccine, num_doses, had_covid): # initializing the class and inputting my arguments
        self.name = name
        self.vaccine = vaccine
        self.num_doses = num_doses
        self.had_covid = had_covid
        
    def get_record(self): # creating the first method
        if self.had_covid == True: # if had_covid = True
            self.covid_history = 'has had covid.' # print this
        else:
            self.covid_history = 'has not had covid.' # othwerwise print this
        if self.num_doses == 0 and self.vaccine == 'none': # if num_doses = 0 and vaccine input is "none"
            self.vaccine = 'any vaccine' # print this (to ensure a proper sentence output)
        elif self.num_doses == 1:
            self.num_doses = "1 dose" # accounting for singular "dose" vs plural "doses"
        else:
            self.num_doses = f'{self.num_doses} doses'
        # putting everything together into a sentence as the final output of this method
        record = f'{self.name} has {self.num_doses} of {self.vaccine} and {self.covid_history}' 
        return record
        
    def same_shot(self, record): # creating the second method
        self.record = record
        # if the vaccine is the same as the one for the new record passing through the method
        if self.vaccine == record.vaccine: 
            print('Same vaccine') # then print this
        else:
            print('Different vaccine') # otherwise print this
            

# creating the instances using the info from the prompt
record1 = CovidInfo('Aaron', 'Moderna', 3, False)
record2 = CovidInfo('Ashu', 'Pfizer', 2, False)
record3 = CovidInfo('Alison', 'none', 0, True)
record4 = CovidInfo('Asma', 'Pfizer', 1, True)

# applying get_record() method to each instance
record1.get_record()
record2.get_record()
record3.get_record()
record4.get_record()

# testing out the same_shot() method with a few different combinations
record2.same_shot(record4)
record2.same_shot(record3)

# creating the function all_data
def all_data(record_list):
    all_records = [[record.name, record.vaccine, record.num_doses, record.had_covid] for record in record_list]
    return all_records

# creating a list of all the instances
record_list = [record1, record2, record3, record4]

# applying the all_data function
all_data(record_list)
    







