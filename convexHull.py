import numpy as np

# find the angle between three point (return in degrees)
def findAngle(a, b, c):
    ba = a - b
    bc = c - b

    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angle = np.arccos(cosine_angle)

    return np.degrees(angle)

# find the determinant between three point
# if > 0 then it is left/upper from p1 and p2
# if = 0 then it is in p1 and p2
# if < 0 then it is right/below from p1 and p2
def determinantBetweenPoint(p1, p2, p3):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    x3 = p3[0]
    y3 = p3[1]
    return x1*y2 + x3*y1 + x2*y3 - x3*y2 - x2*y1 - x1*y3

# find the furthest point from  a line (P1, pn) to a point from array S
# if the distance is the same then maximize the angle
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

# recursive convex searcher for S1
def splittedConvexS1(S, P1, Pn):
    if (len(S) == 0):
        # there's no point in S, then P1 and Pn is convexPoint
        convexPoint.append([np.array([P1[0], Pn[0]]), np.array([P1[1], Pn[1]])])

    else:
        # find the max distance between point in S to the line between P1 and Pn
        pointMaxD = pointDistanceMax(S, P1, Pn)

        # define S1 and S2
        S1 = []
        S2 = []
        for i in S:
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

# recursive convex searcher for S2
def splittedConvexS2(S, P1, Pn):
    if (len(S) == 0):
        # there's no point in S, then P1 and Pn is convexPoint
        convexPoint.append([np.array([P1[0], Pn[0]]), np.array([P1[1], Pn[1]])])

    else:
        # find the max distance between point in S to the line between P1 and Pn
        pointMaxD = pointDistanceMax(S, P1, Pn)

        # define S1 and S2
        S1 = []
        S2 = []
        for i in S:
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
    # initialize convexPoint
    global convexPoint
    convexPoint = []

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
    # there's a different between S1 and S2 because of the direction
    # so for now, the recursive will be split into two function
    splittedConvexS1(S1, P1, Pn)
    splittedConvexS2(S2, Pn, P1)
    return convexPoint