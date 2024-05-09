import numpy as np

array1 = np.array([[1,2,3], [4,5,6]])
array2 = np.array([2,4,6])

result = array1 * array2

print("Массив array1:")
print(array1)
print("\nМассив array2:")
print(array2)
print("\nРезультат умножения:")
print(result)

# Возведение в степень с использованием Broadcasting
result = array1 ** array2

print("Массив array1:")
print(array1)
print("\nМассив array2:")
print(array2)
print("\nРезультат возведения в степень:")
print(result) 

# Деление каждого массива на скаляр
scalar = 2
result_array1 = array1 / scalar
result_array2 = array2 / scalar

print("Массив array1 после деления на скаляр:")
print(result_array1)
print("\nМассив array2 после деления на скаляр:")
print(result_array2)