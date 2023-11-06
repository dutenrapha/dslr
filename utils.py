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

def calculate_percentile(values, percentile):
        if values:
            sorted_values = sorted(values)
            index = int((percentile / 100) * len(sorted_values))
            return sorted_values[index]
        else:
            return None

def calculate_standard_deviation(values):
    n = len(values)
    if n > 1:
        mean = sum(values) / n
        variance = sum((x - mean) ** 2 for x in values) / (n - 1)
        std_deviation = variance ** 0.5
        return std_deviation
    else:
        return None