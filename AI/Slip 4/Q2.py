import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

for species in iris["species"].unique():
    data = iris[iris["species"] == species]
    plt.scatter(data["sepal_length"], data["sepal_width"],
                label=species)

plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Iris Dataset Scatter Plot")
plt.legend()
plt.show()