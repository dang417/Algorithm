import sys

n = int(input())

score = list(map(int,sys.stdin.readline().split()))
# new_score =[]

# for i in range(n) :
#     new_score.append(score[i]/max(score)*100
#     )
new_score = [score[i]/max(score)*100 for i in range(n)]
average = 0

for i in range(n) :
    average = average + new_score[i]/n

print(average)