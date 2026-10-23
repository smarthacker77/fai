import pandas as pd

data = {
    'Name': ['Amit', 'Rahul', 'Priya', 'Sneha'],
    'Salary': [20000, 30000, 25000, 40000],
    'Experience': [2, 6, 4, 8]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

for i in range(len(df)):
    if df.loc[i, 'Experience'] < 5:
        df.loc[i, 'Salary'] *= 1.115
    else:
        df.loc[i, 'Salary'] *= 1.065

print("\nUpdated DataFrame:")
print(df.round(2))