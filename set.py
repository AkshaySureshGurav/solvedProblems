def average(array):
    convertedArray = set(array)
    return sum(convertedArray)/len(convertedArray)


if __name__ == '__main__':
    n = int(input())
    arr = [int(x) for x in input().split(" ")][:n]
    result = average(arr)
    print(result)