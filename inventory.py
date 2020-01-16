""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

filename = "inventory.csv"
title_list = ["id", "name", "manufacturer", "purchase_year", "durability"]

def start_module():
    table = data_manager.get_table_from_file(filename)
    show_table(table)
    ui.print_menu("Inventory manager", common.submenu_options("inventory"), "Go back to the main menu")
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
        year = ui.get_inputs(["Enter year: "], "")
        get_available_items(table, year)
    elif option == "5":
        get_average_durability_by_manufacturers(table)
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

def get_available_items(table, year):
    current_year = 2019
    specific_products = []
    del table[0]
    for product in table:
        if year[0] == product[3]:
            if current_year - int(product[3]) < int(product[4]):
                specific_products.append(product)
    if len(specific_products) > 0:
        ui.print_table(specific_products, title_list)
    else:
        ui.print_result("All the items from {0} have exceeded their durability.".format(year[0]), "")

    return specific_products
    
    
def get_average_durability_by_manufacturers(table):
    dict = {}
    del table[0]
    manufacturers = [product[2] for product in table]
    for manufacturer in manufacturers:
        count_durabilities = 0
        count_products = 0
        for product in table:
            if manufacturer == product[2]:
                count_durabilities += int(product[4])
                count_products += 1
        dict.update({manufacturer: count_durabilities/count_products})

    result = ""
    for manufacturer, avg in dict.items():
        result += "{0}: {1}\n".format(manufacturer, avg)

    ui.print_result(result, "Average durability times for every manufacturer:")
    return dict



    
    
