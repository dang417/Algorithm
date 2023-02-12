n = int(input())
d_dict = {1 : 0, 2 : 0, 3 : 0, 4 : 0}
length = []
height = []

for i in range(6):
    d, l = map(int, input().split())
    d_dict[d] += 1
    if d == 1 or d == 2:
        length.append(l)
    else:
        height.append(l)

small_height = 0
small_length = 0

if d_dict[3] == 2:
    if d_dict[1] == 2:
        for i in range(3):
            if length[i] == max(length) and i != 2:
                small_length = length[i+1]
            elif length[i] == max(length):
                small_length = length[i-2]
        for i in range(3):
            if height[i] == max(height) and i == 0:
                small_height = height[i+2]
            elif height[i] == max(height):
                small_height = height[i-1]

    elif d_dict[2] == 2:
        for i in range(3):
            if length[i] == max(length) and i == 0:
                small_length = length[i+2]
            elif length[i] == max(length):
                small_length = length[i-1]
        for i in range(3):
            if height[i] == max(height) and i != 2:
                small_height = height[i+1]
            elif height[i] == max(length):
                small_height = height[i-2]  

elif d_dict [4] == 2:
    if d_dict[1] == 2:
        for i in range(3):
            if length[i] == max(length) and i == 0:
                small_length = length[i+2]
            elif length[i] == max(length):
                small_length = length[i-1]
        for i in range(3):
            if height[i] == max(height) and i != 2:
                small_height = height[i+1]
            elif height[i] == max(height):
                small_height = height[i-2]        
    elif d_dict[2] == 2:
        for i in range(3):
            if length[i] == max(length) and i != 2:
                small_length = length[i+1]
            elif length[i] == max(length):
                small_length = length[i-2]
        for i in range(3):
            if height[i] == max(height) and i == 0:
                small_height = height[i+2]
            elif height[i] == max(height):
                small_height = height[i-1]

print(((max(length) * max(height)) - (small_length * small_height)) * n)