a = int(input())
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0 :
    print('1')
else :
    print('0')

#print(int(a % 4 == 0 and a % 100 != 0 or a % 400 == 0))
#해도 똑같이 나옴 true = 1 false = 0