# 11b) : Write a program to display powers of 2 using anonymous function using
#        python

number = int(input("Enter a positive integer to be used as a power of 2 - "))
power_of_2 = lambda x : pow(2,x)
print("2 to the power",number,"-",power_of_2(number))
