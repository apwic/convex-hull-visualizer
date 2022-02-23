import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display
from scipy.spatial import ConvexHull
from sklearn import datasets
from convexHull import *
# import numpy as np
# initialize convexPoint
global convexPoint
convexPoint = []

def findAngle(a, b, c):
    ba = a - b
    bc = c - b

    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angle = np.arccos(cosine_angle)

    return np.degrees(angle)

def determinantBetweenPoint(p1, p2, p3):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    x3 = p3[0]
    y3 = p3[1]
    return x1*y2 + x3*y1 + x2*y3 - x3*y2 - x2*y1 - x1*y3

def pointDistanceMax(S, P1, Pn):
    maxD = 0
    pointMaxD = []
    for i in S:
        d = np.abs(np.cross(Pn-P1, i-P1)/np.linalg.norm(Pn-P1))
        if (d > maxD):
            maxD = d
            pointMaxD = i

        elif (d == maxD):
            # maximize the angle if distance is the same
            dAngle = findAngle(P1,i, Pn)
            maxDAngle = findAngle(P1, pointMaxD, Pn)

            if (dAngle > maxDAngle):
                maxD = d
                pointMaxD = i

    return pointMaxD;

def splittedConvexS1(S, P1, Pn):
    if (len(S) == 0):
        # there's no point in S, then P1 and Pn is convexPoint
        # if ((convexPoint[:] == [P1, P1]).any()):
        convexPoint.append([np.array([P1[0], Pn[0]]), np.array([P1[1], Pn[1]])])

    else:
        # find the max distance between point in S to the line between P1 and Pn
        pointMaxD = pointDistanceMax(S, P1, Pn)

        # define S1 and S2
        S1 = []
        S2 = []
        for i in S:
            # dir1 = determinantBetweenPoint(P1, pointMaxD, i)
            # dir2 = determinantBetweenPoint(pointMaxD, Pn, i)
            # if (dir1 > 0 and dir2 < 0):
            #     S1.append(i)
            # elif (dir1 < 0 and dir2 > 0):
            #     S2.append(i)

            # split to S1 and S2
            # check if point outside of the triangle of P1, pointMaxD, and Pn
            if (pointMaxD[0] > i[0]):
                dir = determinantBetweenPoint(pointMaxD, P1, i)
                if (dir < 0):
                    S1.append(i)
            
            #check if point outside of the triangle of P1, pointMaxD, and Pn
            elif (pointMaxD[0] < i[0]):
                dir = determinantBetweenPoint(Pn, pointMaxD, i)
                if (dir < 0):
                    S2.append(i)

        splittedConvexS1(S1, P1, pointMaxD);
        splittedConvexS1(S2, pointMaxD, Pn);

def splittedConvexS2(S, P1, Pn):
    if (len(S) == 0):
        # there's no point in S, then P1 and Pn is convexPoint
        # if ((convexPoint[:] == [P1, P1]).any()):
        convexPoint.append([np.array([P1[0], Pn[0]]), np.array([P1[1], Pn[1]])])

    else:
        # find the max distance between point in S to the line between P1 and Pn
        pointMaxD = pointDistanceMax(S, P1, Pn)

        # define S1 and S2
        S1 = []
        S2 = []
        for i in S:
            # dir1 = determinantBetweenPoint(P1, pointMaxD, i)
            # dir2 = determinantBetweenPoint(pointMaxD, Pn, i)
            # if (dir1 > 0 and dir2 < 0):
            #     S1.append(i)
            # elif (dir1 < 0 and dir2 > 0):
            #     S2.append(i)

            # split to S1 and S2
            # check if point outside of the triangle of P1, pointMaxD, and Pn
            if (pointMaxD[0] < i[0]):
                dir = determinantBetweenPoint(P1, pointMaxD, i)
                if (dir > 0):
                    S1.append(i)
            
            #check if point outside of the triangle of P1, pointMaxD, and Pn
            elif (pointMaxD[0] > i[0]):
                dir = determinantBetweenPoint(pointMaxD, Pn, i)
                if (dir > 0):
                    S2.append(i)

        splittedConvexS2(S1, P1, pointMaxD);
        splittedConvexS2(S2, pointMaxD, Pn);

def convexHull(listOfPoint):

    # sort array by the absis
    listOfPoint = listOfPoint[listOfPoint[:,1].argsort(kind='mergesort')]
    listOfPoint = listOfPoint[listOfPoint[:,0].argsort(kind='mergesort')]
    # take the minimum of absis as P1
    P1 = listOfPoint[0]
    # take the maximum of absis as Pn
    Pn = listOfPoint[-1]

    # define S1 and S2
    S1 = []
    S2 = []
    # split point by the line of P1 and Pn
    for i in listOfPoint[1:-1]:
        dir = determinantBetweenPoint(Pn, P1, i)
        if (dir < 0):
            S1.append(i)
        elif (dir > 0):
            S2.append(i)

    # divide and conquer for S1 and S2
    splittedConvexS1(S1, P1, Pn)
    splittedConvexS2(S2, Pn, P1)
    return convexPoint

#______________________________________________________________________________________________________________________
if __name__ == "__main__":
    data = datasets.load_iris()

    df = pd.DataFrame(data.data, columns= data.feature_names)
    df['Target'] = pd.DataFrame(data.target)
    df.round(decimals = 1)
    # display(df[:50])
    plt.figure(figsize = (10,6))
    colors = ['b', 'r', 'g']
    plt.title('Petal Width vs Petal Length')
    plt.xlabel(data.feature_names[0])
    plt.ylabel(data.feature_names[1])

    bucket = df[df['Target'] == 0]
    # take all of the point (nested array)
    bucket = bucket.iloc[:, [0, 1]].values
    # print(bucket)
    # use convexhull
    hull = ConvexHull(bucket)
    # print(myHull[:][0])
    print("---------------------------------------------------------------")

    plt.scatter(bucket[:, 0], bucket[:, 1], label = data.target_names[0])

    # hull simplices is meant to take nested array from the method
    for simplex in hull.simplices:
        # plot each point to create a convex hull
        print(bucket[simplex, 0], bucket[simplex, 1])
        # plt.plot(bucket[simplex, 0], bucket[simplex, 1], colors[0])
    print("---------------------------------------------------------------")

    myHull = convexHull(bucket)
    print("---------------------------------------------------------------")
    # plt.plot(myHull[-6][0], myHull[0][0], colors[0])
    for j in range(len(myHull)):
        print(myHull[j][0], myHull[j][1])
        plt.plot(myHull[j][0], myHull[j][1], colors[0])

    plt.show()