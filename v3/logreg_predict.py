import sys
import numpy as np
from my_data_frame_dslr import my_data_frame_dslr as mdf
from logistic_regression import logistic_regression
from utils import predict_house, save_predicted_houses_csv, string_lst_2_categ, calculate_age_from_dates

HOUSES = [ 'Slytherin', 'Gryffindor', 'Ravenclaw', 'Hufflepuff']

def main():
    if len(sys.argv) != 2:
        print("Usage: python logreg_predict.py dataset_test.csv")
        return
    file_name = sys.argv[1]
    df = mdf(file_name)
    df.fillna_mean()
    df.data['age'] = calculate_age_from_dates(df.data['Birthday'],2023)
    df.data['left_hand'] = string_lst_2_categ(df.data['Best Hand'],'left')

    x = df.col_2_array([ 'age', 'left_hand','Arithmancy', 'Astronomy', 'Herbology', 'Defense Against the Dark Arts', 'Divination', 'Muggle Studies', 'Ancient Runes', 'History of Magic', 'Transfiguration', 'Potions', 'Care of Magical Creatures', 'Charms', 'Flying'])
    temp = []
    for house in HOUSES:
      model = logistic_regression(model_name = house)
      temp.append(model.predict_prob(x))
    temp = np.array(temp)
    predicted_houses = predict_house(temp, HOUSES)
    save_predicted_houses_csv(predicted_houses)
    
if __name__ == "__main__":
    main()