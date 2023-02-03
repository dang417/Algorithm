n = int(input())

members = []

for i in range(n):
    x, y = input().split()
    members.append([x,y])

members.sort(key = lambda x : int(x[0]))
# 입력한 순이 가입한 순서이기 때문에
# 나이순으로만 정렬하면 자동으로 가입한 순으로 정렬도 된다
# 나이를 str인 그대로 정렬하면 11 이 9보다 우선적으로 정렬
# 반드시 int로 형 변환 후 정렬한다

for j in members:
    print(j[0], j[1])