def partition(arr, low, high):
    pivot = arr[high]  # deterministic choice: last element as pivot
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort_deterministic(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort_deterministic(arr, low, pi - 1)
        quicksort_deterministic(arr, pi + 1, high)


# Example usage
arr = [10, 7, 8, 9, 1, 5]
print("Original Array:", arr)
quicksort_deterministic(arr, 0, len(arr) - 1)
print("Sorted (Deterministic):", arr)




import random

def randomized_partition(arr, low, high):
    # Randomly pick a pivot index and swap it with the last element
    rand_index = random.randint(low, high)
    arr[high], arr[rand_index] = arr[rand_index], arr[high]
    return partition(arr, low, high)  # use the same partition logic


def quicksort_randomized(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        quicksort_randomized(arr, low, pi - 1)
        quicksort_randomized(arr, pi + 1, high)


# Example usage
arr2 = [10, 7, 8, 9, 1, 5]
print("\nOriginal Array:", arr2)
quicksort_randomized(arr2, 0, len(arr2) - 1)
print("Sorted (Randomized):", arr2)
