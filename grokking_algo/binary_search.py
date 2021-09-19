def binary_search(list, item):
    low = 0
    high = len(list)-1
    
    iteractions = 0
    while low <= high:
        iteractions += 1
        print(iteractions)
        mid = (low + high)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9]

print (binary_search(my_list, 3)) # 1
print ("\n")
print (binary_search(my_list, -1)) # None
