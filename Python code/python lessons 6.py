#Gabriel Harrison
#9/21/2018
#Change sorter

#change 1
def change():
    #1 get input from the user how much change
    raw_change=int(input("How much change do you have? "))
    #2 calculate total for quarters, dimes, nickels, and penies
    quarters=raw_change//25
    whats_left=raw_change % 25
    dimes=whats_left//10
    whats_left=whats_left % 10
    nickles=whats_left//5
    whats_left=whats_left % 5
    penies=whats_left
    #3 display the information back to the user
    print("Quarters:", quarters, "\ndimes:", dimes, "\nnickles:", nickles, "\npenies:", penies)
    
change()

#change 2
def change_two(raw_change):
    #1 get input from the user how much change
    raw_change=raw_change
    #2 calculate total for quarters, dimes, nickels, and penies
    quarters=raw_change//25
    whats_left=raw_change % 25
    dimes=whats_left//10
    whats_left=whats_left % 10
    nickles=whats_left//5
    whats_left=whats_left % 5
    penies=whats_left
    #3 return value
    return quarters, dimes, nickles, penies

raw_change=int(input("How much change do you have?"))
quarters, dimes, nickles, penies= change_two(raw_change)





print("Quarters:", quarters, "\ndimes:", dimes, "\nnickles:", nickles, "\npenies:", penies)
    
    
