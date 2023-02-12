t = int(input())

for tc in range(1, t+1):
    rlt = 0
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    distance = ((x1 - x2) ** 2) + ((y1 - y2) ** 2)
    
    if x1 == x2 and y1 == y2:
        # 동심원이며 반지름이 다를 때
        if r1 != r2:
            rlt = 0
        # 동심원이며 반지름이 0일 때
        elif r1 == r2 == 0:
            rlt = 1
        # 동심원이며 반지름이 같을 때
        else:
            rlt = -1
    # 점 사이의 거리가 반지름의 합보다 클 때
    elif distance > (r1 + r2) ** 2:
        rlt = 0
    # 점 사이의 거리가 반지름의 합과 같을 때
    elif distance == (r1 + r2) ** 2:
        rlt = 1
    # 점 사이의 거리가 반지름의 합보다 작을 때
    else:
        # 작은 원이 큰 원에 내접할 때
        if distance == (r1 - r2) ** 2:
            rlt = 1
        # 작은 원이 큰 원 내부에서 접하지 않을 때
        elif distance < (r1 - r2) ** 2:
            rlt = 0
        # 두 원이 두 점에서 접할 때
        else:
            rlt = 2

    print(rlt)