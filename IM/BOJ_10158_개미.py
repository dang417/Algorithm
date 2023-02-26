import sys
sys.stdin = open('input.txt')

# 오른쪽 아래 45도 방향으로 움직이다가
# 벽을 만나면 오 왼 전환
# 바닥/천장을 만나면 위 아래 전환

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

if ((t - w + p) // w) % 2:
    p = (t - w + p) % w

else:
    p = w - ((t - w + p) % w)

if ((t - h + q) // h) % 2:
    q = (t - h + q) % h

else:
    q = h - ((t - h + q) % h)

print(p, q)