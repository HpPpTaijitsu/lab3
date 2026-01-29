def find_words(board, dictionary):
    """
    Находит все слова из словаря, которые можно составить из матрицы
    
    Args:
        board: 2D список символов (матрица M x N)
        dictionary: список слов для поиска
        
    Returns:
        Множество найденных слов
    """
    rows = len(board)
    cols = len(board[0])
    
    found_words = set()
    
    # 8 направлений движения
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]
    
    def dfs(x, y, word, index, visited):
        """Рекурсивный DFS для поиска слова"""
        # Если достигли конца слова - слово найдено
        if index == len(word):
            return True
        
        # Проверяем границы и посещенные клетки
        if (x < 0 or x >= rows or y < 0 or y >= cols or 
            visited[x][y] or board[x][y] != word[index]):
            return False
        
        # Помечаем клетку как посещенную
        visited[x][y] = True
        
        # Пробуем все 8 направлений
        for dx, dy in directions:
            if dfs(x + dx, y + dy, word, index + 1, visited):
                visited[x][y] = False  # Возвращаем состояние
                return True
        
        # Возвращаем состояние
        visited[x][y] = False
        return False
    
    for word in dictionary:
        # Создаем матрицу посещенных клеток для этого слова
        visited = [[False] * cols for _ in range(rows)]
        word_found = False
        
        # Начинаем поиск с каждой клетки
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, word, 0, visited):
                    found_words.add(word)
                    word_found = True
                    break
            if word_found:
                break
    
    return found_words


my_board = [
    ['К', 'О', 'Т'],
    ['Р', 'А', 'Н'],
    ['С', 'Л', 'О']
]

my_dictionary = ['КОТ', 'РАН', 'СОН', 'ЛОСЬ', 'НОС', 'ТОР', 'РОТ', 'КОРА']

print("\nМатрица 3x3:")
for row in my_board:
    print(' '.join(row))

print(f"\nСловарь: {my_dictionary}")

# Ищем слова
found = find_words(my_board, my_dictionary)

print(f"\nНайденные слова: {found}")