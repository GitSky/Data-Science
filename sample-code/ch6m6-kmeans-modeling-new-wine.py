import pandas as pd
import numpy as np

from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler

data = load_wine()
wine = pd.DataFrame(data.data, columns=data.feature_names)

X = wine[['alcohol', 'total_phenols']]

scale = StandardScaler()
scale.fit(X)
X_scaled = scale.transform(X)


from sklearn.cluster import KMeans
# instantiate the model
kmeans = KMeans(n_clusters=3)
# fit the model
kmeans.fit(X_scaled)
# make predictions
y_pred = kmeans.predict(X_scaled)

X_new = np.array([[13, 2.5]])
X_new_scaled = scale.transform(X_new)

print(X_new_scaled)
print(kmeans.cluster_centers_)
print(kmeans.predict(X_new_scaled))
