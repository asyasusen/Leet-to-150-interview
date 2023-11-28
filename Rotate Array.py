class Solution(object):
    #O(1) memory solution
    """
    Runtime
    166ms
    Beats 15.23%of users with Python
    Memory
    24.72MB
    Beats 63.08%of users with Python
    """
    def gcd(self, a, b):
        if b==0: 
            return a
        else:
            return self.gcd(b,a%b)
    def rotate(self, nums, k):
        for i in range (0, self.gcd(len(nums),k)):
            temp = nums[i]
            j=i
            while True:
                d=(j-k)%len(nums)
                if d==i:
                    break
                nums[j]=nums[d]
                j=d
            nums[j]=temp
    #Faster soln but O(n) storage
    """
    Runtime
    151ms
    Beats 64.82%of users with Python
    Memory
    25MB
    Beats 14.26%of users with Python
    """
    def rotate(self, nums, k):
        mod = k%len(nums)
        res= nums[-mod:] +nums[:-mod]
        for i in range(0, len(nums)):
            nums[i]=res[i]

        
        




"""Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

 

Constraints:

    1 <= nums.length <= 105
    -231 <= nums[i] <= 231 - 1
    0 <= k <= 105

 

Follow up:

    Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
    Could you do it in-place with O(1) extra space?

"""