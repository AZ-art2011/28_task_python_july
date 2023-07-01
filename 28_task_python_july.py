def sum_rec(a, b):
    if a == 0:
        return b
    else:
        return sum_rec(a - 1, b + 1)

a = abs(int(input('Укажите первое число ')))
b = abs(int(input('Введите второе число ')))

print(sum_rec(a, b))