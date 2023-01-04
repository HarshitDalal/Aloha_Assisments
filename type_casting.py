str_v = '12'

str_to_int = int(str_v)
print(f'String to Int : {type(str_v), str_v} to {type(str_to_int), str_to_int}')

str_to_float = float(str_v)
print(f'String to float : {type(str_v), str_v} to {type(str_to_float), str_to_float}')

print()

int_v = 123
float_v = 45.12

int_to_float = float(int_v)
print(f'Int to Float : {type(int_v), int_v} to {type(int_to_float), int_to_float}')

float_to_int = int(float_v)
print(f'Float to Int : {type(float_v), float_v} to {type(float_to_int), float_to_int}')

print()

int_to_str = str(int_v)
print(f'Int to String : {type(int_v), int_v} to {type(int_to_str), int_to_str}')

float_to_str = str(float_v)
print(f'Float to String : {type(float_v), float_v} to {type(float_to_str), float_to_str}')
