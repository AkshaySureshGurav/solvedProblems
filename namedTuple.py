from collections import namedtuple


if __name__=="__main__":
    numberOfStudents = int(input("Number of students "))
    scoresList = []
    for i in range(numberOfStudents):
        data = input().split(' ')
        scoresList.append(data)
    print(scoresList)