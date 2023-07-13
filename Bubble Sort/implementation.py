# IMPLEMENTATION OF BUBBLE SORT (for reference)

def bubble_sort(arr):
    """
    Sort the given array using the bubble sort algorithm.
    
    Args:
        arr (list): The list of elements to sort.
    """
    
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n - 1):
        
        # Last i elements are already in place, so we only need to traverse up to n - i - 1
        for j in range(n - i - 1):
            
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

