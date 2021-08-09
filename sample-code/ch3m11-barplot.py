import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

presidents_df = pd.read_csv('https://raw.githubusercontent.com/GitSky/Data-Science/main/president_heights_party.csv', index_col='order')
party_cnt = presidents_df['party'].value_counts()
plt.style.use('ggplot')
party_cnt.plot(kind ='bar')

plt.savefig("plot.png")
plt.show()
