import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv("https://raw.githubusercontent.com/GitSky/Data-Science/main/dataset/iris.csv")

# # build a dict mapping species to an integer code
# inv_name_dict = {'iris-setosa': 0, 'iris-versicolor': 1, 'iris-virginica': 2}
#
# # build integer color code 0/1/2
# colors = [inv_name_dict[item] for item in iris['species']]
#
# # scatter plot
# # plt.style.use('ggplot')
# scatter = plt.scatter(iris['sepal_len'], iris['sepal_wd'], c = colors)
# plt.xlabel('sepal length (cm)')
# plt.ylabel('sepal width (cm)')
#
# # add legend
# plt.legend(handles=scatter.legend_elements()[0], labels = inv_name_dict.keys())
# # plt.savefig("plot.png")
# plt.show()

# iris.drop('id', axis=1, inplace=True)
# pd.plotting.scatter_matrix(iris, diagonal='hist')
# plt.show()
