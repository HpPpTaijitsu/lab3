def longest_path(matrix, start_char):
    """
    Поиск длины самого длинного пути в матрице, начиная с заданного символа.
    Символы в пути должны следовать в алфавитном порядке без пропусков.
    """
    rows = len(matrix)
    cols = len(matrix[0])
    
    memo = [[-1] * cols for _ in range(rows)]
    
    # 8 возможных направлений движения
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]
    
    def dfs(x, y):
        """Рекурсивный DFS поиск с мемоизацией"""
        if memo[x][y] != -1:
            return memo[x][y]
        
        max_length = 1  # Минимальная длина - сама точка
        
        # Пробуем двигаться во всех 8 направлениях
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # Проверяем границы и что следующий символ - следующий по алфавиту
            if (0 <= nx < rows and 0 <= ny < cols and
                ord(matrix[nx][ny]) == ord(matrix[x][y]) + 1):
                max_length = max(max_length, 1 + dfs(nx, ny))
        
        memo[x][y] = max_length
        return max_length
    
    # Ищем максимальную длину пути среди всех начальных точек
    max_path = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == start_char:
                max_path = max(max_path, dfs(i, j))
    
    return max_path


my_matrix = [
    ['C', 'D', 'E', 'F', 'G'],
    ['B', 'C', 'D', 'E', 'F'],
    ['A', 'B', 'C', 'D', 'E'],
    ['B', 'C', 'D', 'E', 'F'],
    ['C', 'D', 'E', 'F', 'G']
]

start_char = 'C'

print("Матрица (5x5):")
for row in my_matrix:
    print(' '.join(row))

result = longest_path(my_matrix, start_char)
print(f"\nДлина самого длинного пути, начинающегося с '{start_char}': {result}")