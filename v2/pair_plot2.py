import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from my_data_frame_dslr import my_data_frame_dslr as mdf

def main():
    # Load your custom data structure
    df = mdf("dataset/dataset_train.csv")

    # Convert the dictionary data to a pandas DataFrame
    data = pd.DataFrame(df.data)

    # Define the courses
    courses = ['Arithmancy', 'Astronomy', 'Herbology', 'Defense Against the Dark Arts', 'Divination', 
               'Muggle Studies', 'Ancient Runes', 'History of Magic', 'Transfiguration', 'Potions', 
               'Care of Magical Creatures', 'Charms', 'Flying']

    # Ensure that only the relevant columns are considered for the pairplot
    data_for_pairplot = data[courses + ['Hogwarts House']]

    # Define the colors for the Hogwarts Houses
    house_colors = {'Gryffindor': 'red', 'Hufflepuff': 'yellow', 'Ravenclaw': 'blue', 'Slytherin': 'green'}

    # Create a pairplot with the DataFrame data
    pairplot_fig = sns.pairplot(data_for_pairplot, hue='Hogwarts House', palette=house_colors, corner=True)

    # Adjust the layout
    plt.tight_layout()

    # Show the plot
    plt.savefig('v2/charts/pair_plot2.png', bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    main()
