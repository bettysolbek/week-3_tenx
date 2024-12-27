# scripts/visualizations.py
import matplotlib.pyplot as plt
import seaborn as sns

def plot_trend(data, date_col, value_col):
    plt.figure(figsize=(12, 6))
    sns.lineplot(x=date_col, y=value_col, data=data, marker='o', color='green')
    plt.title(f'Trend of {value_col} Over Time')
    plt.xticks(rotation=45)
    plt.show()

def plot_heatmap(correlation_matrix):
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Heatmap')
    plt.show()
