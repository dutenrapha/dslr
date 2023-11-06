
def all_numeric(lst):
    for item in lst:
        if not isinstance(item, (int, float)):
            return False
    return True

def convert_to_numbers(str_list):
    converted_list = []

    for item in str_list:
        try:
            converted_item = int(item)
        except ValueError:
            try:
                converted_item = float(item)
            except ValueError:
                converted_item = item

        converted_list.append(converted_item)

    return converted_list