""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

filename = "items.csv"
title_list = ["id", "month", "day", "year", "type", "amount"]

def start_module():
    table = data_manager.get_table_from_file(filename)
    show_table(table)
    ui.print_menu("Accounting manager", common.submenu_options("accounting"), "Go back to the main menu")
    option = ui.get_inputs(["Please enter a number: "], "")[0]
    if option == "1":
        add(table)
    elif option == "2":
        id_ = ui.get_inputs(["Enter id to remove: "], "")
        remove(table, id_)
    elif option == "3":
        id_ = ui.get_inputs(["Enter id to update: "], "")
        update(table, id_)
    elif option == "4":
        which_year_max(table)
    elif option == "5":
        year = ui.get_inputs(["Enter year: "], "")[0]
        avg_amount(table, year)
    elif option == "0":
        pass


def show_table(table):
    ui.print_table(table, title_list)


def add(table):
    global title_list
    inputs = []
    title_list = [title + ": " for title in title_list]
    id_ = common.generate_random(table)
    inputs.append(id_)
    inputs += ui.get_inputs(title_list[1:], "Please enter the requested information")
    table.append(inputs)
    del table[0]
    data_manager.write_table_to_file(filename, table)
    ui.print_result("Added.\n", "")
    return table


def remove(table, id_):
    for item in table:
        if id_[0] == item[0]:
            table.remove(item)
    del table[0]
    data_manager.write_table_to_file(filename, table)
    ui.print_result("Item removed.\n", "")

    return table


def update(table, id_):
    global title_list
    inputs = []
    title_list = [title + ": " for title in title_list]
    ui.print_result("{0} selected.".format(id_[0]), "")
    inputs.append(id_[0])
    inputs += ui.get_inputs(title_list[1:], "Please enter the requested information to update {0}".format(id_[0]))
    index = 0    
    for item in table:
        if inputs[0] == item[0]:
            table[index] = inputs
        index += 1
    del table[0]
    data_manager.write_table_to_file(filename, table)
    ui.print_result("Info updated.\n", "")

    return table


# special functions:
# ------------------

def which_year_max(table):
    highest_profit_year = 0
    highest_profit = 0
    del table[0]

    years = {line[3] for line in table}
    for year in years:
        in_ = 0
        out = 0
        profit = 0
        for line in table:
            if int(year) == int(line[3]):
                if line[4] == "in":
                    in_ += int(line[5])
                elif line[4] == "out":
                    out += int(line[5])
        profit = in_ - out
        if profit > highest_profit:
            highest_profit = profit
            highest_profit_year = int(year)
    ui.print_result("The highest profit year was {0}".format(highest_profit_year), "")
    return highest_profit_year

def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """

    pass
