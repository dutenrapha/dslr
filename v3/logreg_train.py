import sys
import numpy as np
from my_data_frame_dslr import my_data_frame_dslr as mdf
from logistic_regression import logistic_regression
from utils import string_lst_2_categ, calculate_age_from_dates
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def main():
    if len(sys.argv) != 2:
        print("Usage: python logreg_train.py dataset_train.csv")
        return
    file_name = sys.argv[1]
    df = mdf(file_name)
    df.fillna_mean()
    df.data['age'] = calculate_age_from_dates(df.data['Birthday'],2023)
    df.data['left_hand'] = string_lst_2_categ(df.data['Best Hand'],'left')

    x = df.col_2_array(['age', 'left_hand','Arithmancy', 'Astronomy', 'Herbology', 'Defense Against the Dark Arts', 'Divination', 'Muggle Studies', 'Ancient Runes', 'History of Magic', 'Transfiguration', 'Potions', 'Care of Magical Creatures', 'Charms', 'Flying'])

    for house in [ 'Slytherin', 'Gryffindor', 'Ravenclaw', 'Hufflepuff']:
        y = np.array(string_lst_2_categ(df.data['Hogwarts House'], house)).reshape(-1,1)
        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
        model = logistic_regression(model_name = house, )
        model.train(X_train,y_train)
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        print(f"Accuracy is {acc}")
if __name__ == "__main__":
    main()