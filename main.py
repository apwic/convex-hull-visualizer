import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display
from scipy.spatial import ConvexHull
from sklearn import datasets
from convexHull import *

# importing data from sklearn
def irisDataSet():
    data = datasets.load_iris()

    df = pd.DataFrame(data.data, columns= data.feature_names)
    df['Target'] = pd.DataFrame(data.target)

    # convexHull
    plt.figure(figsize = (10, 6))
    colors = ['b','r','g']
    plt.title('Petal Width vs Petal Length')
    plt.xlabel(data.feature_names[0])
    plt.ylabel(data.feature_names[1])

    for i in range(len(data.target_names)):
        bucket = df[df['Target'] == i]
        bucket = bucket.iloc[:,[0,1]].values
        # hull = ConvexHull(bucket)
        myHull = convexHull(bucket)

        plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])

        # for simplex in hull.simplices:
        #     plt.plot(bucket[simplex, 0], bucket[simplex, 1], colors[i])

        for j in range(len(myHull)):
            plt.plot(myHull[j][0], myHull[j][1], colors[i])

    plt.legend()
    plt.show()

if __name__ == "__main__":
    irisDataSet()
