""" User Interface (UI) module """


def print_table(table, title_list):
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
    print("\n{0}\n{1}".format(label, result))
    


def print_menu(title, list_options, exit_message):
    print("\n{0}:".format(title))
    option_index = 1
    for option in list_options:
        print("    ({0}) {1}".format(option_index, option))
        option_index += 1
    print("    (0) {0}".format(exit_message))


def get_inputs(list_labels, title):
    print(title)
    inputs = [input(label.title()) for label in list_labels]
    return inputs


def print_error_message(message):
    print("Error: {0}".format(message))
