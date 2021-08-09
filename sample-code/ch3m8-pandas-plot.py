import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

presidents_df = pd.read_csv('https://raw.githubusercontent.com/GitSky/Data-Science/main/president_heights_party.csv', index_col='order')
presidents_df.plot(kind = 'scatter',
  x = 'height',
  y = 'age',
  title = 'U.S. presidents')
plt.savefig("plot.png")
plt.show()
