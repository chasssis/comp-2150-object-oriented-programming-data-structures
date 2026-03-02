#COMP 2150 – Spring 2026
#University of Memphis
#Charles Stevens

#part 1
def power(b, n):
    if n == 0:
        return 1
    elif n > 0:
        return b * power(b, n - 1)
    else:
        return 1 / power(b, -n)
    
def count_negatives(stuff):
    if stuff == []:
        return 0
    if stuff[0] < 0:
        return 1 + count_negatives(stuff[1:])
    else:
        return count_negatives(stuff[1:])

def all_short(stuff):
    if stuff == []:
        return True
    if len(stuff[0]) <= 8:
        return all_short(stuff[1:])
    else:
        return False

def binary_search(stuff, target):
    def helper(stuff, target, low, high):
        if low > high:
            return False
        mid = (low + high) // 2
        if stuff[mid] == target:
            return mid
        elif target < stuff[mid]:
            return helper(stuff, target, low, mid - 1)
        else:
            return helper(stuff, target, mid + 1, high)
    return helper(stuff, target, 0, len(stuff) - 1)

#testing
print("Testing power:")
print(power(2, 3))#positive
print(power(5, 0))#zero
print(power(2, -2))#negative

print("\nTesting count_negatives:")
print(count_negatives([-1, -5, -3]))#all negative
print(count_negatives([1, 2, 3]))#all non-negative
print(count_negatives([-1, 2, -3, 4]))#mixed
print(count_negatives([]))#empty list

print("\nTesting all_short:")
print(all_short(["cat", "dog"]))#all short
print(all_short(["elephant", "giraffe"]))#all long
print(all_short(["cat", "hippopotamus"]))#mixed
print(all_short([]))#empty list

print("\nTesting binary_search:")
sorted_list = [1, 3, 5, 7, 9, 11]

print(binary_search(sorted_list, 7))#present
print(binary_search(sorted_list, -5))#too low
print(binary_search(sorted_list, 15))#too high
print(binary_search(sorted_list, 6))#not present but in range
print(binary_search([], 5))#empty list