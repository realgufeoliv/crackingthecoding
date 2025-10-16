from collections import Counter
# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# The test cases are generated such that the answer is always unique.

# You may return the output in any order.

# Example 1:

# Input: nums = [1,2,2,3,3,3], k = 2

# Output: [2,3]
# Example 2:

# Input: nums = [7,7], k = 1

# Output: [7]

teste1 = [1,2,2,3,3,3]
teste2 = [7,7]

def solution(nums: list[int],k: int) -> int:
    freq_element = Counter(nums) 
    biggest_freq = [[] for num in range(len(nums)+1)] 
    for (item,freq) in freq_element.items(): 
        biggest_freq[freq].append(item)
    
    final_answer = []

    for index in range(len(biggest_freq)-1,0,-1):
        for num in biggest_freq[index]:
            final_answer.append(num)
            k -= 1
            if k == 0:
                return final_answer

        
    return final_answer

print(solution(teste1,2))
print(solution(teste2,1))