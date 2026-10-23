import pandas as pd

data = {
    'Name': ['Rahul', 'Amit', 'Sneha', 'Priya'],
    'Age': [22, 20, 24, 21]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("\nDataFrame sorted by Age:")
print(df.sort_values(by='Age', ascending=True))