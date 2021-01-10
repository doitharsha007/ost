from math import floor # importing 'floor' function from 'math' module
start = int(input("Enter the start of the Armstrong number range - ")) #lower limit
end = int(input("Enter the end of the Armstrong number range - ")) #upper limit
if start > end or start < 0 or end < 0:
    print("Invalid range")
else:
    flag = 0
    print("Armstrong number(s) between",start,"and",end,"- ",end="")
    for i in range(start,end+1):
        temp = i
        sum1 = 0
        while temp != 0:
            remainder = temp % 10
            sum1 = sum1 + pow(remainder,3)
            temp = floor(temp / 10) # truncates to the previous highest integer
        if sum1 == i:
            flag = 1
            print(sum1,end=" ")
    if flag == 0:
        print("zero numbers") # if there's no armstrong number within the specified range



