## Heap Sort

Heap sort is a comparison-based sorting algorithm that uses the concept of a binary heap data structure. It builds a max-heap (for ascending order) or a min-heap (for descending order) from the input list and repeatedly extracts the root element to obtain the sorted list.

**Time and Space Complexity**

Best case:

    Heap sort does not have a best case scenario different from the average or worst case.
    Regardless of the input characteristics, heap sort requires building a heap and performing the same number of comparisons and swaps.
    The best case time complexity is O(n log n).

Average and worst cases:

    The average and worst cases of heap sort have the same time complexity of O(n log n).
    Heap sort builds a heap from the input list, which takes O(n) time.
    The process of repeatedly extracting the root element and maintaining the heap property requires log n iterations, each taking O(log n) time.
    Therefore, the overall time complexity is O(n log n) in both cases.

Space complexity:

    The space complexity of heap sort is O(1) in all cases.
    Heap sort performs sorting operations in-place, without requiring additional memory proportional to the input size.
    Only a constant amount of additional memory is used for temporary variables during the heapify operation.
    As a result, the space complexity is O(1).

In summary, heap sort has a time complexity of O(n log n) in the best, average, and worst cases. It provides consistent performance characteristics for different input distributions. The space complexity of heap sort is O(1) as it operates in-place without requiring additional memory proportional to the input size.

**Implementation Details**

    a. The function heap_sort takes in one parameter, arr, which is the list to be sorted.
    b. The variable n is initialized with the length of the list to determine the number of elements.
    c. The initial step of heap sort is to build a max-heap from the input list. This is done by calling the heapify function for each 
        non-leaf node in the list, starting from the last non-leaf node and moving up to the root.
    d. The heapify function takes in the input list, the size of the heap (n), and the root index of the subtree. It ensures that the 
        subtree rooted at the given index maintains the heap property: the parent is greater than its children (in the case of a max-heap).
    e. The heapify function compares the root element with its left and right children, determines the largest element among the three, 
        and swaps it with the root if necessary. This maintains the heap property for the affected subtree.
    f. After building the max-heap, heap sort proceeds to extract elements from the heap one by one. In each iteration, the maximum 
        element (root) is swapped with the last element of the heap and removed from consideration.
    g. The heapify function is called on the reduced heap to ensure that the new root element satisfies the heap property.
    h. The process continues until the entire list is sorted.
