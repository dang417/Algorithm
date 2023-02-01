
def how_many_people(floor, room_num):
    if floor == 0:
        return list(range(1,room_num+1))
    else :
        floor_n = []
        for i in range(1,room_num+1):
            floor_n.append(sum(how_many_people(floor-1,i)))
        return floor_n
    
t = int(input())
for case in range(t):
    floor = int(input()) #풀어야 하는 리스트의 갯수
    room_num = int(input()) #최대로 출현하는 수

    print(how_many_people(floor, room_num)[-1])



