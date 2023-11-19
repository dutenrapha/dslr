
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

def calculate_variance(values):
    n = len(values)
    mean = sum(values) / n
    squared_deviations = [(x - mean) ** 2 for x in values]
    variance = sum(squared_deviations) / n
    return variance

def calculate_coefficient_of_variation(values):
    mean = sum(values) / len(values)
    std = (sum([(x - mean) ** 2 for x in values]) / len(values)) ** 0.5
    if mean != 0:
        return (std / mean) * 100  # Retorna o coeficiente de variação em porcentagem
    else:
        return None

def calculate_skewness(values):
    n = len(values)
    mean = sum(values) / n
    std = (sum([(x - mean) ** 2 for x in values]) / n) ** 0.5
    skewness = (sum([(x - mean) ** 3 for x in values]) / (n * std ** 3))
    return skewness

def calculate_kurtosis(values):
    n = len(values)
    mean = sum(values) / n
    std = (sum([(x - mean) ** 2 for x in values]) / n) ** 0.5
    kurtosis = (sum([(x - mean) ** 4 for x in values]) / (n * std ** 4)) - 3
    return kurtosis

def calculate_median_absolute_deviation(values):
    median = sorted(values)[len(values) // 2]
    absolute_deviations = [abs(x - median) for x in values]
    mad = sorted(absolute_deviations)[len(absolute_deviations) // 2]
    return mad
