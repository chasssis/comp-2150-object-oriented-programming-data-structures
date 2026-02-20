"""
COMP 2150 – Lab 4: Searching and Sorting Fundamentals

Name: Charles Stevens
UID:U00962336

"""

import time
import random

def linear_search(lst, target):
    #Returns the index of target in lst, or -1 if not found.
    for index in range(len(lst)):
        if lst[index] == target:
            return index
    return -1

def binary_search(lst, target, left=0, right=None):
    #Recursively returns the index of target in sorted list lst, or -1 if not found.
    if right is None:
        right = len(lst) - 1
    #base case
    if left > right:
        return -1
    
    mid = (left + right) // 2
    #target found
    if lst[mid] == target:
        return mid
    #search left half
    elif target < lst[mid]:
        return binary_search(lst, target, left, mid - 1)

    #search right half
    else:
        return binary_search(lst, target, mid + 1, right)

def insertion_sort(lst):
    #Sorts lst in place using insertion sort.
    for i in range(1, len(lst)):
        key = lst[i]          #value to insert
        j = i - 1

        #shift elements > key to the right
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        #insert key
        lst[j + 1] = key

if __name__ == "__main__":
    #tests

    #1
    print("Testing linear_search...\n")
    test_list = [10, 20, 30, 40, 50]
    #beginning
    print("Beginning test (10):", linear_search(test_list, 10)) #0
    #middle
    print("Middle test (30):", linear_search(test_list, 30))    #2
    #end
    print("End test (50):", linear_search(test_list, 50))   #4
    #not present
    print("Not present test (11):", linear_search(test_list, 11))   #-1

    #2
    print("\nTesting binary_search...\n")
    sorted_list = [5, 10, 15, 20, 25, 30, 35]
    #beginning
    print("Beginning test (5):", binary_search(sorted_list, 5)) #0
    #middle
    print("Middle test (20):", binary_search(sorted_list, 20))  #3
    #end
    print("End test (35):", binary_search(sorted_list, 35)) #6
    #not present
    print("Not present test (40):", binary_search(sorted_list, 40)) #-1

    #3
    print("\nTesting insertion_sort...\n")
    #unsorted list 1
    lst1 = [5, 2, 9, 1, 5, 6]
    insertion_sort(lst1)
    print("Unsorted test1:", lst1)  #[1, 2, 5, 5, 6, 9]
    #unsorted list 2
    lst1 = [8, 4, 2, 7, 3, 5]
    insertion_sort(lst1)
    print("Unsorted test2:", lst1)  #[2, 3, 4, 5, 7, 8]
    #sorted list
    lst2 = [1, 2, 3, 4, 5]
    insertion_sort(lst2)
    print("Sorted test:", lst2)  #[1, 2, 3, 4, 5]
    #reverse
    lst3 = [9, 7, 5, 3, 1]
    insertion_sort(lst3)
    print("Reverse test:", lst3)  #[1, 3, 5, 7, 9]
    #duplicates
    lst4 = [4, 2, 4, 3, 2, 1, 1]
    insertion_sort(lst4)
    print("Duplicates test:", lst4)  # Expected: [1, 1, 2, 2, 3, 4, 4]


    print("\nTiming analysis...\n")

    lst = random.sample(range(10000), 1000)
    target = lst[-1]

    #linear search
    start = time.time()
    linear_search(lst, target)
    end = time.time()
    print(f"Linear search time: {end - start:.6f} seconds")

    #insertion sort
    lst_copy = lst.copy()
    start = time.time()
    insertion_sort(lst_copy)
    end = time.time()
    print(f"Insertion sort time: {end - start:.6f} seconds")

    #built-in sort
    lst_copy2 = lst.copy()
    start = time.time()
    sorted(lst_copy2)
    end = time.time()
    print(f"Built-in sort time: {end - start:.6f} seconds")

    #binary search (after sorting)
    start = time.time()
    binary_search(lst_copy, target)
    end = time.time()
    print(f"Binary search time: {end - start:.6f} seconds")

    #DISCUSSION
    """
    In comments below, answer:
    - Which search is faster for large lists? Why?
        Binary search is  faster for large lists because it eliminates half of the elements each step
        while linear search checks every element in the worst case.      
    - How does the time change if you double the list size?
        For linear search, time ~doubles.
        For insertion sort, time increases by ~four times .
        For binary search, time increases slightly.
    """
