t = int(input())
num = []
for i in range(t):
    num.append(int(input()))
for i in range(len(num)):
    print(sorted(num)[i],end='\n')