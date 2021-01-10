# 8d) : Write a program to multiply two matrices using Python

def matmult(m1,m2): #function for multiplying two matrices
    m3 = [] # the product-to-be matrix
    i = 0 # i, j and k are just for iterations
    j = 0
    k = 0
    sum1 = 0
    m1rows = len(m1)
    m1columns = len(m1[0])
    m2rows = len(m2)
    m2columns = len(m2[0])
    for i in range(m1rows):
        m3.append([])
    for i in range(m1rows):
        for j in range(m2columns):
            for k in range(m2rows):
                sum1+=m1[i][k]*m2[k][j]
            m3[i].append(sum1)
            sum1 = 0
    print("Matrix product - ")
    for row in range(len(m3)):
        for column in range(len(m3[0])):
            print(m3[row][column],end=" ")
        print()
m1rows = int(input("Enter the number of rows of first matrix - "))
m1columns = int(input("Enter the number of columns of first matrix - "))
m2rows = int(input("Enter the number of rows of second matrix - "))
m2columns = int(input("Enter the number of columns of second matrix - "))
if m1columns != m2rows and m2columns != m1rows: 
    print("Matrix multiplication is not possible.")
else:
    m1 = []
    print("Creating first matrix.....")
    for i in range(m1rows):
        m1.append([])
        for j in range(m1columns):
            temp = int(input("Enter element of row {} and column {} - ".format(i+1,j+1)))
            m1[i].append(temp)
    print("First matrix -") #Print first matrix
    for row in range(len(m1)):
        for column in range(len(m1[0])):
            print(m1[row][column],end=" ")
        print()
    m2 = []
    print("Creating second matrix.....") 
    for i in range(m2rows):
        m2.append([])
        for j in range(m2columns):
            temp = int(input("Enter element of row {} and column {} - ".format(i+1,j+1)))
            m2[i].append(temp)
    print("Second matrix -") #Print second matrix
    for row in range(len(m2)):
        for column in range(len(m2[0])):
            print(m2[row][column],end=" ")
        print()
    if m1columns == m2rows:
        matmult(m1,m2)
    elif m2columns == m1rows:
        matmult(m2,m1)



                
    

