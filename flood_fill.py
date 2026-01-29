# Реализация алгоритма заливки (Flood Fill) с использованием рекурсивного DFS
def flood_fill(matrix, x, y, target, replacement):
    """
    Рекурсивный алгоритм заливки, использующий поиск в глубину
    
    matrix: двумерный массив (матрица)
    x, y: начальные координаты (строка, столбец)
    target: целевой цвет для замены
    replacement: цвет замены
    """
    # Проверка границ матрицы
    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
        return
    
    # Если текущий цвет не совпадает с целевым или уже заменен
    if matrix[x][y] != target or matrix[x][y] == replacement:
        return
    
    # Замена цвета текущей клетки
    matrix[x][y] = replacement
    
    # Рекурсивный вызов для соседних клеток (4 направления)
    flood_fill(matrix, x + 1, y, target, replacement)  # Вниз
    flood_fill(matrix, x - 1, y, target, replacement)  # Вверх
    flood_fill(matrix, x, y + 1, target, replacement)  # Вправо
    flood_fill(matrix, x, y - 1, target, replacement)  # Влево


# Исходная матрица
matrix = [
    ["Y", "Y", "Y", "G", "G", "G", "G", "G", "G", "G"],
    ["Y", "Y", "Y", "Y", "Y", "Y", "G", "X", "X", "X"],
    ["G", "G", "G", "G", "G", "G", "G", "X", "X", "X"],
    ["W", "W", "W", "W", "W", "G", "G", "G", "G", "X"],
    ["W", "R", "R", "R", "R", "R", "G", "X", "X", "X"],
    ["W", "W", "W", "R", "R", "G", "G", "X", "X", "X"],
    ["W", "B", "W", "R", "R", "R", "R", "R", "R", "X"],
    ["W", "B", "B", "B", "B", "R", "R", "X", "X", "X"],
    ["W", "B", "B", "X", "B", "B", "B", "B", "X", "X"],
    ["W", "B", "B", "X", "X", "X", "X", "X", "X", "X"]
]

# Параметры для заливки
start_x, start_y = 3, 9      # Начальная точка
target_color = "X"           # Заменяемый цвет
replacement_color = "C"      # Новый цвет

print("Исходная матрица:")
for row in matrix:
    print(row)

# Выполняем заливку
flood_fill(matrix, start_x, start_y, target_color, replacement_color)

print("\nМатрица после заливки:")
for row in matrix:
    print(row)


print("Алгоритм начал работу с точки (3, 9)")
print("Целевой цвет для замены: 'X'")
print("Цвет замены: 'C'")