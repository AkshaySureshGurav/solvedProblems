if __name__ == '__main__':
    N = int(input())
    array = []
    for _ in range(N):
        user_input = input().strip(" ").split(" ")
        if len(user_input) > 1:
            if len(user_input) > 2:
                array.insert(int(user_input[1]), int(user_input[2]))
            else:
                if user_input[0] == "append":
                    array.append(int(user_input[1]))
                else:
                    array.remove(int(user_input[1]))
        else: 
            if len(user_input) < 1:
                print("No command given to apply on array")
            elif user_input[0] == "print":
                print(array)
            elif user_input[0] == "sort":
                array.sort()
            elif user_input[0] == "pop":
                array.pop()
            else: 
                array.reverse()
