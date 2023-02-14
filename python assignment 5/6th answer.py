#Write a python script which takes a three digit number from the user and displays only its middle digit.
a=int(input("Enter a three digit number:"))
if a>=100 and a<=999:
    a=a//10
    a=a%10
    print(a)
else:
    print("Enter a valid three digit number")