n, m = map(int,input().split())
matrix_1 = []
matrix_2 = []
rlt = []

for i in range(n):
    num_list1 = list(map(int,input().split()))
    matrix_1.append(num_list1)
for i in range(n):
    num_list2 = list(map(int,input().split()))
    matrix_2.append(num_list2)
for i in range(n):
    for j in range(m):
        matrix_1[i][j] += matrix_2[i][j]
        print(matrix_1[i][j],end = ' ')
    print()
