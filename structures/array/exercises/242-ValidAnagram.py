from collections import Counter

# Valid Anagram
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:
# Input: s = "racecar", t = "carrace"
# Output: true

# Example 2:
# Input: s = "jar", t = "jam"
# Output: false

# Constraints:
# s and t consist of lowercase English letters.

s1 = "jar"
t1 = "jam"

s2 = "racecar"
t2 = "carrac"

def validateAnagram(s: str,t: str) -> bool:
    s_map = dict()

    if(len(s) != len(t)): 
        return False

    for letter in s:
        if letter in s_map:
            s_map[letter] += 1
        else:
            s_map[letter] = 1

    for letter in t:
        if letter not in s_map or s_map[letter] == 0:
            return False
        elif letter in s_map:
            s_map[letter] -= 1
    
    return True

# 
# Time complexity: O(s) 
# Because we do a interation through string s and make a map of words and then compare 
# with letters of t so in the worst case that the words are equal we pass through all string t Which is the same size as s
# And in the best we map s and see in the first letter that t is different than s, but worst case that would be O(2n) still O(n) 

#Space complexity: O(1)
# the complexity is only O(1) because no matter what size of the input string, we still keep 
# only 26 keys which is the size of our alphabet in memory 

print(validateAnagram(s1,t1))
print(validateAnagram(s2,t2))
    
# Other approach
def validateAnagramUsingCounter(s: str, t: str) -> bool:
    return Counter(t) == Counter(s)

print(validateAnagramUsingCounter(s1,t1))
print(validateAnagramUsingCounter(s2,t2))