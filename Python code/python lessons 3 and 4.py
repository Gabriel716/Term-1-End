#Gabriel Harrison
#9/13
import math
#get name function
def get_name(name_input):

    name=name_input
    name=name.lower()
    name=name.title()
    print("the name you entered was", name)
    input("is this correct yes or no")

print("this is our function")
name=input("What's your name?")
get_name(name)




#ask user for name
    #name=input("What is your name?")

    
      
#display name
    #print("This is your name that you entered", name)


print("This is our function")


def area_circle(radius1):
    PI=3.14159265
#1 get a radius 
    radius= radius1
#2 compute the area
    radius=float(radius)
    area=radius*radius*PI
#3 display information
    print("This is the area of the circle", area)

radiusx=input("what is the radius")
#area_circle(radiusx)    


def pythag_theorem():
    #a^2 +b^2=c^2
    a=float(ap)
    b=float(bp)
    c= a*a+b*b
    c=math.sqrt(c)
    
    print("this is the third side is",c)

#pythag_theorem(3,4)
    
def add_numbers(x,y):
    num1=x
    num2=y
    num3=float(num1) + float(num2)
    print(num1,"this is number 1")
    print(num2,"this is number 2")
    return num3
x=input("enter a number")
y=input("enter a second number")
num4=add_numbers() #num4=num3
print("the sum of your numbers is")
print(num4)


