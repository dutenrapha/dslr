import sys
from src.my_data_frame_dslr import my_data_frame_dslr as mdf

def main():
    if len(sys.argv) != 2:
        print("Usage: python my_script.py file.csv")
        return
    file_name = sys.argv[1]
    df = mdf(file_name)
    df.my_describe()

if __name__ == "__main__":
    main()