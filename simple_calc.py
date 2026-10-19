#*****************************************************************************
# Author:          Josh Meyer 
# Lab:             CIS-133Y Lab4
# Date:            10/16/2026
# Description:     A library of simple calculations
# Input:           string: run, integer: total, float: num
# Output:          The results of different calculations.
# Sources:         
#*****************************************************************************
import valid

# The base calculation function that accepts a type of calculation to perform
# and prompts the user for the number of variables and their values to execute
# the desired calculation.
# -Josh Meyer
def _calculation(calc_type):
    # Initialize values
    count = 0
    sum = 0

    # Prompt for the total number of variables
    total = valid.get_integer(
        "Specify the number of values to prompt for (minimum 2):"
        )
    # If the input was less than 2, set it to 2
    if total < 2:
        total = 2

    # Loop through until the total number is reached
    while count < total:
        # Prompt for the value of the variable
        num = valid.get_real()

        # If this is the first variable, simply assign the value
        if count == 0:
            sum = num
        # If the type is "add", add the vaule to sum
        elif calc_type == "add":
            sum += num
        # If the type is "sub", subtract the value from sum
        elif calc_type == "sub":
            sum -= num
        # If the type is "mul", multiply the value with sum
        elif calc_type == "mul":
            sum *= num
        # If the type is "div", divide the value from sum
        elif calc_type == "div":
            # if the value is zero, state that is not allowed and continue
            if num == 0:
                print("Cannot divide by 0...")
                continue
            sum /= num
        # All else, state it is an unknown type and exit the loop
        else:
            print("Unknown type...")
            break

        count += 1

    if type(sum) == float:
        if sum.is_integer():
            sum = int(sum)
    
    print("The result is: " + str(sum))


# The wrapper function for calculating Addition
# -Josh Meyer
def addition():
    run = "y"
    # While run is set to "y" or "yes" run the add calculation and prompt for
    # additional executions
    while run == "y" or run == "yes":
        _calculation("add")
        run = valid.get_y_or_n("Add additional numbers? (y/N): ")

    
# The wrapper function for calculating Subtraction
# -Josh Meyer
def subtraction():
    run = "y"
    # While run is set to "y" or "yes" run the subtract calculation and prompt
    # for additional executions
    while run == "y" or run == "yes":
        _calculation("sub")
        run = valid.get_y_or_n("Subtract additional numbers? (y/N): ")


# The wrapper function for calculating Multiplication
# -Josh Meyer
def multiplication():
    run = "y"
    # While run is set to "y" or "yes" run the multiply calculation and prompt
    # for additional executions
    while run == "y" or run == "yes":
        _calculation("mul")
        run = valid.get_y_or_n("Multiply additional numbers? (y/N): ")


# The wrapper function for calculating Division
# -Josh Meyer
def division():
    run = "y"
    # While run is set to "y" or "yes" run the divide calculation and prompt
    # for additional executions
    while run == "y" or run == "yes":
        _calculation("div")
        run = valid.get_y_or_n("Divide additional numbers? (y/N): ")