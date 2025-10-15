# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

teste1 = [2,7,11,15] 
target1 = 22
teste2 = [3,4,7]
target2 = 10
def solution(nums: list[int] , target: int) -> list[int]:
    nums_dict = {}
    for index,num in enumerate(nums):
        complement = target - num
        if complement in nums_dict:
            return [nums_dict[complement],index]
        nums_dict[num] = index
    return

print(solution(teste1,target1))
print(solution(teste2,target2))

# This problem has time complexity of O(n) because it iterates throght the list only once 
# and it has space complexity of O(n) because in the worst case we keep all nums in nums_dict 