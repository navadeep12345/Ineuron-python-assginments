#Write a python script to print greater among three numbers. Print number only once even if the numbers are the same.

a=int(input("Enter 1st Number:"))
b=int(input("Enter 2nd Number:"))
c=int(input("Enter 3rd Number:"))
if(a>b):
    if(a>c):
        print(a," is greater among three")
elif(b>c):
    print(b," is greater among three") 
elif(c>b):
    print(c,"is greater among three")  
elif(a==b or a==c) :
    print(a,"is greater among the three")
elif(b==a or b==c):
    print(b,"is greater among the three")    
elif(c==a or c==b):
    print(c,"is greater among the three")
elif(a==b and b==c and c==a):
    print(a,"is greater among the three")