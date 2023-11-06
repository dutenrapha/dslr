
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