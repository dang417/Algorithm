num = []
for i in range(9) :
    num.append(int(input())) 
    #입력되는 정수를 하나씩 리스트에 추가
print(max(num))
print(num.index(max(num))+1)
#num 에서 max(num)이 몇번째 자리인지 + 1 출력