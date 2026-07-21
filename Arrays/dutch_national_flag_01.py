# This Dutch National Flag Problem uses a two-pass partition approach
# The goal is to rearrange an array A around a pivot value so that : 
# - All the numbers smaller than pivot come first.
# - All the numbers equal to pivot come in the middle.
# - All the numbers larger than the pivot come last.

# Instead of sorting the entire array, the algorithm rearranges in two simple sweeps:
# 1. Pass1 (Left to Right) - Sweeps forward to move every number smaller than pivot to front
# 2. Pass2 (Right to Left) - Sweeps backward to move every number larger than pivot to back
# 3. Anything left in the middle is guranteed to be equal to the pivot

# [  < pivot  |   == pivot   |  > pivot  ]
# 0        smaller        larger       len(A)-1

from typing import List
 
def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    # Grab the actual value at the given pivot index
    pivot = A[pivot_index]
    
    # First Pass - Move smaller elements to the left
    # 'smaller' keeps track fof where the next small number should go
    smaller = 0
    
    # This terminates when i reaches len(A)
    # Inspects every element from index 0 to the end once, guaranteeing that every
    # small element has been shifted to the left boundary (smaller)
    
    for i in range(len(A)):
        # If we find a number smaller than our pivot
        if A[i] < pivot: 
            # we swap it into the 'smaller' position
            A[i], A[smaller] = A[smaller], A[i]
            # and we move the 'smaller' index forward
            smaller = smaller + 1
    
    # Second Pass - Move larger elements to the right
    # 'larger' keeps track of where the next big number should go
    larger = len(A) - 1
    # Terminates when i goes past index - (reaches -1)
    for i in reversed(range(len(A))):
        # If we find a number larger than our pivot
        if A[i] > pivot : 
            # swap it into the 'larger' position
            A[i], A[larger] = A[larger], A[i]
            # and move the 'larger' index backward
            larger = larger - 1
            
# Testing :
# 1. Define your array and the pivot index
numbers = [5,2,8,3,1,3,9,0]
pivot_index = 3    # A[3] is value '3'

print(f"Original Array : {numbers}")
print(f"Pivot Value: A[{pivot_index}]  = {numbers[pivot_index]} \n")
# 2. Pass parameters into the function
dutch_flag_partition(pivot_index, numbers)

# 3. Print the array to see the changes
print("Modified Array:", numbers)

# Time Complexity : O(n) time - Every step processes at least one element
# Space Complexity : O(1) space - Operates in place