import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int,input().split()))
new_list = sorted(list(set(num_list)))
# 리스트의 중복을 없애고 이를 정렬하면 index 값이
# 곧 해당하는 수 보다 작은 수의 갯수가 됨

for i in num_list: # 리스트 안에 있는 숫자들에 대해
    # 해당하는 각 인덱스 값을 출력
    print(new_list.index(i), end = ' ')