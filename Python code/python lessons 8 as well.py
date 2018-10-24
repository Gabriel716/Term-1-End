#Gabriel Harrison
#9/27/2018

#age=input("What is your age?")
#if age<"75" or age>"16" and age.isdigit():
    #print("You can drive")
#elif age>"16" and age.isdigit():
    #print("Grow up")
#else:
    #print("Sorry you can not drive")
##num1: input from the user; cast to int
##num2: input from the user; cast to int
##
##check numbers if num1 and num2 are all digits
##if both are digits tell user (compound if)
##if one or the other is a digit tell user
##if neither are digits tell user

num1=input("Enter a number")
num2=input("Enter a second number")

if num1.isdigit() and num2.isdigit():
    print(num1,num2, "You entered two numbers")
elif num1.isdigit() or num2.isdigit():
    print("You entered one number")
else:
    print("You did not enter a number")

     
   
