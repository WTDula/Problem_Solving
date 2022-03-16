# 1. Reverse a string
#   a. Write code that takes a string as input and returns the string reversed
#   b. i.e. “Hello” will be returned as “olleH” 

# code as I understand it:
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

# code as I understand it:
# write a function that takes in a string and capitalize first letter of each word
# if char == " "
# easy -> string.title()
# store new string in result string, return result string

# prove space is a char to check for in for loop
# print(len("this"))
# print(len("this ")) # space is counted as a char

def capitalize_first_letter(the_string):
    return the_string.title()

# test
print(capitalize_first_letter("I strangely am more alert when i code"))

