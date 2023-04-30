

if __name__=="__main__":
    number = int(input())
    stamps = []
    for i in range(number):
        stamps.append(input())
    print(len(set(stamps)))