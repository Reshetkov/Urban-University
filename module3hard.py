def summator(x):
    global summa
    if isinstance(x, list):
        for i in x:
            summator(i)

    elif isinstance(x, tuple):
        for i in x:
            summator(i)

    elif isinstance(x, dict):
        for i in x:
            summator(i)
        for i in x:
            summator(x[i])

    elif isinstance(x, set):
        for i in x:
            summator(i)

    elif isinstance(x, str):
        length = len(x)
        summa += length

    elif isinstance(x, int):
        summa += x

summa = 0
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

summator(data_structure)
print(summa)