import sys

def sqDist(p1, p2):
    return ((p2[0]-p1[0])**2) + ((p2[1]-p1[1])**2)

def closest_points(arr):
    v = [0, 0, sys.maxsize]
    for i, j in enumerate(arr):
        for k in arr[i+1:]:
            d = sqDist(j, k)
            if d < v[2]:
                v = (j, k, d)
    return list(v[:2])

if __name__ == '__main__':
    arr = [(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)]
    print(closest_points(arr))
    