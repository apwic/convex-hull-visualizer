from convexHull import *
from utils import *
from random import randint

colorList = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'b', 'r', 'g', 'c', 'm', 'y', 'k']

if __name__ == "__main__":
    # ask for whether using external file or load from provided datasets
    print("1. external file")
    print("2. provided datasets")
    dataType = input("Choose data type (1-2): ")
    dataType = checkInput(dataType, [1, 2])

    if (dataType == 1):
        # datasets from external file
        df, X, Y = inputDataSets()
        # NaN might raise an error in function so it's better to clear dataset
        df.dropna(inplace=True)
        # some datasets might not use integer as their target
        # so it's better to use the original name from dataset
        df['Target'] = df.iloc[:, -1]
    else:
        data, X, Y = providedDataSets()
        df = pd.DataFrame(data.data, columns=data.feature_names)
        try:
            # data with no target might raise an error
            # will be handled using generalized convex
            df['Target'] = pd.DataFrame(data.target)
        except:
            pass

    try:
        # only works if datasets is categorized (have a target)
        linearSepDataSet(df, X, Y)
    except:
        # generalized convex, only display one convex
        # color will be randomized
        plt.clf()
        color = randint(0, len(colorList)-1)
        color = colorList[color]

        print("\nCant use categorized convex")
        print("Will take all point to create convex hull")
        showConvexFromTable(df, X, Y, color)
