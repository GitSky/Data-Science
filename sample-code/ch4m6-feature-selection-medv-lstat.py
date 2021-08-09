import pandas as pd
import matplotlib.pyplot as plt


from sklearn.datasets import load_boston
boston_dataset = load_boston()

boston = pd.DataFrame(boston_dataset.data,
                      columns=boston_dataset.feature_names)

boston['MEDV'] = boston_dataset.target

boston.plot(kind = 'scatter',
 	x = 'LSTAT',
	y = 'MEDV',
	figsize = (8,6))

plt.savefig("plot.png")
plt.show()

