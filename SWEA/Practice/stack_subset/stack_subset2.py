def powerset(arr, K, result):
    if sum(result) > 10:
        return

    if K == len(arr):
        if sum(result) == 10:
            print(*result)
        return
    # K 는 아무튼 증가하는데,
    # K 번째를 쓴 경우와 안 쓴 경우 둘다 불러옴
    powerset(arr, K+1, result + [arr[K]])
    powerset(arr, K+1, result)

arr = list(range(1, 11))

# 원본 배열, 사용한 원소 수, 총합 리스트(사용할 원소 담을)
powerset(arr, 0, [])
