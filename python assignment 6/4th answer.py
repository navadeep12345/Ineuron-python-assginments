#Write a python script to print greater between two numbers. Print number only once even if the numbers are the same.
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
if(a>b):
    print(a)
elif(a<b):
    print(b)
elif(a==b):
    print(a)