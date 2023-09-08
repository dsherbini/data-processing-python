# PPHA 30537: Python Programming for Public Policy
# Spring 2023
# HW1: Lists, Dictionaries, and Loops
# Author: Danya Sherbini

#############

# Question 1: Using a for loop, write code that takes in any list of objects, then prints out:
# "The value at position __ is __" for every element in the loop, where the first blank is the
# index location and the second blank the object at that index location.

# creating a list
names = ['RM', 'Jin', 'Suga', 'J-Hope','Jimin', 'V', 'Jungkook']

# creating the for loop using my list
# I referenced this webpage when using enumerate() function below: https://realpython.com/python-enumerate/
for index, name in enumerate(names): # using enumerate() function to iterate over both index and name
    print(f'The value at position {index} is {name}')
    
# alternate way to do the for loop
for name in names: # only iterating on name here
    index = names.index(name) # creating index variable within the loop and using index() 
    # function on the names list to call the index for each value in the list
    print(f'The value at position {index} is {name}')


# Question 2: A palindrome is a word or phrase that is the same both forwards and backwards. Write
# code that takes a variable of any string, then tests to see whether it qualifies as a palindrome.
# Make sure it counts the word "radar" and the phrase "A man, a plan, a canal, Panama!", while
# rejecting the word "Apple" and the phrase "This isn't a palindrome". Print the results of these
# four tests.

# creating a function to test if string is a palindrome
# decided to use a function based on my knowledge of functions in R
# referenced this webpage for function syntax in python: https://www.freecodecamp.org/news/python-functions-define-and-call-a-function/
def palindrome(string): # naming the function and defining the input as 'string'
    clean_string = string.lower().replace(' ', '').replace(',', '').replace('!', '').replace("'", '') # removing commas, 
    # spaces, exclamation point, and apostrophe from the string
    if clean_string == clean_string[::-1]: # if the new cleaned up string = the reverse of itself 
    # (using slicing to make the string start at the last element)
        return("This is a palindrome") # then return this
    else: # if not then
        return("Sorry, this is not a palindrome") # return this

# running my tests strings through the function I've created
palindrome('radar')

palindrome('A man, a plan, a canal, Panama!')

palindrome('Apple')

palindrome("This isn't a palindrome")


# Question 3: The code below pauses to wait for user input, before assigning the user input to the
# variable.  Beginning with the given code, check to see if the answer given is an available
# vegetable.  If it is, print that the user can have the vegetable and end the bit of code.  If
# they input something unrecognized by our list, tell the user they made an invalid choice and make
# them pick again.  Repeat until they pick a valid vegetable.
available_vegetables = ['carrot', 'kale', 'radish', 'pepper']
choice = input('Please pick a vegetable I have available: ')

# making a while loop
while choice in available_vegetables: # if the choice inputted is in the list
    print("You can have the vegetable.") # then print this
    break # if in the list, end the loop
while choice not in available_vegetables: # if not in the list
    choice = input('Sorry, invalid. Please pick another vegetable I have available: ') 
    # then prompt them to choose a new one
    if choice in available_vegetables: # if that's in the list
        print("Yay! You can have the vegetable!") # then print this


# Question 4: Write a list comprehension that starts with any list of strings, and returns a new
# list that contains each string in all lower-case letters, but only if the string begins with the
# letter "a" or "b".

# creating a list of strings
fruits = ['Watermelon', 'aPPLE', 'Apricot', 'Blueberry', 'bANANA', 'Raspberry', 'Guava']

# creating the new list
fruits_ab = [fruit.lower() # will output the strings in lowercase
             for fruit in fruits if fruit.startswith(('a', 'b'))]
            # using startswith() to check if each string starts with 'a' or 'b'
print(fruits_ab)


# Question 5: Beginning with the list below, write a single list comprehension that turns it into
# the following list: [26, 22, 18, 14, 10, 6]
start_list = [3, 5, 7, 9, 11, 13]

# making a new list: multiplying each element in the list by 2
new_list = [i * 2 for i in reversed(start_list)] # iterating over the reverse of start_list
print(new_list)


# Question 6: Beginning with the two lists below, write a single dictionary comprehension that
# turns them into the following dictionary: {'IL':'Illinois', 'IN':'Indiana', 'MI':'Michigan', 'OH':'Ohio'}
short_names = ['IL', 'IN', 'MI', 'OH']
long_names  = ['Illinois', 'Indiana', 'Michigan', 'Ohio']

# creating the dictionary comprehension
names_dict = {key:value for key, value in zip(short_names, long_names)} # using zip() to put the two lists together
print(names_dict)


