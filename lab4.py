from datetime import datetime
from os import get_terminal_size

# The main program loop presents the name of the application and the current
# time that it was executed. It provides a menu for selecting which 
# computation the user wishes to execute or quit the application.
# - Josh Meyer
def main():
    selected=""
    while selected.lower() != "q":
        # The name of the Application to display
        app_name = "Application Name Here"
        # Set the number of options that will be on display, including quit,
        # to provide enough padding lines to fill the screen
        options = 3
        # Get the current date and time
        current_time = datetime.now()
        # Format current_time to this style: 2026-10-01 12:10:05 PM
        current_time_string = str(current_time.date()) + \
            " " + str(current_time.strftime("%H:%M:%S %p"))
        # Determine which is longer, datetime stamp or the application name
        #  and add some padding
        border_length, border_height = get_terminal_size()
        # Print top border
        print("*" * (border_length))
        # Print "*" on either side of the Application Name while centering it
        #  with whitespace.
        whitespace = (border_length - len(app_name))//2 - 1
        display_string = "{spacing}{naming}{spacing}".format(spacing = \
            (" " * whitespace), naming = app_name)
        # If there is an odd number of characters in the display string, add
        # an extra space to the end
        if len(display_string) != (border_length - 2):
            display_string += " "
        print("*{string}*".format(string = display_string))
        # Print "*" on either side of the datetime stamp while centering it
        #  with whitespace.
        whitespace = (border_length - len(current_time_string))//2 - 1
        display_string = "{spacing}{naming}{spacing}".format(spacing = \
            (" " * whitespace), naming = current_time_string)
        # If there is an odd number of characters in the display string, add
        # an extra space to the end
        if len(display_string) != (border_length - 2):
            display_string += " "
        print("*{string}*".format(string = display_string))
        # Print bottom border
        print("*" * (border_length))
        # 6 because 4 lines have already been display at top and 2 more will
        # be at the bottom
        whitelines = border_height - options - 6
        for i in range(0, whitelines):
            print("*{spacing}*".format(spacing = (" " * (border_length - 2))))
        # Set the number for selection and the name of the function
        display_string = "1) Application 1"
        # Calculate the remaining white space
        whitespace = (border_length - len(display_string) - 4)
        # Display the option
        print("* {string}{whitespace} *".format(string = display_string,\
            whitespace = (" " * whitespace)))
        # Set the number for selection and the name of the function
        display_string = "2) Application 2"
        # Calculate the remaining white space
        whitespace = (border_length - len(display_string) - 4)
        # Display the option
        print("* {string}{whitespace} *".format(string = display_string,\
            whitespace = (" " * whitespace)))
        # Set the character for selection to quit
        display_string = "q) Quit Application"
        # Calculate the remaining white space
        whitespace = (border_length - len(display_string) - 4)
        # Display the option
        print("* {string}{whitespace} *".format(string = display_string,\
            whitespace = (" " * whitespace)))
        # Print the bottom border and then prompt for input
        print("*" * (border_length))
        selected=input("> ")
        # If tree for parsing the user input
        if str.isdigit(selected):
            if int(selected) == 1:
                pass
            if int(selected) == 2:
                pass
        print("")

main()