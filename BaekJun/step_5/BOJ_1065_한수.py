
#N 보다 작은 한수의 갯수?
#1~N 까지 반복
#등차수열인지 확인하는 함수를 만들고
#for i in range(1,N+1)의 i 에 대해
#-> 자리수와 그 다다음 자리수의 합 == 그 다음 자리수 * 2

n = int(input())
count = 0
def han(n) :
    result = 0
    num_list = []
    while n != 0 :
        num_list.insert(0, n % 10)
        n = n // 10
    for i in range(len(num_list)-2):
        if len(num_list) == 1 or len(num_list) ==2 :
            result = 1
            return result
        elif num_list[i] + num_list[i+2] != 2*num_list[i+1] :
            result = 0
            return result
    else :
        result = 1
        return result
for i in range(1,n+1) :
    count += han(i)

print(count)



