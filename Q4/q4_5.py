import sys

student = []
for i in range(28) :
    student.append(int(input())) #student 에 입력 값 저장
num = list(range(1,31)) #1-30 리스트
for i in range(len(student)) :
    if student[i] in num :
        num.remove(student[i])
print(num[0],num[1])
