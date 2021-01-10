n = int(input("Enter a number upto which Fibonacci sequence is to be displayed - "))
if n < 0:
    print("Invalid number.")
elif n == 0:
    print("First Fibonacci number - 0")
else:
    f1 = 0
    f2 = 1
    print("Fibonacci sequence upto",n,"-",f1,f2,end=" ") #One way of printing variables within strings
    while(f1+f2 <= n):
        f3 = f1 + f2
        f1 = f2
        f2 = f3
        print(f3,end=" ")
