t = 10
for tc in range(1, t+1):
    dump = int(input())
    num_list = list(map(int, input().split()))
     
    # 덤프가 0이 될때까지 시행
     
    while dump >= 0:
 
        # 최댓값과 최솟값을 찾기 위해
        maxv = -1
        maxidx = -1
        minv = 101
        minidx = 0
         
        for i in range(len(num_list)):
            if num_list[i] >= maxv:
                maxv = num_list[i]
                maxidx = i
            if num_list[i] <= minv:
                minv = num_list[i]
                minidx = i
        # 리스트를 순회하며 큰 수가 나올때마다 max 밸류와 인덱스 초기화
        # 리스트를 순회하며 작은 수가 나올때마다 max 밸류와 인덱스 초기화
 
        num_list[maxidx] -= 1
        num_list[minidx] += 1
 
        # 순회가 끝난 후 최대값에서 1을 빼고 최소값에 1을 더함
 
        dump -= 1
         
        # 덤프 1회 실행했으므로 덤프 1 차감
 
 
    print(f'#{tc} {maxv - minv}')