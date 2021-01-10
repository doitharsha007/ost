# 10b) : Write a program to sort words in alphabetic order using Python

s = input("Enter any number of words, separated by spaces - ")
words_list = [string for string in s.split(" ")] #list comprehension
print("Before sorting alphabetically - "," ".join(words_list)) #printing words
#seperated by space
words_list.sort()
print("After sorting alphabetically - "," ".join(words_list)) #printing words
#seperated by space
