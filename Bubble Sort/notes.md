## Bubble Sort

Bubble sort is a simple comparison-based sorting algorithm. It repeatedly swaps adjacent elements if they are in the wrong order, gradually "bubbling" larger elements towards the end of the list and smaller elements towards the beginning. This process is repeated until the entire list is sorted.

**Time and Space Complexity**

Best case:

    In the best case scenario, the input list is already sorted, so no swaps are needed during the traversal.
    Bubble sort performs a single pass through the list to confirm that no swaps were made, resulting in a time complexity of O(n).
    However, in subsequent passes, the algorithm still iterates through the entire list, even though no swaps occur.
    Thus, the best case time complexity is O(n).

Average and worst cases:

    In the average and worst cases, the input list is in reverse order or has elements randomly distributed.
    Bubble sort compares and swaps adjacent elements until the largest element "bubbles" to the end of the list in each pass.
    In each pass, the algorithm makes comparisons and swaps for each pair of adjacent elements, resulting in a time complexity of O(n^2).
    As a result, the average and worst case time complexity is O(n^2).

Space complexity:

    The space complexity of bubble sort is O(1) in all cases.
    Bubble sort performs sorting operations in-place, requiring only a constant amount of additional memory for temporary variables.
    The amount of additional memory used does not depend on the size of the input list, resulting in a space complexity of O(1).
    
In summary, bubble sort has a time complexity of O(n^2) and a space complexity of O(1) in the best, average, and worst cases. Its performance is relatively inefficient, particularly for larger input sizes, compared to more optimized sorting algorithms.


**Implementation Details**: 

    a. The function bubble_sort takes in one parameter, arr, which is the list to be sorted.
    b. The variable n is initialized with the length of the list to determine the number of elements.
    c. The outer for loop iterates from 0 to n - 1, representing the number of passes required to sort the entire list.
    d. Inside the outer loop, the inner for loop iterates from 0 to n - i - 1, as the largest element in the unsorted part 
        will "bubble" up to the end in each pass.
    e. Within the inner loop, adjacent elements are compared, and if the current element is greater than the next element, a 
        swap is performed using a temporary variable.
    f. This process is repeated until the largest element in the unsorted part is moved to the correct position at the end of the list.
    g. The outer loop continues until all elements are sorted, and the final sorted list is obtained.
