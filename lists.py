def calc_max(list_in):
    """
    determines the largest value in user input list by initializing max_calc to
    the first value in the list, then comparing each subsequent list value and
    updating max_calc if the value is greater than what is currently in it
    until the end of the list
    :param list_in: user input integer list
    :return max_calc: integer value, maximum value from list
    """
    max_calc = list_in[0]
    for i in range(len(list_in)):
        if list_in[i] > max_calc:
            max_calc = list_in[i]
    return max_calc


def find_max_index(list_in):
    """
    function to find the index of the first occurrence of the maximum value
    :param list_in: a list of values
    :return: the index of the first occurrence of the maximum value
    """
    max_calc = list_in[0]
    max_index = 0
    for i in range(len(list_in)):
        if list_in[i] > max_calc:
            max_calc = list_in[i]
            max_index = i
    return max_index


def calc_min(list_in):
    """
    determines the largest value in user input list by initializing min_calc to
    the first value in the list, then comparing each subsequent list value and
    updating min_calc if the value is less than what is currently in it until
    the end of the list
    :param list_in: user input integer list
    :return min_calc: integer value, minimum value from list
    """
    min_calc = list_in[0]
    for i in range(len(list_in)):
        if list_in[i] < min_calc:
            min_calc = list_in[i]
    return min_calc


def find_min_index(list_in):
    """
    function to find the index of the first occurrence of the minimum value
    :param list_in: a list of values
    :return: the index of the first occurrence of the minimum value
    """
    min_calc = list_in[0]
    min_index = 0
    for i in range(len(list_in)):
        if list_in[i] < min_calc:
            min_calc = list_in[i]
            min_index = i
    return min_index


def calc_sum(list_in):
    """
    calculates sum of user input values by adding each list element to the
    accumulator
    :param list_in: user input integer list
    :return sum_calc: integer value, accumulator, sum of all values in list
    """
    sum_calc = 0
    for i in list_in:
        sum_calc += i
    return sum_calc


def calc_mean(list_in):
    """
    calculates average of user input values by using calc_sum() and dividing
    result by length of input list
    :param list_in: list of values
    :return: integer, average of values
    """
    mean_calc = calc_sum(list_in) / len(list_in)
    return mean_calc


def value_count(list_in, value):
    """
    finds and returns the number of occurrences of value in the list
    :param list_in: a list of values
    :param value: a value to search for in the list
    :return: integer, the number of occurrences of value found in the list
    """
    count = 0
    for item in list_in:
        if item == value:
            count += 1
    return count


def find_value_index(list_in, value):
    """
    finds and returns the index of an input value, returns -1 if not found
    :param list_in: list of values
    :param value: input value
    :return: integer, index of input value, or -1 if not found
    """
    value_index = -1
    for i in range(len(list_in)):
        if value == list_in[i]:
            value_index = i
            return value_index
    return value_index


def is_value(list_in, value):
    """
    searches for input value in a list, returns True if found and False if not
    :param list_in: list of values
    :param value: input value
    :return: bool
    """
    for i in range(len(list_in)):
        if list_in[i] == value:
            return True
    return False