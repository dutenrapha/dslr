import sys
from my_data_frame import my_data_frame as mdf

def main():
    if len(sys.argv) != 2:
        print("Usage: python my_script.py file.csv")
        return
    file_name = sys.argv[1]
    df = mdf(file_name)
    df.my_describe()
if __name__ == "__main__":
    main()
