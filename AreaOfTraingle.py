
num1=int(input("Enter the first value of the triangle: "))
num2=int(input("Enter the second value of the triangle: "))
num3=int(input("Enter the third value of the triangle: "))

s=(num1+num2+num3)/2

area=(s*(s-num1)*(s-num2)*(s-num3))**0.5
print("The area of the triangle is:", area)