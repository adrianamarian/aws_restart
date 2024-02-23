"""
Write a program to check if the given number is a palindrome number.

A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers

Expected Output:

original number 121
Yes. given number is palindrome number
"""


number = input("Enter the number:")
init_number = []
for char in number:
    init_number.append(char)

reverse_num = init_number.copy()
reverse_num.reverse()
if init_number== reverse_num:
    print("polindrome")
