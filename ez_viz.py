#self made module for some pre-written code for visualization in matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from math import ceil
##Create a Grid of plots with all scatterplots of a feature and the response
def plot_x_to_y(X, y, size = (11, 11), style = 'bmh', pad = 8, fontsize = "small"):
    ncols = 3
    nrows = ceil(X.columns.size / ncols)
    
    if(type(y) == pd.Series):
        y = pd.DataFrame(y)
    
    with plt.style.context(style):
        f, axes = plt.subplots(nrows = nrows, ncols = ncols)
        f.set_size_inches(size[0], size[1])
        f.set_dpi(100)
        i = 0
        for row in range(nrows):
            for col in range(ncols):
                #print(row, col, i)
                if ((i + 1)  % 2 == 0):
                    color = '#0a80ff'
                else:
                    color = '#ff430a' 
                if (i >= X.columns.size):
                	return     
                axes[row][col].scatter(y = y, x = X.iloc[:, i], s = 4**2, c = color)
                axes[row][col].set_xlabel(X.columns[i], fontsize = fontsize, labelpad = 2)
                axes[row][col].set_ylabel(y.columns[0], fontsize = fontsize, labelpad = 1)
                i += 1
        f.tight_layout(pad=pad)