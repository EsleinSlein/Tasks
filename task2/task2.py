with open('file1.txt') as f1:
    x0, y0, r = map(float, f1.read().replace("\n", " ").split())
with open('file2.txt') as f2:
    for i in f2.readlines():
        x1, y1 = map(float, i.replace("\n", " ").split())
        if (x1 - x0) ** 2 + (y1 - y0) ** 2 == r ** 2:
            point = 1
        elif (x1 - x0) ** 2 + (y1 - y0) ** 2 < r ** 2:
            point = 0
        else:
            point = 2
        print(point)
