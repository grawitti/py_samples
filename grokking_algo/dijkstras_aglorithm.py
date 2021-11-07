# Нахождение кратчайшего пути обмена с наименьшим весом в
# направленном взвешенном ацикличном графе с помощью алгоритма Дейкстры.

# Грокаем алгоримы, Глава 7, стр. 170 - 181

# Создаем хэш-таблицу для исходного графа
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

print(graph["start"].keys())
print(graph["start"]["a"])
print(graph["start"]["b"])

# Создаём хэш-таблицу для стоимости обмена
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# Создаём хэш-табицу для записи родителей узлов
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# Создаем массив для отслеживания уже обработанных узлов
processed = []

# Функция нахождения узла с наименьшей стоимостью
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# алгоритм Дейкстры
node = find_lowest_cost_node(costs) # Шаг 1, найти узел с наименьшим весом
while node is not None: # Шаг 3, Повтрять для всех узлов
    cost = costs[node]
    neighbors = graph[node]
    # Шаг 2, проверить, существует ли более дешёвый путь к соседям этого узла,
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost: # если существует
            costs[n] = new_cost # обновить их веса
            parents[n] = node
    processed.append(node) # Шаг 4 вычисление итогового пути
    node = find_lowest_cost_node(costs)

print(parents) # Шаг 4


