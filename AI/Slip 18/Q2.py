import pandas as pd

data = {
    'Name': ['Amit', 'Rahul', 'Priya'],
    'Salary': [20000, 30000, 25000]
}

df = pd.DataFrame(data)

print("Original Records:")
print(df)

print("\nSorted Records:")
print(df.sort_values(by='Salary'))

print("\nSalary above 20000:")
print(df[df['Salary'] > 20000])

df.loc[df['Name'] == 'Amit', 'Salary'] = 28000

print("\nUpdated Records:")
print(df)