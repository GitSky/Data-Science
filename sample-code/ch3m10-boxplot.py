import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

presidents_df = pd.read_csv('https://raw.githubusercontent.com/GitSky/Data-Science/main/president_heights_party.csv', index_col='order')
print(presidents_df['height'].describe())
plt.style.use('classic')
presidents_df.boxplot(column='height');
plt.savefig("plot.png")
plt.show()
