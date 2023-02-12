for tc in range(1,11):
    matrix = []
    t = int(input())
 
    for i in range(100):
        row = list(map(int, input().split()))
        matrix.append(row)
 
    max_sum = 0
    tmp_sum = 0
 
    for i in range(100):
        for j in range(100):
            tmp_sum += matrix[i][j]
        if max_sum <= tmp_sum:
            max_sum = tmp_sum
        tmp_sum = 0
 
        for j in range(100):
            tmp_sum += matrix[j][i]
        if max_sum <= tmp_sum:
            max_sum = tmp_sum
        tmp_sum = 0
 
        tmp_sum += matrix[i][i]
        if max_sum <= tmp_sum:
            max_sum = tmp_sum
        tmp_sum = 0
 
        tmp_sum += matrix[-i-1][-i-1]
        if max_sum <= tmp_sum:
            max_sum = tmp_sum
        tmp_sum = 0
 
    print(f'#{tc} {max_sum}')