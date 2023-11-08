import seaborn as sns
import matplotlib.pyplot as plt
from itertools import combinations
from my_data_frame import my_data_frame as mdf

def main():
    df = mdf("dataset/dataset_train.csv")

    courses = ['Arithmancy', 'Astronomy', 'Herbology', 'Defense Against the Dark Arts', 'Divination', 'Muggle Studies', 'Ancient Runes', 'History of Magic', 'Transfiguration', 'Potions', 'Care of Magical Creatures', 'Charms', 'Flying']

    house_colors = {'Gryffindor': 'red', 'Hufflepuff': 'yellow', 'Ravenclaw': 'blue', 'Slytherin': 'green'}

    pairs = list(combinations(courses, 2))
    
    figures = []
    graphs_per_figure = 6
    graphs_per_row = 3
    for i, (course1, course2) in enumerate(pairs):
        if i % graphs_per_figure == 0:
            fig, axes = plt.subplots(nrows=2, ncols=graphs_per_row, figsize=(20, 10))
            figures.append(fig)
            ax_flat = axes.flatten()
            fig_index = 0
        sns.scatterplot(x=df.data[course1], y=df.data[course2], hue=df.data['Hogwarts House'], palette=house_colors, ax=ax_flat[fig_index])
        ax_flat[fig_index].set_title(f"{course1} vs {course2}")
        ax_flat[fig_index].set_xlabel(course1)
        ax_flat[fig_index].set_ylabel(course2)
        fig_index += 1
        if i == len(pairs) - 1:
            for j in range(fig_index, graphs_per_figure):
                ax_flat[j].remove()
    for fig in figures:
        fig.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
