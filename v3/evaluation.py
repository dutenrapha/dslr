import sys
import numpy as np
from sklearn.metrics import accuracy_score
from my_data_frame_dslr import my_data_frame_dslr as mdf

def main():
    if len(sys.argv) != 3:
        print("Usage: python evaluation.py y_pred.csv y_test.csv")
        return
    file_name_1 = sys.argv[1]
    df_pred = mdf(file_name_1)
    file_name_2 = sys.argv[2]
    df_test = mdf(file_name_2)
    acc = accuracy_score(df_test.data['Hogwarts House'], df_pred.data['Hogwarts House'])
    print(f"Accuracy is {acc}")

if __name__ == "__main__":
    main()

