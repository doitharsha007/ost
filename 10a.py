# 10a) : Write a program to recursively calculate the sum of natural numbers
#        using Python

def sum_n(numbers_upto_n):
    if len(numbers_upto_n) == 1: # if length of list is 1
        return numbers_upto_n[0]
    else:
        numbers_upto_n[1] += numbers_upto_n[0] # add first two numbers, store
        #result in second element
        return sum_n(numbers_upto_n[1:]) # omit first element
n = int(input("Enter 'n' value to calculate sum of first 'n' natural numbers - "))
numbers_upto_n = list(range(1,n+1))
print("Sum of first",n,"natural numbers -",sum_n(numbers_upto_n))
