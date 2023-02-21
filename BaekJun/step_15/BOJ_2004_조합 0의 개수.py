n, m = map(int, input().split())

def count_2(n):
    two = 0
    while n != 0:
        n = n // 2
        two += n
    return two

def count_5(n):
    five = 0
    while n != 0:
        n = n//5
        five += n
    return five

print(min(count_2(n) - count_2(n-m) - count_2(m), count_5(n) - count_5(n-m) - count_5(m)))