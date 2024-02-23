# Ex1 Print the sum of the current number and the previous number
# number1= int(input("Enter a number:"))
# print("The sum of the current number and the previous number is ", number1 + (number1-1 ))

# Ex2 Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.
# print("Printing current and previous number sum in a range(10)")
# for i in range(1,10):
    # print(f"Current number {i} Previous number {i-1} Sum {i+(i-1)}")
    
# Ex3 Write a program to accept a string from the user and display characters that are present at an even index number.
# characters = input("Enter a string:")
# print("Original string is v", characters)
# print("Printing only even index chars")
# for letter in characters:
    # if characters.index(letter)%2 == 0:
        # print(letter)
    
# Ex4 Write a program to remove characters from a string starting from zero up to n and return a new string
# initial_string = "pynative"
# remove_chars = 4
# for letter in initial_string:
    # if initial_string.index(letter) >2 :
        # print(letter, end='')
        
# Ex5 Write a function to return True if the first and last number of a given list is same. If numbers are different then return False
# numbers_x = [10, 20, 30, 40, 10]
# numbers_y = [75, 65, 35, 75, 30]
# def check_numers_in_list(my_list):
    # print(f"Given list: {my_list}")
    # if my_list[0]==my_list[-1]:
        # print("result is True")
    # else:
        # print("result is False")
        
# check_numers_in_list(numbers_y)

# Ex6 Iterate the given list of numbers and print only those numbers which are divisible by 5
# numbers_x = [10, 20, 33,46,55]

# def check_div(my_list):
    # print(f"Given list is {my_list}")
    # print("Divisible by 5 ")
    # for item in my_list:
        # if item%5==0:
            # print(item)
            
# check_div(numbers_x)

# Ex7 Write a program to find how many times substring “Emma” appears in the given string
# str_x = "Emma is good developer. Emma is a writer"
# print(f"Emma appeared {str_x.count('Emma')} times")

# Ex8 Print the following pattern
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

            