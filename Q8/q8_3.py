n = int(input())
<<<<<<< HEAD

=======
num = list(map(int,range(2,n+1)))
prime_num = []
for i in range(len(num)):
    while n % num[i] == 0:
        n = int(n / num[i])
        prime_num.append(int(num[i]))
        if n == 1:
            break
for i in range(len(prime_num)):
    print(prime_num[i])
>>>>>>> dd64021c8f4bd4b1ce207e8ad5f1d3a5cdc8c328
