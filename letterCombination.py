def combinations_as(arraay):
    returnValue = []
    for i in arraay[0]:
        print(i)
        if len(arraay) > 1:
            for j in combinations_as(arraay[1:]):
                returnValue.append(i + j)
        else:
            returnValue.append(i)
    return returnValue

def letterCombinations(digits: str) -> list[str]:
    dailer = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'], 
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    combinations = []
    for chars in digits:
        combinations.append(dailer[chars])

    print(combinations_as(combinations))






letterCombinations("23")