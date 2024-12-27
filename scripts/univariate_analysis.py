# scripts/univariate_analysis.py
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def plot_numerical_distributions(data, numerical_columns):
    sns.set_theme(style="whitegrid")
    for column in numerical_columns:
        if not pd.api.types.is_numeric_dtype(data[column]):
            print(f"Skipping {column} as it is not numeric.")
            continue
        
        plt.figure(figsize=(10, 6))
        sns.kdeplot(data[column], shade=True, color='skyblue', bw_adjust=1.5)
        plt.title(f'Distribution of {column}', fontsize=16, fontweight='bold')
        plt.xlabel(column, fontsize=12)
        plt.ylabel('Density', fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.tight_layout()
        plt.show()

def plot_categorical_distributions(data, categorical_columns):
    sns.set_theme(style="darkgrid")
    for column in categorical_columns:
        plt.figure(figsize=(10, 6))
        sns.countplot(data[column], palette="viridis", order=data[column].value_counts().index)
        plt.title(f'Distribution of {column}', fontsize=16, fontweight='bold')
        plt.xlabel(column, fontsize=12)
        plt.ylabel('Count', fontsize=12)
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.6)
        plt.tight_layout()
        plt.show()
