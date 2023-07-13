## Merge Sort

Merge sort is a divide-and-conquer algorithm that works by dividing the input list into smaller halves, sorting them recursively, and then merging them back together to obtain the final sorted list. It follows the concept of merging two sorted arrays to merge the smaller subarrays until the entire list is sorted.

**Time and Space Complexity**

Best case:

    In the best case scenario, merge sort still requires dividing the list into smaller halves and merging them back together.
    Despite being already sorted, merge sort performs the same number of operations.
    The time complexity remains O(n log n).

Average and worst cases:

    In the average and worst cases, merge sort has a time complexity of O(n log n).
    This is because it consistently divides the input list into smaller halves until it reaches the base case (a list with 0 or 1 element) 
        and then merges them back together.
    The merge operation takes O(n) time to combine the subarrays, and the splitting process occurs recursively, leading to O(log n) levels 
        of recursion.
    As a result, the overall time complexity is O(n log n) in both cases.

Space complexity:

    The space complexity of merge sort is O(n) in all cases.
    During the sorting process, merge sort creates temporary arrays for merging the subarrays.
    The size of the temporary arrays is proportional to the input size, as each element is visited once.
    Therefore, the space complexity is O(n) due to the additional memory required for the temporary arrays.

In summary, merge sort has a time complexity of O(n log n) and a space complexity of O(n) in the best, average, and worst cases. 
    It offers efficient sorting performance, making it suitable for large input sizes.


**Implementation Details**

    a. The function merge_sort takes in one parameter, arr, which is the list to be sorted.
    b. The base case checks if the length of the list is 0 or 1, in which case it is already sorted, and the list is returned as is.
    c. If the list has more than one element, it is split into two halves using the midpoint index (mid).
    d. The two halves are recursively sorted by calling merge_sort on each half.
    e. The sorted halves are then merged back together by calling the merge function, which takes in the left and right halves as arguments.
    f. The merge function compares the elements of the two lists and adds the smaller element to the merged list.
    g. If there are any remaining elements in either the left or right list, they are added to the merged list.
    h. The final merged list is returned as the sorted list.
