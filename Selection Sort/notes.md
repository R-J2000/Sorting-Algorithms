## Selection Sort

Selection sort is a simple comparison-based sorting algorithm. It works by dividing the input list into two parts: the sorted part and the unsorted part. The algorithm repeatedly finds the minimum element from the unsorted part and swaps it with the leftmost element of the unsorted part. This process continues until the entire list is sorted.

**Time and Space Complexity**

The time complexity of selection sort is O(n^2), where n is the number of elements in the input list. The space complexity is O(1).

Breakdown of the time complexity:

    a. The outer loop iterates n times, representing the number of passes required to sort the entire list.
    b. For each iteration of the outer loop, the inner loop iterates n-i times, where i is the current iteration of the outer loop. 
        This represents the number of comparisons needed to find the minimum element in the unsorted part.
    c. Therefore, the total number of comparisons made by selection sort is (n-1) + (n-2) + ... + 1 = n*(n-1)/2, which is in the order of n^2.

The time complexity of O(n^2) indicates that selection sort performs poorly for large input sizes. It exhibits quadratic time complexity, meaning that the time taken to execute the algorithm increases rapidly as the number of elements increases.

Regarding the space complexity:

    a. Selection sort has a space complexity of O(1) because it only requires a constant amount of additional space to 
        store temporary variables for swapping elements.
    b. The sorting is performed in-place, meaning the original input list is modified without requiring any additional space 
        proportional to the input size.
        
In summary, selection sort's time complexity is O(n^2) due to its nested loops, and its space complexity is O(1) since it operates in-place.

**Implementation Details**: 

    a. The function selection_sort takes in one parameter, arr, which is the list to be sorted.
    b. The outer for loop iterates through each element of the list using the range function. The loop index i represents the 
        current position of the sorted part.
    c. Inside the outer loop, we initialize min_idx to i, which represents the index of the minimum element in the unsorted part of the list.
    d. The inner for loop starts from i+1 and iterates through the remaining unsorted part of the list. It compares each element with 
        the current minimum element (arr[min_idx]), and if a smaller element is found, it updates min_idx to the index of that element.
    e. After finding the minimum element in the unsorted part, a swap is performed between the minimum element (arr[min_idx]) and 
        the first element of the unsorted part (arr[i]).
    f. This process is repeated for each element in the list until the entire list is sorted.
