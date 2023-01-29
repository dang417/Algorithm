t = int(input())
def prime(num):
    for i in range(2,int(num**(0.5))+1):
        if num % i == 0:
            return False
    return True
prime_num = []
for i in range(10000):
    if prime(i):
        prime_num.append(i)
for test_case in range(t):
    n = int(input())
    rlt = []
    for i in prime_num:
        if i > int(n/2):
            break
        if n - i in prime_num:
            rlt.append((i, n-i))
    if len(rlt) % 2 == 0:
        print(rlt[-1][0],rlt[-1][1])
    else:
        print(rlt[-1][0],rlt[-1][1])