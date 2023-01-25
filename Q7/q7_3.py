import math
#x값 입력, 필요한 리스트, 값들 설정과 근의 공식으로 n 구해서 n 값 대입
x = int(input())
n = math.ceil((((1+8*x)**(1/2))-1)/2)
sum_of_n = int(n*(n-1)/2)
num_list = []
#n번째에 해당하는 분수들을 리스트에 저장
for i in range(0,n):
    if n % 2 == 0:
        num_list.append(f'{i+1}/{n-i}')
    else :
        num_list.append(f'{n-i}/{i+1}')
#x번째가 n번째 리스트에서 몇번째인지 계산해서 출력
print(num_list[x-sum_of_n-1])