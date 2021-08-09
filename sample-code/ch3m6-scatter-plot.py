import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

presidents_df = pd.read_csv('https://raw.githubusercontent.com/GitSky/Data-Science/main/president_heights_party.csv', index_col='order')
x = presidents_df['height']
y = presidents_df['age']
plt.scatter(x, y)
# plt.savefig("plot.png")
plt.show()
