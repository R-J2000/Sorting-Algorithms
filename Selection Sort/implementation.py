# IMPLEMENTATION OF SELECTION SORT (for reference)

def selection_sort(arr):
    """
    Sort the given array using the selection sort algorithm.
    
    Args:
        arr (list): The list of elements to sort.
    """
    
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in the unsorted part
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
