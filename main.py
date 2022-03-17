# 1. Reverse a string
#   a. Write code that takes a string as input and returns the string reversed
#   b. i.e. “Hello” will be returned as “olleH” 

# problem as I understand it:
# -given a string, reverse the chars so it will print backwards (ex: "Hello" becomes "olleH")
# -going to use len(word) - 1 for starting point in range(starting point, ending point, how to iterate) for loop in function
#  store each char in new string and return new string when done

def string_reversed(the_string):
    resulting_string = ""
    for char in range(len(the_string) - 1, -1, -1): # for loop that starts @ last index and goes to 0 index, iterating by -1
        resulting_string += the_string[char]
    return resulting_string

# 1 test
print(string_reversed("Lunch!"))

# 2. Capitalize letter
#   a. Write code that takes a string as input and capitalize the first letter of each word. 
#       Words will be separated by only one space. i.e. “hello world” should be outputted as “Hello World”

# problem as I understand it:
# write a function that takes in a string and capitalize first letter of each word
# see if string method does it already
# easy -> string.title()

def capitalize_first_letter(the_string):
    return the_string.title()

# 2 test
print(capitalize_first_letter("I strangely am more alert when i code"))

# 3. Compress a string of characters
#   a. For example, an input of "aaabbbbbccccaacccbbbaaabbbaaa" would compress to "3a5b4c2a3c3b3a3b3a"

# Problem as I understand it:
# given a string of characters with possible repetition, compress -> leading count following char
# store in new string, return string
# sorted(string) returns a list of sorted characters

# this version combines all occurances of each character then compresses
def compress_string(the_string):
    char_list = sorted(the_string) #char_list is a list of similar characters grouped together
    char_list.append(" ") # append a space so final set of chars will display
    return_string = ""
    counter = 1
    for index in range(0, len(char_list) - 1, 1):
        if(char_list[index] == char_list[index + 1]): # if current char == next char
            counter += 1 #increment current counter
        else:
            return_string += str(counter) + char_list[index] # if current element != next element, you are at the last occurance, need to add counter and element to return_string
            counter = 1 # reset counter
    return return_string

# 3 test
print(compress_string("fffffffffhhhhhhhhhLLLLLLpppppp"))

def compress_string_basic(the_string):
    the_string += " "
    return_string = ""
    counter = 1
    for index in range(0, len(the_string) - 1, 1):
        if(the_string[index] == the_string[index + 1]):
            counter += 1
        else:
            return_string += str(counter) + the_string[index]
            counter = 1
    return return_string

# 3 test
print(compress_string_basic("jjjjjjjjkkkoooooooojjjjjjtttttrr"))

# 4. BONUS CHALLENGE: Palindrome
#   a. A word, phrase, or sequence that reads the same backward as forward i.e. madam
#   b. Write code that takes a user input and checks to see if it is a Palindrome and reports the result

# Problem as I understand it:
# get user input and check to see if it is a palindrome
# prints true if it is, false otherwise
# incorporate string_reversed

def is_palindrome():
    input_string = input("Please enter a word, phrase, or sequence to determine if it is a Palindrome: ")
    input_string_lower = input_string.lower()
    reversed_string = string_reversed(input_string_lower)
    if(input_string_lower == reversed_string):
        return f"{input_string} is a Palindrome."
    else:
        return f"{input_string} is not a Palindrome"

# 4 test
print(is_palindrome())

# 5. A happy number is a number defined by the following process: starting with any positive integer, replace the number
#  by the sum of the squares of its digits, and repeat the process until the number equals 1. An example of a happy number is 19
# c. Write a method that determines if a number is happy or sad

# Problem as I understand it:
# given a number, determine if it is a happy number
# *recursion has to be a part of the solution*
# positive integer and square its digits then add those numbers, repeat until number == 1 (return true)
# int param
# convert string into list of strings (separate digits so you can access them one at a time)
# square each number after casting to int, add to sum
# sum becomes the new number to test
# if sum ever becomes 1, happy
# if sum ever becomes original number, sad

def happy_number(test_num, original_num): # test_num passed in or calculated inside loop, original_num for comparison
    if(test_num == 1):
        is_happy = f"{original_num} is a happy number!"
        return is_happy
    else:
        number_list = []
        current_sum = 0
        # convert int into a string then a list of strings in order to access each digit
        test_num = str(test_num)
        number_list = sorted(test_num) # number_list = ["", "", "", ...]
        for number in number_list: # for every number in the list (currently of type string)
            number = int(number) ** 2 # convert to int, square it
            current_sum += number # add to current_sum
            if(current_sum == original_num):
                is_sad = f"{original_num} is a sad number!"
                return is_sad
        return happy_number(current_sum, original_num) # recursive call to happy_number with current sum and original_num 

# 5 test
print(happy_number(4, 4)) 

# 6. Prime Numbers
#   a. A prime number is a number that is only divisible by one and itself.
#   b. Write a method that prints out all prime numbers between 1 and 100

# Problem as I understand it:
# write a function that prints all prime numbers between 1-100 inclusively (ask user if)
# probably using % == 0 
# (number % (int 1-9) == 0) means divisible by that num

def prime_numbers(lower_bound, upper_bound):
    user_input = input(f"Do you want to include {lower_bound} and {upper_bound}? (y/n): ")
    user_input = user_input.lower()
    if(user_input == "n"):
        lower_bound = lower_bound + 1
        upper_bound = upper_bound - 1
    print(f"The prime numbers between {lower_bound} and {upper_bound} are: ")
    for number in range(lower_bound, upper_bound + 1): # for every number between lower_bound and upper_bound + 1
        if(number > 1): # 1 can only e divided by itself, not itself AND 1 (ie not a prime number)
            # check to see if number is divisible by (number + 1) -> upper_bound (it's obviously divisible by itself, so no need to check that)
            for i in range(2, number): # for every i between 2 and number (excluding number)
                if(number % i == 0): # number is divisible by i
                    # not a prime, move to next iteration
                    break
            # for else statement -> specifies a block of code to execute when loop is finished
            else: # number not divisible by i
                print(number)
        
# 6 test
prime_numbers(1, 100)

# 7. Fibonacci
#   a. A series of numbers in which each number (Fibonacci number) is the sum of the two preceding numbers. 
#       The simplest is the series 1, 1, 2, 3, 5, 8, etc.
#   b. Write a method that does the Fibonacci sequence starting at 1
#   c. HARDER VERSION: Write a method that does the Fibonacci sequence starting at a number that a user input

# Problem as I understand it:
# next_number = current_number + previous_number
# searched for previous number to get  if N is divided by ((1 + sqrt(5)) / 2) and then rounded, the resultant number will be the previous Fibonacci number.

import math

def fibonacci(): # output 8 numbers in the sequence then , ...
    current_number = int(input("Please enter the number you wish to start the Fibonacci sequence at: "))
    current_number = round(current_number) # input validation
    number_of_iterations = int(input("Please enter how many numbers you wish to see: "))
    number_of_iterations = round(number_of_iterations) # input validation
    previous_number = round(current_number / ((1 + math.sqrt(5)) / 2)) # getting previous number (thanks google!)
    next_number = current_number + previous_number 
    for i in range(number_of_iterations): # print number of times user inputs
        print(current_number)
        next_number = current_number + previous_number # calculate next_number
        previous_number = current_number # current_number will be previous_number in next iteration
        current_number = next_number # next_number will be current_number in next iteration
# 7 test
fibonacci()