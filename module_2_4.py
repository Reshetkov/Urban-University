numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
primes.extend(numbers)
for i in numbers:
    if i == 1:
        primes.remove(i)
        continue
    else:
        for j in range(2, i):
            if i % j == 0:
                not_primes.append(i)
                primes.remove(i)
                break
print('Primes: ',  primes)
print('Not primes: ', not_primes)