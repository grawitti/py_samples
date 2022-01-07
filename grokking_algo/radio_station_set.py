# Грокаем алгоритмы, стр. 187

# Задача о покрытии множества
#
# Условие:
# Из множества радио-станций каждая их которых покрывает несколько штатов
# необходимо выбрать минимальное количество радио-станций покрывающих
# нужные штаты США.

# Список необходимых штатов
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

# Хэш-таблица для описания радио-станций и покрываемые ими штаты
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

for st, sts in stations.items():
	print(st, "{", sts, "}")

# Итоговый набор радио-станций
final_stations = set()

# Приближенный алгоритм для решения задачи
while states_needed: # Пока в states_needed есть не покрытые штаты
	best_station = None # Лучшая станция которая покрывает больше штатов
	states_covered = set() # Список штатов покрываемых лучшей станцией
	for station, states in stations.items(): # Проходим по словарю stations
		covered = states_needed & states # Пересечение states_needed и states
		if len(covered) > len(states_covered): # Если радиостанция покрывает больше штатов
			best_station = station # Назначаем эту станцию лучшей
			states_covered = covered # Обновляем спиок покрывающихся штатов

	states_needed -= states_covered # Удаляем их списка нужных штатов те которые покрылись
	final_stations.add(best_station) # В финальный список добавляем лучшую станцию
 
print(final_stations)