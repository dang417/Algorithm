import sys

count = int(input())
n = list(map(int,sys.stdin.readline().split()))
#list 로 감싸지 않으면 type이 map으로 지정돼 인덱스 불가
print(min(n),max(n))
