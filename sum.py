array = [i for i in range(1000001)]
dicts = {}

target = 1900000

for i, num in enumerate(array):
    if (target - num) in dicts.keys():
        print([dicts[target - num], i])
        break
    else:
        dicts[num] = i

# print(dicts)
# print(array)