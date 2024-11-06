import time
import random

# Heapsort Implementation

def heapify(arr, n, i):
    # Initialize largest as root
    largest = i  
    # Left child index
    left = 2 * i + 1  
    # Right child index
    right = 2 * i + 2  

    # If left child is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child is larger than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        # Swap
        arr[i], arr[largest] = arr[largest], arr[i]
        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)
    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)

    return arr

# Quicksort Implementation
def quicksort(arr):
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr
    # Select pivot element
    pivot = arr[len(arr) // 2]
    # Partition the array into three parts
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    # Recursively apply quicksort to the partitions
    return quicksort(left) + middle + quicksort(right)

# Merge Sort Implementation
def merge_sort(arr):
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr
    # Split the array into two halves
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    # Merge the sorted halves
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    # Merge the two arrays while maintaining order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Append any remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Function to run time tests
def run_time_tests():
    # Different input sizes and types
    input_sizes = [1000, 5000, 10000]
    input_types = ['sorted', 'reverse_sorted', 'random']

    for size in input_sizes:
        print(f"\nTesting with array size: {size}")

        for arr_type in input_types:
            # Generate input arrays based on the type
            if arr_type == 'sorted':
                arr = list(range(size))
            elif arr_type == 'reverse_sorted':
                arr = list(range(size-1, -1, -1))  # Starts at size-1 and ends at 0
            else:
                arr = [random.randint(0, 10000) for _ in range(size)]

            # Print the initial array (only first 10 elements for readability)
            print(f"Initial {arr_type} array: {arr[:10]}...")

            # Measure time for Heapsort
            arr_copy = arr.copy()
            start_time = time.time()
            sorted_arr = heapsort(arr_copy)
            end_time = time.time()
            print(f"Heapsort ({arr_type}): {end_time - start_time:.6f} seconds")
            print(f"Sorted array: {sorted_arr[:10]}...")

            # Measure time for Quicksort
            arr_copy = arr.copy()
            start_time = time.time()
            sorted_arr = quicksort(arr_copy)
            end_time = time.time()
            print(f"Quicksort ({arr_type}): {end_time - start_time:.6f} seconds")
            print(f"Sorted array: {sorted_arr[:10]}...")

            # Measure time for Merge Sort
            arr_copy = arr.copy()
            start_time = time.time()
            sorted_arr = merge_sort(arr_copy)
            end_time = time.time()
            print(f"Merge Sort ({arr_type}): {end_time - start_time:.6f} seconds")
            print(f"Sorted array: {sorted_arr[:10]}...")

# Run the time tests
run_time_tests()