""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
"""

import ui
import data_manager
import common

filename = "customers.csv"
title_list = ["id", "name", "email", "subscribed"]

def start_module():
    table = data_manager.get_table_from_file(filename)
    show_table(table)
    ui.print_menu("Customer Relationship Management (CRM)", common.submenu_options("crm"), "Go back to the main menu")
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
        get_longest_name_id(table)
    elif option == "5":
        get_subscribed_emails(table)
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

def get_longest_name_id(table):
    del table[0]
    id_of_longest_name = ""
    len_of_longest_name = 0
    longest_name = ""
    for line in table:
        if len(line[1]) > len_of_longest_name:
            len_of_longest_name = len(line[1])
            id_of_longest_name = line[0]
            longest_name = line[1]
        elif len(line[1]) == len_of_longest_name:
            if line[1] < longest_name:
                len_of_longest_name = len(line[1])
                id_of_longest_name = line[0]
                longest_name = line[1]

    ui.print_result("The id of the customer with the longest name is '{0}'.".format(id_of_longest_name), "")
    return id_of_longest_name


def get_subscribed_emails(table):
    del table[0]
    subscribed_customers = []

    for line in table:
        if line[3] == "1":
            subscribed_customers.append(";".join(line[1:3]))

    result = ""
    for item in subscribed_customers:
        customer_and_mail = item.split(";")
        result += "{0} - {1}\n".format(customer_and_mail[0], customer_and_mail[1])
        
    ui.print_result(result, "These are the customers that subscribed to the newsletter and their email adresses:")
    return subscribed_customers
