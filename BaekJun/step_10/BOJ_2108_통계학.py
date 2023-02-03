import sys
import statistics

input = sys.stdin.readline

n = int(input())
num = []
for i in range(n):
    num.append(int(input()))

print(round(statistics.mean(num)))
print(statistics.median(num))
if len(statistics.multimode(sorted(num))) > 1:
    print(statistics.multimode(sorted(num))[1])
else :
    print(statistics.multimode(sorted(num))[0])
print(max(num)-min(num))

