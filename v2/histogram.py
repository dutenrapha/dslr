import sys
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

if __name__ == '__main__' :
    df = pd.read_csv(sys.argv[1])  # Load the data
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    newdf = df.select_dtypes(include=numerics)  # Filter numeric data
    cols = newdf.select_dtypes(include=np.number).columns.tolist()  # Display list of numeric variables in DataFrame
    cols.remove(cols[0])  # Remove index
    houses = ('Ravenclaw', 'Slytherin', 'Gryffindor', 'Hufflepuff')

    sns.set(style="whitegrid")  # Set the style for Seaborn

    # Create subplots for each course
    fig, axes = plt.subplots(nrows=4, ncols=4, figsize=(15, 15))
    fig.subplots_adjust(hspace=1)
    fig.suptitle("Hogwarts Course Score Distribution by House", fontsize=12)

    # Plot histograms for each course using Seaborn
    for i, course in enumerate(cols):
        ax = axes[i // 4][i % 4]
        sns.histplot(data=df, x=course, hue='Hogwarts House', ax=ax, bins=20, kde=True, legend=None)

        ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True, useOffset=False)) # Format the y-axis ticks with a thousand separators and no decimals
        ax.ticklabel_format(style='plain', axis='y')  # Prevent scientific notation
        ax.tick_params(axis='both', which='both', labelsize=8)  # Make tick labels smaller in font size
        ax.set_ylabel('') # Remove y-axis title (label)
        ax.set_xlabel('') # Remove x-axis labels from the bottom subplots
        ax.set_title(course, fontsize=10)  # Add the course name as the title

    # Remove the last row of empty subplots
    plt.delaxes(axes[3][1])
    plt.delaxes(axes[3][2])
    plt.delaxes(axes[3][3])

    fig.legend(labels=houses, bbox_to_anchor=(0.95, 0.2)) # Add a legend to the figure
    fig.set_figwidth(15) # Adjust figure size and layout
    fig.set_figheight(7)
    fig.tight_layout()

    plt.savefig('v2/charts/histogram.png') # Save and display the figure
    
    #plt.show()

    if len(sys.argv) == 2: # Display or pause the plot based on command-line arguments
        plt.show()
    elif len(sys.argv) > 2:
        plt.show(block=False)
        plt.pause(int(sys.argv[2]))
        plt.close()
