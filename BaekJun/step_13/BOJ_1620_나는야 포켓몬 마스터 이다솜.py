n, m = map(int, input().split())
pokedex = {}

for i in range(n):
    pokedex[input()] = i+1

pokedex_num = {y : x for x,y in pokedex.items()}

for i in range(m):
    pokemon = input()
    if pokemon.isalpha():
        print(pokedex[pokemon])
    else:
        print(pokedex_num[int(pokemon)])
