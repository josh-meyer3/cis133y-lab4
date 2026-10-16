#*****************************************************************************
# Author:          Josh Meyer 
# Lab:             CIS-133Y Lab4
# Date:            10/16/2026
# Description:     
# Input:           
# Output:          
# Sources:         
#*****************************************************************************
import valid

def addition():
    num = -1
    sum = 0
    print("Add multiple numbers together; specify 0 to stop.")
    while num != 0:
        num = valid.get_integer()
        sum += num
    print("The result is: " + str(sum))
    input("... Press Enter to Continue ...")

def subtraction():
    count = 0
    num = -1
    sum = 0
    print("Subtract multiple numbers from each other; specify 0 to stop.")
    while num != 0:
        num = valid.get_integer()
        if count == 0:
            sum = num
        else:
            sum -= num
        count += 1
    print("The result is: " + str(sum))
    input("... Press Enter to Continue ...")

def multiplication():
    count = 0
    sum = 0
    total = valid.get_integer("Specify the number of integers to prompt for: ")
    while count < total:
        num = valid.get_integer()
        if count == 0:
            sum = num
        else:
            sum *= num
        count += 1
    print("The result is: " + str(sum))
    input("... Press Enter to Continue ...")

def division():
    count = 0
    sum = 0
    total = valid.get_integer("Specify the number of integers to prompt for: ")
    while count < total:
        num = valid.get_integer()
        if num == 0:
            print("Cannot divide by 0...")
            continue
        if count == 0:
            sum = num
        else:
            sum /= num
        count += 1
    print("The result is: " + str(sum))
    input("... Press Enter to Continue ...")