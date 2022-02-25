zed convex, only display one convex
    # color will be randomized
    color = randint(0, len(colorList)-1)
    color = colorList[color]
    print(color)

    print("\nCant use categorized convex")
    print("Will take all point to create convex hull")
    showConvexFromTable(df, X, Y, color)
