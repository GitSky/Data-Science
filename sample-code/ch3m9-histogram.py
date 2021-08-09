import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

presidents_df = pd.read_csv('https://raw.githubusercontent.com/GitSky/Data-Science/main/president_heights_party.csv', index_col='order')
# presidents_df['height'].plot(
#     kind ='hist',
#     title = 'height',
#     bins = 5)
plt.hist(presidents_df['height'], bins = 5)
plt.savefig("plot.png")
plt.show()
