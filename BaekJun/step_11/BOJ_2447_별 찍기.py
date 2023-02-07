# ***
# * *
# ***

def star(num):
    if num == 1:
        return '*'
    
    stars = star(num//3)
    star_list = []

    for ele in stars:
        star_list.append(ele*3)
    for ele in stars:
        star_list.append(ele+' '*(num//3)+ele)
    for ele in stars:
        star_list.append(ele*3)
    
    return star_list

n = int(input())
print('\n'.join(star(n)))
    