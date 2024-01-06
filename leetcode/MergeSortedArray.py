# Merge Sorted Array
def merge(nums1: [int], m: int, nums2: [int], n: int):
        if len(nums1) < 1:
             nums1 = nums2
        if len(nums2) < 1:
             return nums1
        p1 = n - 1
        p2 = m - 1
        p = len(nums1) - 1

        while 0 <= p1 and 0 <= p2:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1
        # T = O( n + m ) = O( n )
        # S = O( 1 )

        if n != m:
            nums1[ : p2 + 1] = nums2[ : p2 + 1]

        return nums1
        

# Example 1:

# Input: 
# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3
# result = merge(nums1, m, nums2, n)
# print(result)
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

# Example 2:

# Input:
nums1 = [1],
m = 1
nums2 = []
n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].
result = merge(nums1, m, nums2, n)
print(result)

# https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150