import sys
import numpy as np
from my_data_frame_dslr import my_data_frame_dslr as mdf
from logistic_regression import logistic_regression
from utils import string_lst_2_categ

def main():
    if len(sys.argv) != 2:
        print("Usage: python train.py dataset_test.csv")
        return
    file_name = sys.argv[1]
    df = mdf(file_name)
    df.fillna_mean()
    x = df.col_2_array([ 'Arithmancy', 'Astronomy', 'Herbology', 'Defense Against the Dark Arts', 'Divination', 'Muggle Studies', 'Ancient Runes', 'History of Magic', 'Transfiguration', 'Potions', 'Care of Magical Creatures', 'Charms', 'Flying'])
    for house in [ 'Slytherin', 'Gryffindor', 'Ravenclaw', 'Hufflepuff']:
        y = np.array(string_lst_2_categ(df.data['Hogwarts House'], house)).reshape(-1,1)
        model = logistic_regression(model_name = house)
        model.train(x,y)
if __name__ == "__main__":
    main()