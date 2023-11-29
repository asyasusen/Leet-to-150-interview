class Solution(object):
    def lengthOfLastWord(self, s):
        arr=s.split()
        return len(arr[len(arr)-1])
        
"""
Runtime
17ms
Beats 29.01%of users with Python
Memory
13.36MB
Beats 81.00%of users with Python
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal
substring
consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

 

Constraints:

    1 <= s.length <= 104
    s consists of only English letters and spaces ' '.
    There will be at least one word in s.


"""