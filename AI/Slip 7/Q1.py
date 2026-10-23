import pandas as pd

df = pd.DataFrame({
    "Name": ["Ravi", "Sana", "Amit"],
    "Department": ["IT", "IT", "HR"],
    "Salary": [60000, 55000, 40000]
})

print(df[(df.Department == "IT") &
         (df.Salary > 50000) &
         (df.Name.str.contains("a", case=False))])