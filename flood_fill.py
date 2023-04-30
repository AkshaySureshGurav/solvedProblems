# import random
# a = [[0 for _ in range(3)] for _ in range(3)]
# b = [[random.randint(0, 1) for _ in range(4)] for _ in range(3)]
# c = [[0 for _ in range(7)] for _ in range(4)]
# d = [[0 for _ in range(5)] for _ in range(5)]


def iterateOverPixels(image, sr, sc, newColor, startColor, dimensions):
    
    if image[sr][sc] == startColor:
        if image[sr][sc] is not newColor:
            image[sr][sc] = newColor
            if sc > 0:
                if (image[sr][sc-1] == startColor):
                    iterateOverPixels(image, sr, sc-1, newColor, startColor, dimensions)
            if sr > 0:
                if (image[sr-1][sc] == startColor):
                    iterateOverPixels(image, sr-1, sc, newColor, startColor, dimensions)
            if sr < dimensions[0]:
                if image[sr+1][sc] == startColor:
                    iterateOverPixels(image, sr+1, sc, newColor, startColor, dimensions)
            if sc < dimensions[1]:
                if image[sr][sc+1] == startColor:
                    iterateOverPixels(image, sr, sc+1, newColor, startColor, dimensions)
    return image


def floodFill(image, sr: int, sc: int, color: int):
    startingColor = image[sr][sc]
    # storing the dimensions in computer lang so as to 
    # not do future deductions
    dimensions = [len(image)-1, len(image[0])-1]
    return iterateOverPixels(image, sr, sc, color, startingColor, dimensions)
    
b = [[0,0,0],[0,0,0]]
print(b)
print(floodFill(b, 1, 1, 0))
        