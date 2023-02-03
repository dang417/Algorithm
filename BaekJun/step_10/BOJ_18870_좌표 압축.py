import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int,input().split()))
sorted_num = sorted((set(num_list)))
num_dict = {}

for i in range(len(sorted_num)):
    num_dict[sorted_num[i]] = i
    
for i in num_list:
    print(num_dict[i], end = ' ')

# index 의 시간 복잡도는 O(N), dict 자료형의 key로 value를 찾는 시간 복잡도는 O(1)
# 이기 때문에 index 함수를 활용 하기 보다 dict 자료형을 활용 하는 것이 훨씬 시간 복잡도가 작다
