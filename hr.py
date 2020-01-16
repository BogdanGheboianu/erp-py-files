""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
"""
import ui
import data_manager
import common

filename = "persons.csv"
title_list = ["id", "name", "birth_year"]

def start_module():
    table = data_manager.get_table_from_file(filename)
    show_table(table)
    ui.print_menu("Human resources manager", common.submenu_options("hr"), "Go back to the main menu")
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
        get_oldest_person(table)
    elif option == "5":
        get_persons_closest_to_average(table)
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

def get_oldest_person(table):
    oldest_persons = []
    del table[0]

    years = [int(item[2]) for item in table]
    smallest_year = min(years)
    oldest_persons = [item[1] for item in table if int(item[2]) == smallest_year]

    result = ""
    index = 0
    while index < len(oldest_persons):
        if len(oldest_persons) > 1:
            if index == len(oldest_persons) - 2:
                result += "{0} and ".format(oldest_persons[index])
            elif index == len(oldest_persons) - 1:
                result += "{0}.".format(oldest_persons[index])
            else:
                result += "{0}, ".format(oldest_persons[index])
        elif len(oldest_persons) == 1:
            result = "{0}".format(oldest_persons[index])
        index += 1

    if len(oldest_persons) > 1:
        ui.print_result("The oldest persons are {0}".format(result), "")
    elif len(oldest_persons) == 1:
        ui.print_result("The oldest person is {0}.".format(result), "")

    return oldest_persons


def get_persons_closest_to_average(table):
    del table[0]
    sum_years = 0
    years = [int(item[2]) for item in table]
    for year in years:
        sum_years += year
    avearage_year = round(sum_years / len(years))
   
    smallest_difference = 2020
    closest_persons = []
    repetitions = 2
    while repetitions != 0:
        for item in table:
            if repetitions == 2:
                if abs(int(item[2]) - avearage_year) < smallest_difference:
                    smallest_difference = abs(int(item[2]) - avearage_year)
            elif repetitions == 1:
                if abs(int(item[2]) - avearage_year) == smallest_difference:
                    closest_persons.append(item[1])
        repetitions -= 1

    result = ""
    for person in closest_persons:
        result += "{0}\n".format(person)
    
    ui.print_result(result, "The closest to the average age: ")
    return closest_persons
                
    
