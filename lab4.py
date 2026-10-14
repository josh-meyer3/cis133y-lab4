#*****************************************************************************
# Author:          Josh Meyer 
# Lab:             CIS-133Y Lab4
# Date:            10/13/2026
# Description:     
# Input:           
# Output:          
# Sources:         
#*****************************************************************************
from datetime import datetime
from os import get_terminal_size
#from .file1 import func1, func2
#from .file2 import func2 as f2

# Placeholder function
def test():
    print(datetime.now())
    input()

# Menu Options; the name of the function to display and the app executable
OPTIONS = [
    {"name":"datetime.now","app":test},
    #{"name":"func1","app":func1},
    #{"name":"func2","app":func2},
    #{"name":"f2","app":f2}
]


# Formats a string with whitespace on either side of it to size of the
# width minus 2. Example:
#"                              Title                                        "
# - Josh Meyer
def center_format_string(width, string):
    # Determine the size of whitespace needed on each side
    whitespace = (width - len(string))//2 - 1
    # Generate the formatted string
    display_string = "{spacing}{naming}{spacing}".format(spacing = \
        (" " * whitespace), naming = string)
    # If there is an odd number of characters in the display string, add
    # an extra space to the end
    if len(display_string) != (width - 2):
        display_string += " "
    return display_string


# Formats a string with whitespace on the right side, to left justify the
# the string to the size of the width minus 4. Example:
#"1) Function One                                                          "
# - Josh Meyer
def display_left_formatted_string(width, string):
    # Calculate the remaining white space
    whitespace = (width - len(string) - 4)
    # Display the formatted
    print("* {string}{whitespace} *".format(string = string,\
        whitespace = (" " * whitespace)))


# Display a menu with padding from the top to fill the screen. Example:
# ... extra lines omitted ...
#* 1) Function One                                                           *
#* 2) Function Two                                                           *
#* 3) Function Three                                                         *
#*****************************************************************************
# - Josh Meyer
def display_menu(options, width, height, banner = 0, fill_screen = True):
    if fill_screen:
        # If fill the screen is selected determine the number of extra lines
        # needed, subtracting an extra 3 for the input request and quit option
        whitelines = height - len(options) - banner - 3
        for i in range(0, whitelines):
            # For each extra line, print a bordered blank line
            print("*{spacing}*".format(spacing = (" " * (width - 2))))
    for i in range(0, len(options)):
        # Set the number for selection and the name of the function
        display_left_formatted_string(width,"{num}) {name}".format(\
            num = i + 1, name = OPTIONS[i]["name"]))
    # Add an option for Quit
    display_left_formatted_string(width, "q) Quit Application")
    # Print the bottom border
    print("*" * (width))


# Display a top banner with the title and optional datetime stamp. Example:
#*****************************************************************************
#*                              Title                                        *
#*                     2026-10-13 20:50:19 PM                                *
#*****************************************************************************
# - Josh Meyer
def display_banner(title, width, show_datetime = True):
    # Print top border
    print("*" * (width))
    # Print "*" on either side of the Title while centering it
    #  with whitespace.
    display_string = center_format_string(width, title)
    print("*{string}*".format(string = display_string))
    if show_datetime:
        # Get the current date and time
        current_time = datetime.now()
        # Format current_time to this style: 2026-10-01 12:10:05 PM
        current_time_string = str(current_time.date()) + \
            " " + str(current_time.strftime("%H:%M:%S %p"))
        # Print "*" on either side of the datetime stamp while centering it
        #  with whitespace.
        display_string = center_format_string(width, current_time_string)
        print("*{string}*".format(string = display_string))
    # Print bottom border
    print("*" * (width))
    # Return the number of lines displayed
    if show_datetime:
        return 4
    return 3


# The main program loop presents the name of the application and the current
# time that it was executed. It provides a menu for selecting which 
# computation the user wishes to execute or quit the application.
# - Josh Meyer
def main():
    selected=""
    while selected.lower() != "q":
        # The name of the Application
        app_name = "Application Name Here"
        # Get the dimensions of the screen
        border_length, border_height = get_terminal_size()
        # Display the Welcome Banner
        banner_lines = display_banner(app_name, border_length)
        display_menu(OPTIONS, border_length, border_height, banner_lines)
        # Prompt for a selection from the menu
        selected = input("> ")
        # Validate input is a digit
        if str.isdigit(selected):
            # Validate the digit falls within the number of options
            if int(selected) > 0 and int(selected) < len(OPTIONS) + 1:
                OPTIONS[int(selected) - 1]["app"]()
        print("")

main()