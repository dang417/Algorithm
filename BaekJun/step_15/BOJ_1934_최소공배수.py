t = int(input())

def gcd_r(a,b) :
    if b == 0 :
        return a
    else :
        return gcd_r(b,a%b)

for tc in range(1, t+1):
    A, B = map(int, input().split())
    lcm = A * B // gcd_r(A, B)
    print(lcm)