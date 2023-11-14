import csv
import numpy as np
from utils import all_numeric, print_formatted_table
from my_math import calculate_percentile, calculate_standard_deviation
from my_data_frame import my_data_frame 

OPERATIONS = ["Count", "Mean", "Std", "Min", "25%", "50%", "75%", "Max"]

class my_data_frame_dslr(my_data_frame):
    
    def my_describe(self):
        result = {}
        for column in self.columns:
            if all_numeric(self.data[column]):
                column_data = {}
                for operation in OPERATIONS:
                    value = self.calculate_metric(column, operation)
                    if value is not None:
                        column_data[operation] = value
                result[column] = column_data

        print_formatted_table(result, OPERATIONS)

        return result

    def calculate_metric(self, column, operation):
        if column in self.data:
            values = [float(item) for item in self.data[column] if item is not None]
            if values:
                if operation == "Count":
                    return len(values)
                if operation == "Mean":
                    return sum(values) / len(values)
                elif operation == "Std":
                    return calculate_standard_deviation(values)
                elif operation == "Min":
                    return min(values)
                elif operation == "25%":
                    return calculate_percentile(values, 0.25)
                elif operation == "50%":
                    return calculate_percentile(values, 0.50)
                elif operation == "75%":
                    return calculate_percentile(values, 0.75)
                elif operation == "Max":
                    return max(values)
                else:
                    return None 
            else:
                return None
        else:
            return None

    def col_2_array(self, columns):
        X = []
        for column in columns:
            if column in self.columns:
                X.append(self.data[column])
        return np.array(X).T