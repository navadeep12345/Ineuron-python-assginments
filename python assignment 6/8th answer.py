#Write a python script to check whether a given quadratic equation has two real & distinct roots, real & equal roots or imaginary roots
a=float(input("Enter coefficient of x^2:"))
b=float(input("Enter coefficient of x:"))
c=float(input("Enter constant value:"))
disc=(b**2)+(4*(a*c))
if(disc>0):
    print("The quadratic equation has two real & distinct roots.")
elif(disc==0):
    print("The quadratic equation has equal roots.")
elif(disc<0):
    print("The quadratic equation has imaginary roots.")