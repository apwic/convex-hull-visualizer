import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from convexHull import *
from pathlib import Path

colorList = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'b', 'r', 'g', 'c', 'm', 'y', 'k']

def showConvexFromTable(df, column1, column2, colors):
    """
    generalized convex from any dataset
    """
    # create plot
    plt.figure(num="Convex Hull", figsize=(10, 6))
    plt.title(df.columns[column1] +
              " vs " + df.columns[column2])
    plt.xlabel(df.columns[column1])
    plt.ylabel(df.columns[column2])

    # take the value from specified column
    bucket = df.iloc[:, [column1, column2]].values
    # use convexHull from the bucket
    hull = convexHull(bucket)
    # plot all the point to the graph
    plt.scatter(bucket[:, 0], bucket[:, 1], color=colors)

    # plot convexPoint to the graph
    for i in range(len(hull)):
        plt.plot(hull[i][0], hull[i][1], colors)

    plt.show()

def linearSepDataSet(df, column1, column2):
    """
    use case for linear separability dataset
    """
    # create plot
    plt.figure(num="Convex Hull", figsize=(10, 6))
    colors = colorList
    plt.title(df.columns[column1] +
              " vs " + df.columns[column2])
    plt.xlabel(df.columns[column1])
    plt.ylabel(df.columns[column2])
    target = df.Target.unique()

    for i in range(len(target)):
        bucket = df[df['Target'] == target[i]]
        bucket = bucket.iloc[:, [column1, column2]].values
        # use convex at each target
        myHull = convexHull(bucket)

        # scatter and plot colors
        plt.scatter(bucket[:, 0], bucket[:, 1],
                    label=target[i], color=(colors[i%len(colors)]))

        # plot convex point
        for j in range(len(myHull)):
            plt.plot(myHull[j][0], myHull[j][1], colors[i%len(colors)])

    plt.legend()
    plt.show()

def loadDatasets():
    """
    load datasets from sklearn
    """
    iris = datasets.load_iris()
    wine = datasets.load_wine()
    breastCancer = datasets.load_breast_cancer()
    linerrud = datasets.load_linnerud()
    diabetes = datasets.load_diabetes()
    datasetsArray = [iris, wine, breastCancer, linerrud, diabetes]
    dsName = ["iris", "wine", "breastCancer", "linerrud", "diabetes"]

    return dsName, datasetsArray

def checkInput(var, arr):
    """
    check if input is a number and is in range of array's length
    """
    # check whether the input is a number
    while (not var.isnumeric()):
        var = input(f"Wrong input, choose a number 1-{len(arr)}: ")

    var = int(var)

    # check if the inpunt is correct
    while (var < 1 or var > len(arr)):
        var = int(input(f"Wrong input, number in range 1-{len(arr)}: "))

    return var

def providedDataSets():
    """
    ask user for input from the provided data sets
    """
    # used datasets
    dsName, dsArray = loadDatasets()

    print("List of database: ")
    for i in range(len(dsName)):
        print(f"{i+1}. {dsName[i]}")

    # ask user for database
    dsUsed = input(f"Choose a database (1-{len(dsArray)}): ")
    # validate input
    dsUsed = checkInput(dsUsed, dsArray)

    # ask user for X and Y
    column = dsArray[dsUsed-1].feature_names
    print("List of column: ")
    for i in range(len(column)):
        print(f"{i+1}. {column[i]}")

    X = input(f"Choose a column for X value (1-{len(column)}): ")
    X = checkInput(X, column)
    X -= 1
    Y = input(f"Choose a column for Y value (1-{len(column)}): ")
    Y = checkInput(Y, column)
    Y -= 1

    return dsArray[dsUsed-1], X, Y

def inputDataSets():
    """
    ask user for input from external file
    """
    # get file path and redirect it to test folder
    filePath = input("Input file name: ")
    filePath = str(Path(__file__).resolve().parent) + "/../test/" + filePath

    # check for file
    try:
        df = pd.read_csv(filePath)
    except:
        print("File not found")
        inputDataSets()

    # ask user for X and Y
    column = df.columns
    print("List of column: ")
    for i in range(len(column)-1):
        print(f"{i+1}. {column[i]}")

    X = input(f"Choose a column for X value (1-{len(column)}): ")
    X = checkInput(X, column)
    X -= 1
    Y = input(f"Choose a column for Y value (1-{len(column)}): ")
    Y = checkInput(Y, column)
    Y -= 1

    return df, X, Y
