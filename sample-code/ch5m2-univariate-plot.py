import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv("https://raw.githubusercontent.com/GitSky/Data-Science/main/dataset/iris.csv")
iris.drop('id', axis=1, inplace=True)
iris.hist()
# plt.savefig("plot.png")
plt.show()
