#Write a python script which takes a three digit number from the user and displays only its first digit.
a=int(input("Enter a three digit number:"))
if (a>=100 and a<=999):
    print(a//100)
else:
    print("Enter only three digit number")