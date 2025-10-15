# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:

# Input: strs = [""]

# Output: [[""]]

# Example 3:

# Input: strs = ["a"]

# Output: [["a"]]
strs = ["eat","tea","tan","ate","nat","bat"]
def solution(words: list[str])-> list[list[str]]:
    word_dict = {}

    for word in words:
        freq_encode = [0]*26
        for char in word:
            freq_encode[ord(char) - ord('a')] += 1
        key = tuple(freq_encode)
        word_dict.setdefault(key,[]).append(word)
    
    return list(word_dict.values())
        

print(solution(strs))

# Time complexity: O(n * m)
# where n is the number of words and m is the length of the longest word.
# We iterate through all n words, and for each word we iterate through m characters.

# Space complexity: O(n)
# because in the worst case, each word belongs to a different group,
# so we store n keys and n words. The key size is fixed (26 letters), so it's O(1) per key.

