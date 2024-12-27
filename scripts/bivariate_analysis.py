# scripts/bivariate_analysis.py
import matplotlib.pyplot as plt
import seaborn as sns

def calculate_correlations(data, columns):
    return data[columns].corr()

def scatter_plot(data, x_col, y_col, hue_col=None):
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x=x_col, y=y_col, data=data, hue=hue_col)
    plt.title(f'{x_col} vs. {y_col}')
    plt.show()
