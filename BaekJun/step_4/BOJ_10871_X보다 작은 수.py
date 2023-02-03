n , x = map(int,input().split())
num = list(map(int,input().split()))
number_of_correct = []
for i in range(0,n) :
    if num[i] < x :
        number_of_correct.append(num[i])

num = ' '.join(str(s) for s in number_of_correct)

print(num)