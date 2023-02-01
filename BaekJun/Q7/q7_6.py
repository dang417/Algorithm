t = int(input())

for test in range(t):
    floor = int(input())
    num = int(input())
    f0 = list(range(1,num+1))

    for k in range(floor):
        for n in range(1,num):
            f0[n] += f0[n-1] #1부터 n까지 더하기를 반복하는 방법,,,
    print(f0[-1])
