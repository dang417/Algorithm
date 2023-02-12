def distance(x1, y1, x2, y2):
    return ((x1 - x2)**2) + ((y1 - y2)**2)

t = int(input())

for tc in range(1, t+1):
    
    s_x, s_y, g_x, g_y = map(int, input().split())
    n = int(input())
    cnt = 0
    
    for i in range(n):
        x, y, r = map(int, input().split())
        if distance(s_x, s_y, x, y) < r**2 and distance(g_x, g_y, x, y) > r**2:
            cnt += 1
        if distance(g_x, g_y, x, y) < r**2 and distance(s_x, s_y, x, y) > r**2:
            cnt += 1
        
    print(cnt)