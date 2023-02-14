#Write a python script to calculate simple interest

p=int(input("Enter intial principal balance:"))
r=int(input("Enter annual interest rate:"))
t=int(input("Enter time in years:"))
simple_interest=(p*t*r)/100
print(simple_interest)