# scripts/outlier_detection.py
import matplotlib.pyplot as plt
import seaborn as sns

def detect_outliers(data, numerical_columns):
    for column in numerical_columns:
        plt.figure(figsize=(8, 5))
        sns.boxplot(x=data[column], color='purple')
        plt.title(f'Outliers in {column}')
        plt.show()
