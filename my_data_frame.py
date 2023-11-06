import csv
from utils import all_numeric, convert_to_numbers

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
        resp = []
        for column in self.columns:
            resp.append(self.my_count(column))
        return(resp)
  
    def my_count(self, column):
        if column in self.data:
            count = sum(1 for item in self.data[column] if item is not None)
            return count
        else:
            return 0
