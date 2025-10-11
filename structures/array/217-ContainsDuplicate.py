# Contains Duplicate
# Solved 
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:
# Input: nums = [1, 2, 3, 3]
# Output: true

# Example 2:
# Input: nums = [1, 2, 3, 4]
# Output: false

test1 = [1,2,3,4] 
test2 = [1,1,3,4]

def hasDuplicate(duplicateList):
    visited_nums = set()
    for num in duplicateList:
        if num in visited_nums:
            return True
        else:
            visited_nums.add(num) 
    return False


print(hasDuplicate(test1))
print(hasDuplicate(test2))