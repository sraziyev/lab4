import math

p=math.pi


g=int(input("Input degree: "))
a=(g*p)/180
print(a)

h=int(input("Height: "))
a=int(input("Base 1: "))
b=int(input("Base 2: "))
area=(a+b)*h*0.5
print("Area of trapezoid: ",area)

n=int(input("Input number of sides: "))
s=int(input("Input the length of a side: "))
tg=math.tan(p/n)
print(tg)
apth=s/(2*tg)
print(apth)
area=0.5*n*s*apth
print("Area of ", n ,"-sided polygon is ", area)

a=int(input("Length of a base: "))
h=int(input("Height: "))
areap=a*h
print("Area of a parallelogram: ", areap)