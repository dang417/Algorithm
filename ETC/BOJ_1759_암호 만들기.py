import sys
sys.stdin = open('input.txt')

def combi(arr, l):
    result = []
    if l > len(arr):
        return result
    if l == 1:
        for i in arr:
            result.append([i])
    elif l > 1:
        for i in range(c - l + 1):
            for j in combi(arr[i + 1:], l - 1):
                result.append([arr[i]] + j)
    return result

l, c = map(int, input().split())
words = sorted(list(input().split()))
rlt = []

for i in combi(words, l):
    aiueo_cnt = 0
    alpha_cnt = 0

    for j in range(l):
        if i[j] in 'aiueo':
            aiueo_cnt += 1
        else:
            alpha_cnt += 1

    if aiueo_cnt >= 1 and alpha_cnt >= 2:
        for j in range(l):
            print(i[j], end='')
        print()