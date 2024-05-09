'''import numpy as np

arr1 = np.random.randint (1,10, size=(3,3))
arr2 = np.random.randint (1,10, size=(3,3))

result = np.multiply (arr1, arr2)

print (f"Array1:{arr1}")
print (f"Array2:{arr2}")

print (f"\n result {result}")'''

import numpy as np
data = np.random.rand(100)
mean_value = np.mean(data)
median_value = np.median(data)
std_deviation = np.std(data)
print("Среднее значение:", mean_value)
print("Медиана:", median_value)
print("Стандартное отклонение:", std_deviation)