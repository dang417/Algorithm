import sys
sys.stdin = open('sample_input.txt')

def RSP(left, right):
    global number
    if number[left] == 1 and number[right] == 3:
        return left

    elif number[left] == 3 and number[right] == 1:
        return right

    elif number[left] == number[right]:
        return left
    else:
        if number[left] < number[right]:
            return right
        else:
            return left

def mergeSort(arr):
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return RSP(arr[0], arr[1])

    if len(arr) % 2:
        mid = len(arr)//2 + 1
    else:
        mid = len(arr)//2

    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    return RSP(left, right)

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    people = list(range(1, n + 1)) # 1 2 3 4 5
    card = list(map(int, input().split())) # 1 2 3 1 3
    number = {} # 선수 등번호 : 그 사람이 들고있는 카드

    for i in range(n):
        number[i+1] = card[i]

    print(f'#{tc}', mergeSort(people))