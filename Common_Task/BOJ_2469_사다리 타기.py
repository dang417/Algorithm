k = int(input())
n = int(input())
rlt = list(input())
raw_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
raw_list = raw_list[:k]
arr = [list(input()) for _ in range(n)]
ans = ''

for i in range(n):
    if arr[i] == ['?'] * (k-1):
        left = arr[:i]
        right = arr[i+1:]
        idx = i
        break

for i in range(idx):
    for j in range(len(left[i])):
        if left[i][j] == '-':
            raw_list[j], raw_list[j+1] = raw_list[j+1], raw_list[j]


for i in range(n-idx-2, -1, -1):
    for j in range(len(right[i])):
        if right[i][j] == '-':
            rlt[j], rlt[j+1] = rlt[j+1], rlt[j]

for i in range(k-2):
    if raw_list[i] == rlt[i]:
        ans += '*'
    elif raw_list[i] == rlt[i+1]:
        ans += '-'
    elif raw_list[i] == rlt[i-1]:
        ans += '*'

if raw_list[-1] == rlt[-1]:
    ans += '*'
else:
    ans += '-'

if len(ans) == k-1:
    print(ans)
else:
    print('x' * (k-1))
