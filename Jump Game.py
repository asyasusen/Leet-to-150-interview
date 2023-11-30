class Solution(object):
    def canJump(self, nums):
        furthestPossible=0
        for i in range(0, len(nums)-1):
            if i== furthestPossible and nums[i] == 0:
                return False
            jumpMax= i+nums[i]
            if jumpMax > furthestPossible:
                if jumpMax>= len(nums):
                    return True
                furthestPossible=jumpMax
        return True
        

"""
Runtime
347ms
Beats 83.44%of users with Python
Memory
14.5MB
Beats 24.99%of users with Python

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

 

Constraints:

    1 <= nums.length <= 104
    0 <= nums[i] <= 105


"""