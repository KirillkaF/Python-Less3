a = list(input('Введите значения через пробел ').split())
print(max(a, key=lambda x: len(x)))
