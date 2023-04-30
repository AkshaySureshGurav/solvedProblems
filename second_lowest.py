# test cases
    # test case 1 :    
                # 3
                # Test1
                # 52
                # Test2
                # 53
                # Test3
                # 53

    # test case 2
                # 5
                # Harry
                # 37.21
                # Berry
                # 37.21
                # Tina
                # 37.2
                # Akriti
                # 41
                # Harsh
                # 39

def seocnd_lowest(marks):
    #storing only scores of every student in scores array  
    scores = []
    scores_dict = {}

    for student in marks:
        if student[1] not in scores:
            scores.append(student[1])
        
        if student[1] not in scores_dict.keys():
            scores_dict[student[1]] = [student[0]]
        else:
            scores_dict[student[1]].append(student[0])

    return sorted(scores_dict[sorted(scores)[1]])



if __name__ == '__main__':
    marks = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marks.append([name, score])

    for student in seocnd_lowest(marks):
        print(student)  


