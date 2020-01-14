""" User Interface (UI) module """


def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    row_separator = "-"
    corner_1_and_3 = "/"
    corner_2_and_4 = "\\"
    white_space = " "
    max_len_elements = []

    len_table = len(title_list)*2
    index = 0
    
    iterations = 0
    while iterations < len(table):
        max_len_element = 0
        for line in table:
            if index < len(line):
                if len(line[index]) > max_len_element:
                    max_len_element = len(line[index])
                    max_element = line[index]
        max_len_elements.append(max_element)
        len_table += max_len_element
        index += 1
        iterations += 1
    upper_bar_lenght = 0
    
    columns_lenght = []
    print_titles = "|"
    index = 0
    for title in title_list:
        if len(title) < len(max_len_elements[index]):
            upper_bar_lenght += len(max_len_elements[index])
            spaces = len(max_len_elements[index]) + 2
            white_spaces =  (spaces - len(title))/2
            if white_spaces % 2 == 0:
                print_titles += "{0}{1}{0}|".format(white_space*int(white_spaces), title)
            else:
                print_titles += "{0}{1}{2}|".format(white_space*int(white_spaces-0.5), title, white_space*int(white_spaces+0.5))
        elif len(title) >= len(max_len_elements[index]):
            spaces = len(title) + 2
            upper_bar_lenght += len(title)
            print_titles += " {0} |".format(title)
        columns_lenght.append(spaces)
        index += 1

    print_row_separator = "|"
    index = 0
    for title in title_list:
        if len(title) <= len(max_len_elements[index]):
            print_row_separator += "{0}|".format(row_separator * len(max_len_elements[index]) + row_separator * 2)
        elif len(title) > len(max_len_elements[index]):
            print_row_separator += "{0}|".format(row_separator * len(title) + row_separator * 2)
        index += 1
    print("{0}{1}{2}".format(corner_1_and_3, row_separator * upper_bar_lenght + row_separator * (len(title_list)-1) + row_separator * (len(title_list) * 2), corner_2_and_4))
    print(print_titles)
    print(print_row_separator)

    
    print_data = "|"
    column_index = 0
    index = 0
    count = 0
    

    while column_index < len(columns_lenght):
        for line in table:
            column_index = 0
            index = 0
            while index < len(line):
                spaces = columns_lenght[column_index]
                white_spaces = (spaces - len(line[index]))/2
                if white_spaces == 1:
                    print_data += "{0}{1}{2}|".format(white_space*int(white_spaces+0.5), line[index], white_space*int(white_spaces+0.5))
                elif len(line[index]) == 1:
                    print_data += "{0}{1}{0}|".format(white_space*int(white_spaces), line[index])
                elif white_spaces % 2 == 0:
                    print_data += "{0}{1}{0}|".format(white_space*int(white_spaces), line[index])
                elif white_spaces % 2 != 0:
                    print_data += "{0}{1}{2}|".format(white_space*int(white_spaces-0.5), line[index], white_space*int(white_spaces+0.5))
                index += 1
                column_index += 1
            count+=1
            # if count == len(columns_lenght):
            #     print_data += "\n{0}{1}{2}".format(corner_1_and_3, row_separator * upper_bar_lenght + row_separator * (len(title_list)-1) + row_separator * (len(title_list) * 2), corner_2_and_4)
            # else:
            print_data += "\n{0}\n|".format(print_row_separator)

    print(print_data)
    





def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, number, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    print("{0}:".format(title))
    option_index = 1
    for option in list_options:
        print("    ({0}) {1}".format(option_index, option))
        option_index += 1
    print("    (0) {0}".format(exit_message))


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    print(title)
    inputs = [input(label) for label in list_labels]
    return inputs


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    print("Error: {0}".format(message))
