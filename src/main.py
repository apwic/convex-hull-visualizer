import pandas as pd
from sqlalchemy import true
from convexHull import *
from utils import *

colorList = ['b', 'r', 'g', 'c', 'm', 'y', 'k']

if __name__ == "__main__":
    print("1. external file")
    print("2. provided datasets")
    dataType = input("Choose data type (1-2): ")
    dataType = checkInput(dataType, [1, 2])

    if (dataType == 1):
        df, X, Y = inputDataSets()
        df.dropna(inplace=True)
        print(df)
        df['Target'] = df['target']

    else:
        data, X, Y = providedDataSets()
        df = pd.DataFrame(data.data, columns=data.feature_names)
        df['Target'] = pd.DataFrame(data.target)

    try:
        linearSepDataSet(df, X, Y)
    except:
        # generalized convex, only display one convex
        # user can choose color
        print("Cant use categorized convex")
        print("Will take all point to create convex hull\n")
        print("List of colors: ")
        for i in range(len(colorList)):
            print(f"{i+1}. {colorList[i]}")

        color = input(f"Choose a color (1-{len(colorList)}): ")
        color = checkInput(color, colorList)
        color = colorList[color-1]

        showConvexFromTable(df, X, Y, color)
