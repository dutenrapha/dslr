import seaborn as sns
import matplotlib.pyplot as plt
from my_data_frame_dslr import my_data_frame_dslr as mdf

def main():
    df = mdf("dataset/dataset_train.csv")

    courses = ['Arithmancy', 'Astronomy', 'Herbology', 'Defense Against the Dark Arts', 'Divination', 'Muggle Studies', 'Ancient Runes', 'History of Magic', 'Transfiguration', 'Potions', 'Care of Magical Creatures', 'Charms', 'Flying']

    houses = ['Hufflepuff','Ravenclaw', 'Slytherin', 'Gryffindor']

    n_courses = len(courses)
    n_per_row = 3

    n_rows = n_courses // n_per_row
    if n_courses % n_per_row != 0:
        n_rows += 1

    fig, axes = plt.subplots(nrows=n_rows, ncols=n_per_row, figsize=(15, 15))

    house_colors = {'Gryffindor': 'red', 'Hufflepuff': 'yellow', 'Ravenclaw': 'blue', 'Slytherin': 'green'}

    for i, course in enumerate(courses):
        row = i // n_per_row
        col = i % n_per_row
        
        for j, house in enumerate(houses):

            lst_mask = [ True if value == house else False for value in df.data['Hogwarts House'] ]
            data = [value for value, mask in zip(df.data[course], lst_mask) if mask]
      
            sns.histplot(data=data, ax=axes[row, col], bins=50, color=house_colors[house], label=house)
            
            axes[row, col].set_title(f'{course}')
            axes[row, col].set_xlabel('Score')
            axes[row, col].set_ylabel('Frequency')
            
            axes[row, col].legend(title='House')

    plt.tight_layout()
    fig.savefig(f"v2/charts/histogram.png") 
    plt.show()

if __name__ == "__main__":
    main()