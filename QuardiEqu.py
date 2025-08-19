import cmath
a=int(input("Enter value of a: "))
print("The number is:", a)
b=int(input("Enter value of b: "))
print("The second number is:", b)
c=int(input("Enter value of c: "))
print("The third number is:", c)
d=b**2-4*a*c

x1=(-b+ cmath.sqrt(d))/(2*a)
x2=(-b- cmath.sqrt(d))/(2*a)
print("The roots of the equation are:", x1, "and", x2)