import pandas as pd

from sklearn.datasets import load_boston
boston_dataset = load_boston()

boston = pd.DataFrame(boston_dataset.data,
                      columns=boston_dataset.feature_names)

boston['MEDV'] = boston_dataset.target

print(boston[['CHAS', 'RM', 'AGE', 'RAD', 'MEDV']].head())
# print(boston.describe().round(2))
# print(boston['CHAS'].describe().round(2))
# print(boston.describe(include='all'))
