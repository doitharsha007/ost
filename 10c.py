# 10c) : Write a program to copy the contents from one file to another file

file1 = open("file1.txt","r") # file1 must exist, you can give your own filename
content1 = file1.read()
print("Content from source file -")
print(content1)
print()
file1.close()
file2 = open("file2.txt","w+")
file2.write(content1)
file2.seek(0)
content2 = file2.read()
print("After copying, content from destination file -")
print(content2)
file2.close()
