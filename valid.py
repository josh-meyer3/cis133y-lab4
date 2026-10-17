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
        except:
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
        except:
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
    Function to prompt for and return 'y' or 'n'.
    'Y', 'N', and all cases of 'yes' and 'no' are accepted.
    :param prompt: string Optional string to use as prompt
    :return: string Non-empty string of characters
    """
    answer = input(prompt).lower()
    while answer != "n" and answer != "y" and answer != "no" and answer != "yes" and answer != "":
        print("Invalid response.")
        answer = input(prompt)
        answer = answer.lower()

    return answer