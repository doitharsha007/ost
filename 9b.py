# 9b) : Write a program to find maximum element in the list using recursive
#       functions

def maximum(numbers):
    if len(numbers) == 1: #if length of list is 1
        return numbers[0]
    else:
        max1 = numbers[0]
        if max1 > numbers[1]: #if first element > second element
            del numbers[1]
            return maximum(numbers)
        else:                 #otherwise, first element < second element
            return maximum(numbers[1:]) #list slicing, omit first element
s = input("Enter some numbers, separated by space - ")
numbers = [int(i) for i in s.split(" ")] #list comprehension, here integers are
#split using space, and each integer is inserted into the list
print("Maximum of ",numbers,"- ",maximum(numbers))
