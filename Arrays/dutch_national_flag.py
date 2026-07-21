# Write a program that takes an array A and an index i into A, rearranges the elements such that
# all the elements less than A[i] ('the pivot') appear first, followed by elements equal to the
# pivot followed by elements greater than the pivot.

# The problem can be solved with O(n) additional spacemm where n = length of the array A
# We can form three lists : less than pivot, equal to pivot, greater than pivot 
# Consecutively, we can write this value into A. The Time Complexity is O(n).

# We can avoid using O(n) additional space at the cost of increased time complexity.
# In the first stage, we iterate through A starting from index 0, then index 1
# In each iteration, we seek an element smaller than the pivot -
# As soon as we find an element < pivot, we move it to the subarray of smaller elements
# In the second iteration, we move the elements > pivot, to the subarray of larger elements

from typing import List

# Enum Representation (0: RED, 1: WHITE, 2: BLUE)
RED, WHITE, BLUE = range(3)

def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    """
    Rearranges array A in place into three sections relative to pivot = A[pivot_index]:
    1. Elements < pivot
    2. Elements == pivot
    3. Elements > pivot
    """
    pivot = A[pivot_index]
    
    # First Pass : Group elements smaller than the pivot and move them to the left
    for i in range(len(A)):
        # Search ahead from i+1 to end for any element smaller than pivot
        # Look for smaller element
        for j in range(i + 1, len(A)):
            if A[j] < pivot: 
                # Swap the smaller element into the position i 
                A[i], A[j] = A[j], A[i]
                # Stop the inner loop once positon i gets a valid smaller element
                break 
    
    # Second Pass : Group elements larger than the pivot to the right
    for i in reversed(range(len(A))):
        # Iterate backwards from the end of the list
        # Look for a larger element. 
        # Stop when we reach an element less than pivot
        # Since first pass has moved them to the start of A
        # Search backwards from i - 1 to 0 for any element larger than the pivot
        for j in reversed(range(i)):
            if A[j] > pivot:
                # Swap the larger element into the position i 
                A[i], A[j] = A[j], A[i]
                # Stop the inner loop once positin i gets a valid larger element
                break
            

# Testing the Code
A = [0,1,2,0,2,1,1]
pivot_index = 1

print(f"Original array: {A}")
print(f"Pivot value: A[{pivot_index}] = {A[pivot_index]}\n")

# 2. Call the function
dutch_flag_partition(pivot_index, A)

# 3. Print the result
print(f"Partitioned array: {A}")
  
    # This two pass algorithm is using a nested loop approach to group elements without
    # requiring extra space O(1)
    
    # First Pass (Left to Right) - 
    # 1. Iterates through indices i from 0 to n - 1
    # 2. Searches forward (j > i) for the first element smaller than the pivot
    # 3. Swaps into the position i 
    # 4. This guarantess all elements smaller than the pivot end up packed at the front of A
    
    # Second Pass (Right to Left):
    # 1. Iterates backwards through indices from i from n-1 down to 0
    # 2. Searches backwards (j < i) for the first element larger than the pivot.
    # 3. Swaps it into position i 
    # 4. This says all the elements larger than the pivot end up packed at back of A
    
# Time Complexity : O(n^2)
# Because of the nested loops, in the worst case, we inspect remaining elements repeastedly

# Space Complexity : O(1)
# Modifies the array directly in place with no secondary lists created. 

