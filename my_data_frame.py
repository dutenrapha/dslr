import csv
from utils import all_numeric, convert_to_numbers, calculate_percentile, calculate_standard_deviation

OPERATIONS = ["Count", "Mean", "Std", "Min", "25%", "50%", "75%", "Max"]

class my_data_frame:

    def __init__(self, file_name) -> None:
        self.file_name = file_name
        result = self.csv_read(file_name)
        if 'Error' in result:
           raise Exception(result['Error'])
        else:
            self.columns = result['Columns']
            self.data = result['Data']
  
    def csv_read(self, file_name):
        result = {}

        try:
            with open(file_name, 'r', newline='') as csv_file:
                csv_reader = csv.reader(csv_file)
                columns = next(csv_reader)
                result['Columns'] = columns
                data = {}
                for column in columns:
                    data[column] = []
                for row in csv_reader:
                    for idx, column in enumerate(columns):
                        data[column].append(row[idx])
                for column in columns:
                    data[column] = convert_to_numbers(data[column])
                result['Data'] = data
        
        except FileNotFoundError:
            result['Error'] = f"File '{file_name}' not found."
        except Exception as e:
            result['Error'] = f"An error occurred: {e}"
        return result

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

        for column, metrics in result.items():
            print(f"Column: {column}")
            for metric, value in metrics.items():
                print(f"{metric}: {value:.2f}")
        return(result)

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
                    return calculate_percentile(values, 25)
                elif operation == "50%":
                    return calculate_percentile(values, 50)
                elif operation == "75%":
                    return calculate_percentile(values, 75)
                elif operation == "Max":
                    return max(values)
                else:
                    return None 
            else:
                return None
        else:
            return None
