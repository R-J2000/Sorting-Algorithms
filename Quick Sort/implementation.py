# IMPLEMENTATION OF QUICK SORT (for reference)

def quick_sort(arr):
    """
    Sort the given array using the quick sort algorithm.
    
    Args:
        arr (list): The list of elements to sort.
        
    Returns:
        list: The sorted list.
    """
    
    # Base case: If the list is empty or has a single element, it is already sorted
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]  # Choose a pivot element (in this implementation, the middle element)
    left = [x for x in arr if x < pivot]  # Elements less than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]  # Elements greater than pivot
    
    # Recursively sort the sub-arrays and combine them
    return quick_sort(left) + middle + quick_sort(right)
