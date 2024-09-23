def is_prime(func):
    def wrapper(*args):
        n = func(*args)
        if n > 1 and all(n%d for d in range(2,n)):
            return (f'Простое\n{n}')
        else:
            return (f'Составное\n{n}')
    return wrapper

@is_prime
def sum_three(*number):
    return sum(number)

result = sum_three(2, 3, 6)
print(result)