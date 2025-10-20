# Encode and Decode Strings
# Solved 
# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

# Please implement encode and decode

# Example 1:

# Input: ["neet","code","love","you"]

# Output:["neet","code","love","you"]
# Example 2:

# Input: ["we","say",":","yes"]

# Output: ["we","say",":","yes"]

class Solution:
    def encode(self,strs: list[str])->str:
        for index in range(len(strs)):
            strs[index] = f'#{len(strs[index])}{strs[index]}'
        return ''.join(strs)
    
    def decode(self,str: str)->list[str]:
        counter = 0
        final_answer = []
                
        return
    
solution = Solution()
print(solution.encode(['aa']))