import sys
sys.stdin = open('input.txt')

N, L = map(int, input().split())
traffic_lights = [list(map(int, input().split())) for _ in range(N)]

SK = 0
time = 0
for lights in traffic_lights:
    time += lights[0] - SK
    SK = lights[0]
    if time % (lights[1] + lights[2]) > lights[1]:
        continue
    else:
        time += lights[1] - (time % (lights[1] + lights[2]))

print(time + L - SK)