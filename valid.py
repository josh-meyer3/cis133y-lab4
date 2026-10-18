#*****************************************************************************
# Author:          Jake Nishikido
# Lab:             CIS-133Y Lab4
# Date:            10/16/2026
# Description:     Provides reusable functions to validate user input.
# Input:           Optional prompt strings and user-entered integers,
#                  real numbers, nonblank strings, and yes/no responses.           
# Output:          Validated int, float, or str return values; displays
#                  error messages when input is invalid.         
# Sources:         Google, W3Schools, Textbook
#*****************************************************************************


def get_integer(prompt="Please enter an integer: "):
    """
    Function to prompt for and return a valid integer.
    :param prompt: string Optional string to use as prompt
    :return: integer Valid integer
    """
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Invalid integer.")


def get_real(prompt="Please enter a real number: "):
    """
    Function to prompt for and return a valid real number
    :param prompt: string Optional string to use as prompt
    :return: float Valid real number
    """
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Invalid number.")


def get_string(prompt="Please enter a string: "):
    """
    Function to prompt for and return a string of characters.
    An empty string is invalid input.
    :param prompt: string Optional string to use as prompt
    :return: string Non-empty string of characters
    """
    while True:
        chars = input(prompt)
        if chars.strip():
            return chars
        else:
            print("Invalid string.")


def get_y_or_n(prompt="Please enter 'y' or 'n': "):
    """
    Function to prompt for and return 'y', 'n', or an empty string.
    'Y', 'N', and all cases of 'yes' and 'no' are accepted.
    An empty string is accepted for debugging purposes.
    :param prompt: string Optional string to use as prompt
    :return: string 'y', 'n', or an empty string
    """
    answer = input(prompt).lower()
    
    while answer not in ("y", "n", "yes", "no", ""):
        print("Invalid response.")
        answer = input(prompt).lower()

    if answer in ("y", "yes"):
        return "y"
    elif answer in ("n", "no"):
        return "n"
    else:
        return ""