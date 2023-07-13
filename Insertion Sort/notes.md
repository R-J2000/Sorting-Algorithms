## Insertion Sort

Insertion sort is a simple comparison-based sorting algorithm that builds the final sorted list one element at a time. It divides the input list into a sorted and an unsorted part. It iterates through the unsorted part, comparing each element with the elements in the sorted part and inserting it at the correct position to maintain the sorted order.

**Time and Space Complexity**

The time complexity of insertion sort varies based on the input characteristics.

Best case:

    In the best case scenario, when the input list is already sorted, insertion sort exhibits a time complexity of O(n).
    This is because each element in the list only needs to be compared to the elements before it once, and no swapping is required.

Average and worst cases:

    In the average and worst cases, insertion sort has a time complexity of O(n^2).
    This occurs when the input list is in reverse order or has elements in a random order.
    In these cases, each element needs to be compared and potentially swapped with all the elements before it, 
        resulting in a quadratic time complexity.
        
Space complexity:

    The space complexity of insertion sort is O(1) because it operates in-place and does not require additional space proportional to the input size.
    Only a constant amount of additional memory is used to store temporary variables.
    
It's worth noting that while insertion sort has a quadratic time complexity in the worst case, it can perform well for small input 
sizes or when the input is nearly sorted. Its advantage lies in its simplicity and efficiency for small or partially sorted lists.

**Implementation Details**: 

    a. The function insertion_sort takes in one parameter, arr, which is the list to be sorted.
    b. The outer for loop iterates through the unsorted part of the list, starting from the second element (i = 1) up to the last element (len(arr)).
    c. Inside the outer loop, the current element to be inserted (key) is stored in a temporary variable.
    d. The inner while loop compares the current element (key) with the elements in the sorted part of the list (arr[0..i-1]).
    e. If an element in the sorted part is greater than the current element (arr[j] > key), it shifts that element one position 
        ahead (arr[j + 1] = arr[j]).
    f. The j index is decremented to continue comparing with previous elements until the correct position for the current element is found.
    g. Finally, the current element (key) is inserted at the correct position in the sorted part of the list (arr[j + 1] = key).
