import pandas as pd
from sklearn.datasets import load_diabetes

data = load_diabetes()
df = pd.DataFrame(data.data, columns=data.feature_names)

print("First 7 Rows:")
print(df.head(7))

print("Shape of Dataset:", df.shape)