# IMPLEMENTATION OF HEAP SORT (for reference)

def heap_sort(arr):
    """
    Sort the given array using the heap sort algorithm.
    
    Args:
        arr (list): The list of elements to sort.
    """
    
    n = len(arr)
    
    # Build a max-heap from the input list
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements from the max-heap one by one
    for i in range(n - 1, 0, -1):
        # Swap the root (maximum element) with the last element
        arr[i], arr[0] = arr[0], arr[i]
        
        # Heapify the reduced heap
        heapify(arr, i, 0)
    

def heapify(arr, n, root):
    """
    Helper function to heapify a subtree rooted at the given root index.
    
    Args:
        arr (list): The input list.
        n (int): The size of the heap.
        root (int): The root index of the subtree.
    """
    
    largest = root
    left = 2 * root + 1
    right = 2 * root + 2
    
    # Compare the root with its left child
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # Compare the root with its right child
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # If the largest element is not the root, swap them and heapify the affected subtree
    if largest != root:
        arr[root], arr[largest] = arr[largest], arr[root]
        heapify(arr, n, largest)
