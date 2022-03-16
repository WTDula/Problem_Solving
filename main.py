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
# if char == " "
# easy -> string.title()
# store new string in result string, return result string

def capitalize_first_letter(the_string):
    return the_string.title()

# test
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

# test
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

# test
print(compress_string_basic("jjjjjjjjkkkoooooooojjjjjjtttttrr"))