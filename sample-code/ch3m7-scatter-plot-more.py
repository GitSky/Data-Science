import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

presidents_df = pd.read_csv('https://raw.githubusercontent.com/GitSky/Data-Science/main/president_heights_party.csv', index_col='order')
plt.scatter(presidents_df['height'], presidents_df['age'],
   marker='<',
   color='r')
plt.xlabel('height')
plt.ylabel('age')
plt.title('U.S. presidents')
# plt.savefig("plot.png")
plt.show()
