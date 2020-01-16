""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
"""

import ui
import data_manager
import common

filename = "sales.csv"
title_list = ["id", "title", "price", "month", "day", "year"]

def start_module():
    table = data_manager.get_table_from_file(filename)
    show_table(table)
    ui.print_menu("Sales Manager Menu", common.submenu_options("sales"), "Go back to the main menu")
    while True:
        option = ui.get_inputs(["Please enter a number: "], "")[0]
        if common.check_submenu_option(option) == False:
            ui.print_error_message("Index out of range!\n")
        elif common.check_submenu_option(option) == ValueError:
            ui.print_error_message("Please enter a number!\n")
        else:
            break
    if option == "1":
        add(table)
    elif option == "2":
        while True:
            id_ = ui.get_inputs(["Enter id to remove: "], "")
            if common.check_main_functions_inputs(id_, table) == False:
                ui.print_error_message("'{0}' does not exist in your file!".format(id_[0]))
            else:
                break
        remove(table, id_)
    elif option == "3":
        while True:
            id_ = ui.get_inputs(["Enter id to update: "], "")
            if common.check_main_functions_inputs(id_, table) == False:
                ui.print_error_message("'{0}' does not exist in your file!".format(id_[0]))
            else:
                break
        update(table, id_)
    elif option == "4":
        get_lowest_price_item_id(table)
    elif option == "5":
        inputs = ui.get_inputs(["From date: ", "To date: "], "Enter from date and to date in the format 'month-day-year':")
        from_date = inputs[0].split("-")
        to_date = inputs[1].split("-")
        get_items_sold_between(table, from_date[0], from_date[1], from_date[2], to_date[0], to_date[1], to_date[2])
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
    while True:
        inputs += ui.get_inputs(title_list[1:], "Please enter the requested information!")
        answer = common.check_date(inputs[3], inputs[4], inputs[5])
        if answer != True:
            ui.print_error_message(answer)
        else:
            break
    table.append(inputs)
    del table[0]
    data_manager.write_table_to_file(filename, table)
    ui.print_result("Choose another operation!", "{0} added.".format(inputs))
    return table


def remove(table, id_):
    for item in table:
        if id_[0] == item[0]:
            table.remove(item)
    del table[0]
    data_manager.write_table_to_file(filename, table)
    ui.print_result("Choose another operation!", "Item removed.")

    return table


def update(table, id_):
    global title_list
    inputs = []
    title_list = [title + ": " for title in title_list]
    ui.print_result("{0} selected.".format(id_[0]), "")
    inputs.append(id_[0])
    while True:
        inputs += ui.get_inputs(title_list[1:], "Please enter the requested information!")
        answer = common.check_date(inputs[3], inputs[4], inputs[5])
        if answer != True:
            ui.print_error_message(answer)
        else:
            break
    index = 0    
    for item in table:
        if inputs[0] == item[0]:
            table[index] = inputs
        index += 1
    del table[0]
    data_manager.write_table_to_file(filename, table)

    ui.print_result("Choose another operation!", "Info updated.")
    return table



# special functions:
# ------------------

def get_lowest_price_item_id(table):
    del table[0]
    prices = [int(item[2]) for item in table]
    lowest_price = min(prices)
    
    products_with_lowest_prices = []
    for line in table:
        if int(line[2]) == lowest_price:
            products_with_lowest_prices.append(line[0])

    titles = []
    for product in products_with_lowest_prices:
        for item in table:
            if product == item[0]:
                titles.append(item[1])

    last_alphabetical = ""
    chosen_id = ""
    index = 0
    while index < len(titles):
        if titles[index] > last_alphabetical:
            last_alphabetical = titles[index]
            chosen_id = products_with_lowest_prices[index]
        index += 1
    
    ui.print_result("The product's id sold for the lowest price is {0}.".format(chosen_id), "")
    return chosen_id


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    del table[0]
    filtered_table = []

    for item in table:
        if int(item[5]) >= int(year_from) and int(item[5]) <= int(year_to):
            if int(item[3]) >= int(month_from) and int(item[3]) <= int(month_to):
                if int(item[4]) >= int(day_from):
                    filtered_table.append(item)
    ui.print_result("These are the items sold between your given dates ", "")
    ui.print_table(filtered_table, title_list)
