
def calculate_percentile(data, percentile):
    if data:
        data.sort()
        index = percentile * (len(data) - 1)
        if isinstance(index, (int)):
            print(index)
            return data[int(index)]
        else:
            lower_index = int(index // 1)
            upper_index = lower_index + 1
            lower_value = data[lower_index]
            upper_value = data[upper_index]
            fraction = index - lower_index
            return lower_value + fraction * (upper_value - lower_value)
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