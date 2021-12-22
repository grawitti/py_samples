print_iteractions=0

def binary_search(list, item):
    low = 0
    high = len(list)-1
    
    iteractions = 0
    while low <= high:
        if print_iteractions:
            iteractions += 1
            print(iteractions)

        mid = (low + high) / 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9]

print (binary_search(my_list, 1)) # 0
print (binary_search(my_list, 3)) # 1
print (binary_search(my_list, 5)) # 2
print (binary_search(my_list, 9)) # 4
print ("\n")
print (binary_search(my_list, -1)) # None
print (binary_search(my_list, 10)) # None
