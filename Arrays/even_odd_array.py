# Goal : Rearrange a list of numbers so that all even numbers go to the front and all 
# the odd numbers go to the back, without creating a brand new list. 


# # This algorithm uses a two pointer partition pattern to reorder the list in place.

# Two Pointers: 
# next_even : tracks the boundary of even numbers growing from the left
# next_odd : tracks the boundary of odd numbers growing from the right
# Unprocessed numbers remain in the middle number between next_even and next_id

# Step by Step Logic :
# 1. Check the value at A[next_even]
# 2. If it is even : It is already in its correct section (left side). 
# We leave it alone and increment next_even by 1
# 3. If it is odd : It belongs on the right side. We swap it with whatever is currently at 
# A[next_odd], and decrement next_odd by 1

# Termination: 
# Once next_even >= next_odd, all the elements have been inspected, and all the evens are
# guaranteed to precede all odds.

from typing import List

def even_odd(A: List[int]) -> None:
    # Initialize two pointers:
    # next_even : starts at the beginning (index 0)
    # next_odd starts at the end (last valid index)
    next_even, next_odd = 0, len(A) - 1 
    
    # Continue processing until the two pointers meet
    # We ask ===> "Is next_even still smaller than next_odd?" If yes, then run.
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            # If the current number is even, it is already in the correct region.
            # Advance the left pointer to inspect the next element.
            next_even = next_even + 1
        else:
            # If the current number is odd, swap it with the unclassifies element
            # at the end of the list (next_odd)
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            
            # Decrement next_odd to mark the spot as known a containing odd number
            next_odd = next_odd - 1

# Testing with an input
# Sample list with mixed numbers
numbers = [3, 8, 4,5, 2, 9, 1]
print(f"Original List: {numbers}")

# Call the function
even_odd(numbers)
print(f"Partitioned List :", numbers) # Where even at left and odd at right

# Visualizing the exact moment it stops:
# Cycle N : next_even = 2, next_odd = 3 (2 < 3) ---> True : Loop runs
# Cycle N+1 : next_even = 3, next_odd = 3 ( 3 < 3) --> False : Loop Terminates
# Once both the pointers meet at the same index, every element has been classified and 
# list is fully partitioned

# Time Complexity : O(n)
# Every iteration either increments next_even or decrements next_idd, so the loop must run n times
# Space Complexity : O(1)
# Reordering happens entirely in place without allocating a new array or list