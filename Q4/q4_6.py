import sys

a = []

for i in range(10) :
    num = int(sys.stdin.readline()) % 42 
    #num에 입력값을 42로 나눈 나머지 할당
    if num in a :
        pass
    #중복이면 PASS
    else :
        a.append(num)
    #아니면 a에 포함

print(len(a))