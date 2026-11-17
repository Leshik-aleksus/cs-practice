import numpy as np

print("ЗАДАНИЕ 1. Создание векторов и матриц")

# hours - числа от 0 до 21 с шагом 3
hours = np.arange(0, 22, 3)
print("hours:", hours)
print("shape:", hours.shape)
print("ndim:", hours.ndim)
print("size:", hours.size)
print("dtype:", hours.dtype)

# line - пять равноудалённых чисел от 0 до 1 включительно
line = np.linspace(0, 1, 5)
print("\nline:", line)

# zeros - вектор из шести нулей целого типа
zeros = np.zeros(6, dtype=int)
print("zeros:", zeros)

# unknown_table - матрица формы (2, 3), заполненная числом -1
unknown_table = np.full((2, 3), -1)
print("unknown_table:\n", unknown_table)

# identity - единичная матрица 3*3
identity = np.eye(3)
print("identity:\n", identity)


print("ЗАДАНИЕ 2. Индексы и срезы в векторе")

print("Третий элемент (индекс 2):", hours[2])
print("Последний элемент:", hours[-1])
print("Элементы с индексами 2–5:", hours[2:6])
print("Каждый второй элемент:", hours[::2])
print("В обратном порядке:", hours[::-1])


print("ЗАДАНИЕ 3. Строки и столбцы таблицы")

temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print("Форма:", temperatures.shape)
print("Число измерений (ndim):", temperatures.ndim)
print("Число элементов (size):", temperatures.size)

# Значение из второй строки и третьего столбца (индексы 1, 2)
print("\ntemperatures[1, 2]:", temperatures[1, 2])

# Первая строка
print("Первая строка:", temperatures[0])

# Последний столбец
print("Последний столбец:", temperatures[:, -1])

# Первые две строки без первого столбца
print("Первые две строки без первого столбца:\n", temperatures[:2, 1:])

# Центральный фрагмент 2*2 - строки 0 и 1, столбцы 1 и 2
central = temperatures[0:2, 1:3]
print("Центральный фрагмент 2*2:\n", central)
print("Форма центрального фрагмента:", central.shape)


print("ЗАДАНИЕ 4. Прямоугольные срезы")

matrix = np.arange(1, 26).reshape(5, 5)
print("Исходная матрица 5*5:\n", matrix)

# Первые три строки
first_three_rows = matrix[:3]
print("\nПервые три строки:\n", first_three_rows)
print("shape:", first_three_rows.shape)

# Последние две строки
last_two_rows = matrix[-2:]
print("\nПоследние две строки:\n", last_two_rows)
print("shape:", last_two_rows.shape)

# Первые два столбца
first_two_cols = matrix[:, :2]
print("\nПервые два столбца:\n", first_two_cols)
print("shape:", first_two_cols.shape)

# Фрагмент из строк с индексами 1-3 и столбцов 2–4
fragment = matrix[1:4, 2:5]
print("\nФрагмент строки 1-3, столбцы 2-4:\n", fragment)
print("shape:", fragment.shape)

# Угловой блок 2*2 в правом нижнем углу
corner = matrix[-2:, -2:]
print("\nУгловой блок 2*2 в правом нижнем углу:\n", corner)
print("shape:", corner.shape)


print("ЗАДАНИЕ 5. Изменение массива с помощью срезов")

# Демонстрация из задания
vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0
print("После vector[1:4] = 0:", vector)

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9
print("small_matrix после изменений:\n", small_matrix)

# changed_hours - копия hours с изменениями
changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[1::2] = -1
print("\nchanged_hours:", changed_hours)
print("исходный hours:", hours)

# changed_matrix - копия matrix с изменениями
changed_matrix = matrix.copy()
changed_matrix[1, :] = 0          # вся вторая строка на нули
changed_matrix[:, -1] = -1        # последний столбец на -1
changed_matrix[1:4, 1:4] = 100    # центральный блок 3*3 на 100
print("\nchanged_matrix:\n", changed_matrix)
print("\nисходная matrix:\n", matrix)


print("ЗАДАНИЕ 6. Изменение формы")

numbers = np.arange(12)
print("numbers:", numbers)
print("shape numbers:", numbers.shape)

table = numbers.reshape(3, 4)
print("\ntable (3, 4):\n", table)
print("shape table:", table.shape)

transposed = table.T
print("\ntransposed (table.T):\n", transposed)
print("shape transposed:", transposed.shape)
