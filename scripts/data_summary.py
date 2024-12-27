# scripts/data_summary.py
import pandas as pd

def calculate_descriptive_stats(data, numerical_columns):
    return data[numerical_columns].describe()

def check_data_structure(data):
    return data.dtypes
