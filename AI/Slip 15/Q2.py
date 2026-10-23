import numpy as np

data = np.array([10, 20, 30, 40, 50])

print("Minimum:", np.min(data))
print("Maximum:", np.max(data))
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", round(np.std(data), 2))