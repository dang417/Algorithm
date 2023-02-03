word = input()
num_dict = {
    2 : ['A','B','C'],
    3 : ['D','E','F'],
    4 : ['G','H','I'],
    5 : ['J','K','L'],
    6 : ['M','N','O'],
    7 : ['P','Q','R','S'],
    8 : ['T','U','V'],
    9 : ['W','X','Y','Z'],
}
count = 0
for keys in num_dict:
    for char in word:
         if char in num_dict[keys]:
            count += (keys+1)

print(count)