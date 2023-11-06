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