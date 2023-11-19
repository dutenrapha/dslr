import sys
import pandas as pd
import numpy as np

def calc_stat(data):
    n = len(data)
    count = n 
    mean = sum(data) / n
    minimum = data[0]
    for x in data:
        if x < minimum:
            minimum = x
    maximum = data[0]
    for x in data:
        if x > maximum:
            maximum = x
    range = maximum - minimum
    variance = sum((x - mean) ** 2 for x in data) / (n - 1)
    std_dev = variance ** 0.5
    skewness = (sum((x - mean) ** 3 for x in data) / (n * std_dev ** 3))
    kurtosis = (sum((x - mean) ** 4 for x in data) / (n * std_dev ** 4)) - 3
    sorted_data = sorted(data)
    quant25 = sorted_data[int(0.25 * n)]
    quant50 = sorted_data[int(0.5 * n)]
    quant75 = sorted_data[int(0.75 * n)]
    iqr = sorted_data[int(0.75 * n)] - sorted_data[int(0.25 * n)]
    cv = (((sum([(x - mean) ** 2 for x in data]) / len(data)) ** 0.5) / (sum(data) / len(data))) * 100 #Coefficient Variation
    mad = sorted([abs(x - quant50) for x in data])[len([abs(x - quant50) for x in data]) // 2]
    
    return {'Count': count, 'Mean': mean, 'Standard Deviation': std_dev, 'Min': minimum, 'Max': maximum, 'Range': range, 'Variance': variance
            , 'Skewness': skewness, 'Kurtosis': kurtosis, '25th Percentile': quant25, '50th Percentile (Median)': quant50, '75th Percentile': quant75
            ,'IQR': iqr, 'CV': cv, 'MAD':mad}


if __name__ == '__main__' :
    if len(sys.argv) != 2:
        print('NOK\nAbort: You must give a dataset as a parameter.\nE.g. python3 v1/describe.py dataset/dataset_train.csv')
        sys.exit(-1)
        
    df = pd.read_csv(sys.argv[1]) # Load the data
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    newdf = df.select_dtypes(include=numerics) # Filter numeric data
    cols = newdf.select_dtypes(include=np.number).columns.tolist() # Display list of numeric variables in DataFrame
    cols.remove(cols[0]) # Remove index

    df_stats = pd.DataFrame(
        [(calc_stat([value for value in df[column] if pd.notna(value)]) if any(pd.notna(value) for value in df[column]) else None) for column in cols],
        index=cols, columns=['Count', 'Mean', 'Standard Deviation', 'Min', '25th Percentile', '50th Percentile (Median)', '75th Percentile', 'Max', 'Range', 'Variance', 'IQR', 'CV', 'Skewness', 'Kurtosis', 'MAD'])

    pd.set_option('display.colheader_justify', 'center')
    pd.set_option('display.float_format', '{:.2f}'.format)
    print()
    print(df_stats)
