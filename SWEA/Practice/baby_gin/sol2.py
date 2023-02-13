import sys

sys.stdin = open('input.txt')

T = int(input())


def check_babygin(numbers):
    # 내가 받은 숫자들이 총 몇번씩 나왔는지 세기 위한 리스트...
    counter = [0 for _ in range(10)]
    # 베이비진 여부 확인을 위한 변수
    is_babygin = 0

    # 전체 순회하며 나온 숫자 카운팅
    for number in numbers:
        counter[number] += 1

    idx = 0
    while idx < len(counter):
        # Triplet 검증
        if counter[idx] >= 3:
            counter[idx] -= 3
            is_babygin += 1
            # continue를 통해 아래 로직을 수행하지 않고 다시 한번 이를 확인
            continue

        # Run 검증
        if idx < len(counter) - 2:
            if counter[idx] and counter[idx + 1] and counter[idx + 2]:
                counter[idx] -= 1
                counter[idx + 1] -= 1
                counter[idx + 2] -= 1
                is_babygin += 1
                # continue를 통해 아래 로직을 수행하지 않고 다시 한번 이를 확인
                continue

        if is_babygin == 2:
            return 1
        # 인덱스 증가
        idx += 1
    return 0

for tc in range(1, T + 1):
    numbers = list(map(int, input()))
    print(numbers)
    result = check_babygin(numbers)  # 디버깅 breakpoint
    print(f"#{tc} {result}")