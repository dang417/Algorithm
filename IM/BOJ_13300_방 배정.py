import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())
student = {'b1' : 0, 'g1' : 0,
           'b2' : 0, 'g2' : 0,
           'b3' : 0, 'g3' : 0,
           'b4' : 0, 'g4' : 0,
           'b5' : 0, 'g5' : 0,
           'b6' : 0, 'g6' : 0}

for i in range(n):
    s, y = map(int, input().split())
    student_key = ''
    if s == 0:
        student_key += 'g'
    else:
        student_key += 'b'
    student_key += str(y)
    student[student_key] += 1

rlt = 0
for i in student.values():
    if i:
        if i % k:
            rlt += (i // k) + 1
        elif not i % k:
            rlt += (i // k)
        else:
            rlt += 1
print(rlt)