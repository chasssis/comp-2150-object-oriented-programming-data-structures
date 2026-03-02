import random
import time

#part 2
def partition_naive(stuff):
    pivot = stuff[0]
    less = []
    greater = []
    
    for i in range(1, len(stuff)):
        if stuff[i] <= pivot:
            less.append(stuff[i])
        else:
            greater.append(stuff[i])
    
    stuff[:] = less + [pivot] + greater
    return len(less)

def partition_in_place(stuff):
    pivot = stuff[0]
    left = 1
    right = len(stuff) - 1
    
    while True:
        while left <= right and stuff[left] <= pivot:
            left += 1
        while left <= right and stuff[right] > pivot:
            right -= 1
        if left > right:
            break
        
        stuff[left], stuff[right] = stuff[right], stuff[left]
    
    stuff[0], stuff[right] = stuff[right], stuff[0]
    return right

def verify_partition(stuff, pivot_index):
    pivot = stuff[pivot_index]
    for i in range(pivot_index):
        if stuff[i] > pivot:
            return False
    for i in range(pivot_index + 1, len(stuff)):
        if stuff[i] <= pivot:
            return False
    return True

def random_list(size):
    result = []
    while len(result) < size:
        num = random.randint(1, size)
        if num not in result:
            result.append(num)
    return result

#timing&comparison
size = 10000

list1 = random_list(size)
list2 = list1.copy()

#naive time
#time.process_time() was not working
start = time.perf_counter()
pivot1 = partition_naive(list1)
end = time.perf_counter()
naive_time = end - start
naive_correct = verify_partition(list1, pivot1)

#in place time
start = time.perf_counter()
pivot2 = partition_in_place(list2)
end = time.perf_counter()
inplace_time = end - start
inplace_correct = verify_partition(list2, pivot2)

print("\nNaive Partition:")
print("Time:", naive_time)
print("Correct?:", naive_correct)

print("\nIn-Place Partition:")
print("Time:", inplace_time)
print("Correct?:", inplace_correct)
