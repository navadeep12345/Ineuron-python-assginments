#Write a python script to check whether a given year is a leap year or not.
year=int(input("Enter the Year:"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("This is Leap Year.")
else:
    print("This is not a Leap Year.")