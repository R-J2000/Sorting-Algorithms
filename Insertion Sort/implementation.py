# IMPLEMENTATION OF INSERTION SORT (for reference)

def insertion_sort(arr):
    """
    Sort the given array using the insertion sort algorithm.
    
    Args:
        arr (list): The list of elements to sort.
    """
    
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be inserted
        
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key  # Insert the current element at the correct position
