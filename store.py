""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

filename = "games.csv"
title_list = ["id", "title", "manufacturer", "price", "in-stock"]

def start_module():
    table = data_manager.get_table_from_file(filename)
    show_table(table)
    ui.print_menu("Store manager", common.submenu_options("store"), "Go back to the main menu")
    option = ui.get_inputs(["Please enter a number: "], "")[0]
    if option == "1":
        add(table)
    elif option == "2":
        id_ = ui.get_inputs(["Enter the id of the item that you want to remove: "], "")
        remove(table, id_)
    elif option == "3":
        id_ = ui.get_inputs(["Enter the id of the item that you want to update: "], "")
        update(table, id_)
    elif option == "4":
        get_counts_by_manufacturers(table)
    elif option == "5":
        manufacturer = ui.get_inputs(["Manufacturer: "], "")
        get_average_by_manufacturer(table, manufacturer)
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

def get_counts_by_manufacturers(table):
    dict = {}
    del table[0]
    for lines in table:
        if lines[2] in dict:
            dict[lines[2]] += 1
        else:
            dict[lines[2]] = 1
    result = ""
    for manufacturer, count in dict.items():
        result += "{0}: {1} games\n".format(manufacturer, count)

    ui.print_result(result, "Games by manufacturer: ")

    return dict


def get_average_by_manufacturer(table, manufacturer):
    count_games = 0
    stock_amount = 0

    for game in table:
        if manufacturer[0] == game[2]:
            count_games += 1
            stock_amount += int(game[4])
    average = stock_amount / count_games
    result = str(average) + " games"
    ui.print_result(result, "The average amount in stock from {0}".format(manufacturer[0]))
    
    return average
