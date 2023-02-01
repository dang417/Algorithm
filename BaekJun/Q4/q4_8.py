import sys

t = int(input())

score = 0
add_score = 0

for i in range(t) :
    result = sys.stdin.readline()
    for i in range(len(result)) :
        if result[i] == 'O' :
            add_score = add_score + 1
            score = score + add_score
        else :
            add_score = 0
    print(score)
    score = 0
