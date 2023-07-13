## Quick Sort

Quick sort is a popular divide-and-conquer sorting algorithm that works by selecting a pivot element from the list and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively, and the process continues until the entire list is sorted.

**Time and Space Complexity**

Best case:

    In the best case scenario, quick sort exhibits a time complexity of O(n log n).
    This occurs when the chosen pivot element partitions the input list into two sub-arrays of roughly equal sizes.
    In this case, the algorithm performs well and divides the problem into sub-problems efficiently.
    The time complexity of O(n log n) arises from the fact that each level of recursion splits the input into two halves, resulting 
        in log n levels, and each level performs n operations (comparisons and swaps).

Average case:

    In the average case, quick sort also has a time complexity of O(n log n).
    This assumes that the pivot selection and partitioning process is done randomly or in an average manner.
    The average case time complexity analysis takes into account the varying sizes of sub-arrays at each recursion level and their 
        corresponding partitioning operations.

Worst case:

    In the worst case scenario, quick sort has a time complexity of O(n^2).
    This occurs when the pivot selection and partitioning process consistently divides the input list into sub-arrays of unequal sizes.
    For example, when the pivot is chosen as the smallest or largest element, resulting in one sub-array with n-1 elements and 
        another with no elements.
    In this case, the algorithm degrades into a worst-case quadratic time complexity.
    However, the worst case scenario is uncommon when the pivot is chosen randomly or using a median-of-three strategy.

Space complexity:

    The space complexity of quick sort is generally O(log n) due to the recursive calls made during the partitioning process.
    The space usage is primarily determined by the maximum depth of the recursion stack, which is proportional to the logarithm of the input size.
    In-place quick sort variants have a space complexity of O(1) as they sort the list in the original memory space without additional arrays.

In summary, quick sort has an average and best case time complexity of O(n log n), a worst case time complexity of O(n^2), and a space complexity of O(log n). Quick sort is efficient in practice due to its average and best case performance, but care should be taken to avoid the worst case scenario through proper pivot selection strategies.

**Implementation Details**

    a. The function quick_sort takes in one parameter, arr, which is the list to be sorted.
    b. The base case checks if the length of the list is 0 or 1, in which case it is already sorted, and the list is returned as is.
    c. A pivot element is chosen from the list. In this implementation, the middle element is used as the pivot, but other choices are possible.
    d. The list is partitioned into three sub-arrays: left, middle, and right. The left sub-array contains elements less than the pivot, 
        middle contains elements equal to the pivot, and right contains elements greater than the pivot.
    e. The sub-arrays are recursively sorted by calling quick_sort on each sub-array.
    f. The sorted sub-arrays are then combined by concatenating left, middle, and right in that order, resulting in the final sorted list.
