import pandas as pd

data = {
    'Name': ['Amit', 'Rahul', 'Priya', 'Sneha'],
    'Salary': [20000, 30000, 25000, 40000],
    'Experience': [2, 5, 1, 4]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

for i in range(len(df)):
    if df.loc[i, 'Experience'] < 3:
        df.loc[i, 'Salary'] *= 1.10
    else:
        df.loc[i, 'Salary'] *= 1.05

df['Salary'] = df['Salary'].astype(int)

print("\nUpdated DataFrame:")
print(df)