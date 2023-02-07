def hanoi(num, start, end):
    if num == 1:
        print(start, end)
        return 
    
    hanoi(num-1, start, 6-(start+end))
    print(start, end)
    hanoi(num-1, 6-(start+end), end)

n = int(input())
print(2**n-1)
hanoi(n, 1, 3)

# 1단은 1,3 으로 옮기면 된다
# 2단은 1단을 2로 옮기고
# 1에 남은 단을 3으로 옮기고
# 1단을 다시 3으로 옮기면 된다
# 이때 이 2와 3이 계속해서 바뀌는데 이를 1+2+3 은 6임을 이용해
# 6-(start+end)로써 정리