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

    table.insert(0, title_list)
    item_index = 0
    iterations = 0
    longest_elements = []
    data = "|"
    row_separator = "|"
    elements_lenght = 0

    while iterations < len(table[0]):
        longest_item = 0
        for item in table:
            if len(item[item_index]) > longest_item:
                longest_item = len(item[item_index])
        item_index += 1
        iterations +=1
        longest_elements.append(longest_item)

    for item in table:
        item_index = 0
        row_separator = "|"
        while item_index < len(item):
            column_lenght = longest_elements[item_index] + 4
            data += "{0}|".format(item[item_index].center(column_lenght))
            row_separator += "{0}|".format("-".center(column_lenght, "-"))
            item_index += 1
        
        data += "\n{0}\n|".format(row_separator)

    for element in longest_elements:
        elements_lenght += element

    upper_bar = "/{0}\\".format("-" * (elements_lenght + 4 * len(title_list) + len(title_list) - 1)) 
    lower_bar = "\{0}/".format("-" * (elements_lenght + 4 * len(title_list) + len(title_list) - 1)) 
    
    print(upper_bar)
    print(data)
    print(lower_bar)



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
