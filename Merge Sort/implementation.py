# IMPLEMENTATION OF MERGE SORT (for reference)

def merge_sort(arr):
    """
    Sort the given array using the merge sort algorithm.
    
    Args:
        arr (list): The list of elements to sort.
        
    Returns:
        list: The sorted list.
    """
    
    # Base case: If the list is empty or has a single element, it is already sorted
    if len(arr) <= 1:
        return arr
    
    # Split the list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort the two halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    """
    Merge two sorted lists into a single sorted list.
    
    Args:
        left (list): The left sorted list.
        right (list): The right sorted list.
        
    Returns:
        list: The merged sorted list.
    """
    
    merged = []
    i = j = 0
    
    # Compare the elements of the two lists and add the smaller element to the merged list
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    # Add the remaining elements from the left list
    while i < len(left):
        merged.append(left[i])
        i += 1
    
    # Add the remaining elements from the right list
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged
