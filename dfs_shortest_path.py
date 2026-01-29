def dfs_shortest_path(graph, start, goal):
    min_distance = float('inf')
    best_path = []
    
    def dfs(current, distance, path, visited):
        nonlocal min_distance, best_path
        
        # Если достигли цели
        if current == goal:
            if distance < min_distance:
                min_distance = distance
                best_path = path.copy()
            return
        
        # Добавляем текущую вершину в посещенные
        visited.add(current)
        
        # Рекурсивно обходим всех соседей
        for neighbor, cost in graph.get(current, []):
            if neighbor not in visited:
                path.append(neighbor)
                dfs(neighbor, distance + cost, path, visited)
                path.pop()  # Возвращаемся назад для поиска других путей
        
        # Удаляем вершину из посещенных для других путей
        visited.remove(current)
    
    # Запускаем DFS
    dfs(start, 0, [start], set())
    
    return min_distance, best_path


romania_map = {
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Vaslui', 142), ('Hirsova', 98)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)]
}

print("Поиск минимального расстояния с помощью метода поиска в глубину")

# Тестируем на нескольких маршрутах
test_routes = [
    ('Arad', 'Bucharest'),
    ('Timisoara', 'Bucharest'),
    ('Oradea', 'Bucharest'),
    ('Arad', 'Craiova')
]

print("\nГРАФ ДОРОГ РУМЫНИИ")
print("Количество городов:", len(romania_map))

for start, goal in test_routes:
    print("\n" + "-" * 60)
    print(f"Маршрут: {start} -> {goal}")
    
    # Используем DFS для поиска минимального пути
    distance, path = dfs_shortest_path(romania_map, start, goal)
    
    if distance < float('inf'):
        print(f" DFS нашел путь")
        print(f"  Расстояние: {distance} км")
        print(f"  Путь: {' -> '.join(path)}")
    else:
        print(f" DFS не нашел путь")
    
    # Сравнение с ручным расчетом для Arad -> Bucharest
    if start == 'Arad' and goal == 'Bucharest':
        print("\n  СРАВНЕНИЕ С РУЧНЫМ РАСЧЕТОМ:")
        print("  " + "-" * 50)
        
        # Известные маршруты из лабораторной работы
        print("  Известные маршруты из лабораторной работы 1:")
        print("  1. Arad -> Sibiu -> Rimnicu Vilcea -> Pitesti -> Bucharest")
        print("     Расстояние: 140 + 80 + 97 + 101 = 418 км")
        print("  2. Arad -> Sibiu -> Fagaras -> Bucharest")
        print("     Расстояние: 140 + 99 + 211 = 450 км")
        print("  3. Arad -> Timisoara -> Lugoj -> Mehadia -> Drobeta -> Craiova -> Pitesti -> Bucharest")
        print("     Расстояние: 118 + 111 + 70 + 75 + 120 + 138 + 101 ≈ 733 км")
        
        if distance == 418:
            print(f"\n   Метод поиска в глубину нашел оптимальный путь (418 км)")
            print("  Этот путь совпадает с результатом A* поиска из лаб. работы 1")
        elif distance == 450:
            print(f"\n  ! Метод поиска в глубину нашел путь 450 км")
            print("  Это не оптимальный путь, но допустимый")
        else:
            print(f"\n  Метод поиска в глубину нашел путь {distance} км")
            print("  Это не совпадает с ожидаемыми результатами")