# 방의 갯수는 한 칸 나아갈때마다 6씩 증가
# 6 12 18 24 30 36 42....
#6*i를 더해가며,, 만약 
num = int(input())-1

for i in range(1000000000):
    num -= 6*i
    if num <= 0:
        print(i+1)
        break