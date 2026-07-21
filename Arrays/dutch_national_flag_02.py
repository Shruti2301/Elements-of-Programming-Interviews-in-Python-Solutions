from typing import List

def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    # Grab the pivot value we will compare all the numbers against
    pivot = A[pivot_index]
    
    # Maintain the following invariants during partitioning:
    # bottom group (smaller than pivot) : A[:smaller]
    # middle group (equal to pivot)     : A[smaller : equal]
    # unclassified group (unknown)       : A[equal : larger]
    # top group (larger than pivot)      : A[larger:]
    
    # Initialize pointer boundaries: 
    # 'smaller' and 'equal' both start at index 0 (front of the array)
    # 'larger' starts at len(A) (one past the last valid index)
    smaller, equal, larger = 0, 0, len(A)
    
    # Termination Condition: 
    # Keep running as long as there are still unclassified elements (equal < larger)
    # Once 'equal' meets 'larger', all elements are categorized!
    while equal < larger: 
        # A[equal] is our current incoming unclassified element
        if A[equal] < pivot:
            # Case 1: Number is smaller than pivot
            # Swap it to the 'smaller' boundary, then expand both 'smaller' and 'equal' regions forward
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
            
        elif A[equal] == pivot:
            # Case 2: Number is equal to pivot
            # It's already in the right spot for the middle group! Just move 'equal' forward.
            equal = equal + 1
            
        else: 
            # Case 3: Number is larger than pivot (A[equal] > pivot)
            # Shrink the 'larger' boundary first, then swap the big element into the space.
            # We don't increment 'equal' here because the newly swapped-in element at A[equal]
            # is still unclassified and needs to be checked in the next loop cycle!
            larger = larger - 1
            A[equal], A[larger] = A[larger], A[equal]


# --- TESTING THE CODE ---

# 1. Define a sample list and pick a pivot index
numbers = [5, 2, 8, 3, 1, 3, 9, 0]
pivot_index = 3
    
print("Original Array:", numbers)
print(f"Pivot Value   : numbers[{pivot_index}] = {numbers[pivot_index]}\n")

# 2. Call the function (rearranges 'numbers' in-place)
dutch_flag_partition(pivot_index, numbers)

# 3. Print the result
print("Partitioned Array:", numbers)

# Why are we moving smaller forward? (smaller = smaller + 1)
# - The smaller pointer marks the boundary line between the numbers that are smaller
# than the pivot and numbers that are not
# - Once a small number is placed into A[smaller], that slot is filled and finalized
# - Moving smaller forward by 1 opens up the next slot to receive the next smaller number

# Why move equal forward? (equal = equal + 1)?
# The equal pointer is your scanner - it looks at the current unclassified element
# Before the swap, A[smaller] was pointing to an element 'equal to pivot' group
# When we swap A[equal] and A[smaller], I am placing:
# - The smaller number into A[smaller]
# - An equal number into A[equal]
# Since the element now sitting at A[equal] is known to be equal to the pivot, 
# we should not inspect it again. 

# Example : 
# Pivot = 3

        smaller                 equal
            |                    |
# Array : [ 1,  2,              3,                  0,   8   ]
#         [--- less than (<) 3] [equal to ==3]  [Unknown]

# At equal, we see 0 (which is  < 3) : We compare 0 and 3

# We swap A[smaller] and A[equal]

#      smaller      equal
          ↓           ↓
# Array: [  1,   2,     0,     3,     8  ]

# What happened? 
# Index 2 now holds 0 (small number). We extend the small group boundary : smaller = smaller + 1
# Index 3 now holds 3 (an equal number that came from smaller)

# After moving both pointers 
# smaller      equal                  ↓           ↓
# Array: [  1,   2,   0,     3,     8  ]
#       [----- < 3 ----]  [== 3] [Unknown]

# Time Complexity : O(n)
# The loop runs at most n times. Equal starts at 0 and larger starts at n (len(A)),
# The distance between equal and larger shrinks by at least 1 step in every single loop

# Space Complexity : O(1)
# Algorithm modifies array A in place
# It creates integer variable (smaller, equal and larger) to keep track of the
# pointer positions.         