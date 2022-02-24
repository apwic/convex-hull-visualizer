import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display
from scipy.spatial import ConvexHull
from sklearn import datasets
from convexHull import *

def showConvexFromTable(data, column1, column2, colors):
    # create dataframe
    df = pd.DataFrame(data.data, columns= data.feature_names)

    # create plot
    plt.title('Convex Searched')
    plt.xlabel(data.feature_names[column1])
    plt.ylabel(data.feature_names[column2])

    # take the value from specified column
    bucket = df.iloc[:, [column1, column2]].values
    # use convexHull from the bucket
    hull = convexHull(bucket)
    # plot all the point to the graph
    plt.scatter(bucket[:, 0], bucket[:, 1], color = colors)

    # plot convexPoint to the graph
    for i in range(len(hull)):
        plt.plot(hull[i][0], hull[i][1], colors)

    plt.legend()
    plt.show()

def irisSepalDataSet():
    data = datasets.load_iris()

    df = pd.DataFrame(data.data, columns= data.feature_names)
    df['Target'] = pd.DataFrame(data.target)

    plt.figure(figsize = (10, 6))
    colors = ['b','r','g']
    plt.title('Sepal Width vs Sepal Length')
    plt.xlabel(data.feature_names[0])
    plt.ylabel(data.feature_names[1])

    for i in range(len(data.target_names)):
        bucket = df[df['Target'] == i]
        bucket = bucket.iloc[:,[0,1]].values
        myHull = convexHull(bucket)

        plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])

        for j in range(len(myHull)):
            plt.plot(myHull[j][0], myHull[j][1], colors[i])

    plt.legend()
    plt.show()

def irisPetalDataSet():
    data = datasets.load_iris()

    df = pd.DataFrame(data.data, columns= data.feature_names)
    df['Target'] = pd.DataFrame(data.target)

    plt.figure(figsize = (10, 6))
    colors = ['b','r','g']
    plt.title('Petal Width vs Petal Length')
    plt.xlabel(data.feature_names[2])
    plt.ylabel(data.feature_names[3])

    for i in range(len(data.target_names)):
        bucket = df[df['Target'] == i]
        bucket = bucket.iloc[:,[2,3]].values
        myHull = convexHull(bucket)

        plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])

        for j in range(len(myHull)):
            plt.plot(myHull[j][0], myHull[j][1], colors[i])

    plt.legend()
    plt.show()

if __name__ == "__main__":
    irisPetalDataSet()
    irisSepalDataSet()
    linerrud = datasets.load_linnerud()
    showConvexFromTable(linerrud, 0, 1, 'b')
    showConvexFromTable(linerrud, 1, 2, 'r')
    showConvexFromTable(linerrud, 0, 2, 'g')
