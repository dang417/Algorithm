#자리수와 그 다음 자리수의 차 == 그 다음 자리수와 그 다다음 자리수의 차
#-> 자리수와 그 다다음 자리수의 합 == 그 다음 자리수 * 2
#이면 등차수열
#N 보다 작은 한수의 갯수?
#1~N 까지 반복
#등차수열인지 확인하는 함수를 만들고
#for i in range(1,N+1)
n = input()
count = 0
def han(n) :
    num_list = []
    while n != 0 :
        num_list.insert(0, n % 10)
        n = n // 10
    for i in range(len(n)-2) :
        if num_list[i] + num_list[i+2] != num_list[i+1] :
            return False
        
    
    
    return num_list

print(han(123456))



