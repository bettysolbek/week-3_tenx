# scripts/data_quality.py
def check_missing_values(data):
    return data.isnull().sum()
