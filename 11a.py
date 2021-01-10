# 11a) : Write a program to handle exceptions using Python

#Handling built-in exceptions
while True:
    try:
        x = float(input("Enter dividend - "))
        y = float(input("Enter divisor - "))
        z = x/y
        break
    except ZeroDivisionError: #When divisor is zero
        print("A number cannot be divided by zero. Re-enter the numbers")
    except ValueError: #Raised when you input anything other than a number
        print("Enter a number next time.")
print(z)

#Handling user-defined exceptions
class Error(Exception):
    pass
class UnderAgeError(Error):
    pass
while True:
    try:
        age = float(input("Enter an age - "))
        if age < 18:
            raise UnderAgeError
        else:
            print("Age is above 18.")
            break
    except UnderAgeError:
        print("Under age, please enter a valid age.")




      
    

    
