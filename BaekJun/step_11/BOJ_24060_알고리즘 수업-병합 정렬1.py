import math

n, T = map(int, input().split())
num_list = list(map(int, input().split()))

cnt = [0]
t = [0]
t[0] = T
rlt_num = [0]

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = math.ceil(len(arr)//2)
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    rlt = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            rlt.append(left[i])
            cnt[0] += 1
            if cnt[0] == t[0]:
                rlt_num[0] = left[i]
            i += 1
        else:
            rlt.append(right[j])
            cnt[0] += 1
            if cnt[0] == t[0]:
                rlt_num[0] = right[j]
            j += 1

    for k in range(i, len(left)):
        rlt.append(left[k])
        cnt[0] += 1
        if cnt[0] == t[0]:
            rlt_num[0] = left[k]

    for k in range(j, len(right)):
        rlt.append(right[k])
        cnt[0] += 1
        if cnt[0] == t[0]:
            rlt_num[0] = right[k]

    return rlt


mergeSort(num_list)
if cnt[0] < t[0]:
    rlt_num[0] = -1

print(rlt_num[0])
