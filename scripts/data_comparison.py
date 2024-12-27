# scripts/data_comparison.py
import matplotlib.pyplot as plt
import seaborn as sns

def compare_by_category(data, category_col, numerical_col):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=category_col, y=numerical_col, data=data)
    plt.title(f'Comparison of {numerical_col} by {category_col}')
    plt.xticks(rotation=45)
    plt.show()
