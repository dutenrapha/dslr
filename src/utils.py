import csv
import numpy as np

def all_numeric(lst):
    for item in lst:
        if item != None:
            if not isinstance(item, (int, float)):
                return False
    return True

def convert_to_numbers(str_list):
    converted_list = []
    for item in str_list:
        if item != None:
            try:
                converted_item = int(item)
            except ValueError:
                try:
                    converted_item = float(item)
                except ValueError:
                    converted_item = item

            converted_list.append(converted_item)
        else:
            converted_list.append(None)
    return converted_list

def print_formatted_table(result, OPERATIONS):
    max_column_width = max(len(column) for column in result.keys())
    column_names = [""] + list(result.keys())

    header = "{:<{width}}".format("", width=max_column_width)
    for column in column_names[1:]:
        header += "\t{:<8}".format(column)
    print(header)

    for operation in OPERATIONS:
        row = "{:<{width}}".format(operation, width=max_column_width)
        for column in column_names[1:]:
            value = result[column].get(operation, "")
            row += "\t{:<8.2f}".format(value) if value != "" else "\t"
        print(row)

def string_lst_2_categ(string_lst, categ):
    categ_lst = []
    for string in string_lst:
        if string == categ:
            categ_lst.append(1)
        else:
            categ_lst.append(0)
    return(categ_lst)

def predict_house(temp, HOUSES):
    max_indices = np.argmax(temp, axis=0)
    predicted_houses = [HOUSES[i] for i in max_indices]
    return predicted_houses


def save_predicted_houses_csv(predicted_houses):
    data = list(enumerate(predicted_houses))
    with open('houses.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Index', 'Hogwarts House'])
        writer.writerows(data)


