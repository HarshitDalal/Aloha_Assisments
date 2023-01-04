a, b, c = 12, 15, 17

print(f'a : {a}, b : {b}, c : {c}')

a, *b = 10, 20, 30, 40
print(f'a : {a}, b : {b}')

a = b = c = 100
print(f'a : {a}, b : {b}, c : {c}')

num1, num2 = 20, 40
print(f'Before swap num1 : {num1} & num2 : {num2}')
num1, num2 = num2, num1
print(f'After swap num1 : {num1} & num2 : {num2}')

print()
# Unpacking of Collection
a, b = [1, 2]
print(f'a : {a}, b : {b}')

a, b = {'one': 1, 'two': 2}.items()
print(f'a : {a}, b : {b}')
