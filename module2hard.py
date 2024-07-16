n = int(input('Если Вы хотите спастись, то Вы обратились по адресу. Введите число от 3 до 20: '))
all_numbers = []
result = []
for i in range(1, n):
    all_numbers.append(i)
for i in range(0, n - 1):
    for j in range(i + 1,n - 1):
        if n % (all_numbers[i] + all_numbers[j]) == 0:
            result.append(all_numbers[i])
            result.append(all_numbers[j])
print(result)