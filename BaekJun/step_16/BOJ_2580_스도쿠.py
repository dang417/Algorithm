import sys
sys.stdin = open('input.txt')

sdoku = [list(map(int, input().split())) for _ in range(9)]
while True:
    for i in range(9):
        number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(9):
            if sdoku[i][j]:
                number_list.remove(sdoku[i][j])
        for j in range(9):
            if not sdoku[i][j] and len(number_list) == 1:
                sdoku[i][j] = number_list[0]
                break

    for i in range(9):
        number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(9):
            if sdoku[j][i]:
                number_list.remove(sdoku[j][i])
        for j in range(9):
            if not sdoku[j][i] and len(number_list) == 1:
                sdoku[j][i] = number_list[0]
                break

    for i in range(0, 9, 3):
        for l in range(0, 9, 3):
            number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for j in range(3):
                for k in range(3):
                    if sdoku[j+i][k+l]:
                        number_list.remove(sdoku[j+i][k+l])
            for j in range(3):
                if not number_list:
                    break
                for k in range(3):
                    if not sdoku[j+i][k+l] and len(number_list) == 1:
                        sdoku[j+i][k+l] = number_list[0]
                        break
    for i in range(9):
        if 0 in sdoku[i]:
            continue
        else:
            for i in range(9):
                print(*sdoku[i])
            exit()


