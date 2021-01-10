# 8c) : Write a program to perform various operations on Tuples and dictionaries      

#Tuples are immutable data structures, which means an element cannot be 
#modified or deleted, but can be added (operation 4).

print("Operations on tuples")
print()

print("1.Creating a tuple") #one
t = (1,2,4,8,16,32)
print("Tuple t =",t)
print()

print("2.Accessing tuple element") #two
print("t[2] =",t[2])
print()

print("3.Concatenating tuples") #three
t2 = (64,128,256)
print("t =",t,"t2 =",t2)
t3 = t + t2
print("t3 = t + t2 =",t3)
print()

print("4.Adding single element") #four
print("Before adding 512, t3 =",t3)
t3 = t3 + (512,)
print("After adding 512, t3 =",t3)
print()

print("5.Repeating a tuple") #five
t4 = ("Hi!",) #Even for a tuple with a single element, trailing comma is compulsory
print("t4 =",t4)
print("t4 repeated 4 times -",(t4*4))
print()

print("6.Deleting a tuple - del <tuple-name>")
del t #You can only delete an entire tuple, not an element
print()

#A dictionary is like an associative array. It stores key-value pairs, where
#values are accessed using keys.

print("Operations on dictionaries -")
print()

print("1.Creating a dictionary") #one
dict1 = {"Name":"XYZ","Age":20,"Cars":['Audi','BMW','Mercedes'],5:"crores"}
print("dict1 =",dict1)
print()
#A key can be a string, a numeric value or a tuple
#A value can be a string, numeric value, a list, or even a dictionary

print("2.Accessing dictionary elements") #two
print("dict1['Name'] =",dict1["Name"])
print("dict1['Cars'][1] =",dict1["Cars"][1])
print("dict1[5] =",dict1[5])
print()

print("3.Appending key-value pair") #three
print("Adding key-value pair \"email\" = \"xyz@gmail.com\" to dict1..")
dict1["email"]="xyz@gmail.com"
print("dict1 =",dict1)
print()

print("4.Updating value of a key") #four
print("Before updating, dict1['Age']=",dict1["Age"]) #same as appending
dict1["Age"]=21
print("After updating, dict1['Age']=",dict1["Age"])
print()

print("5.Deleting a key-value pair")
print("Before deleting dict1['email'] and dict1['Cars'][1],")
print("dict1 =",dict1)
del dict1["email"]
del dict1["Cars"][1] #Deleting a list element
print("After deleting them,")
print("dict1=",dict1)
print()

print("6.Deleting an entire dictionary - del <dictionary-name>")
del dict1
