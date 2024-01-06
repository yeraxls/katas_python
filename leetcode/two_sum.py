def twoSum(nums: [int], target: int) -> [int]:
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [i, hashmap[complement]]
        hashmap[nums[i]] = i


# Input: 
nums = [2,7,11,15]
target = 9
# Output: [0,1]
result = twoSum(nums, target)
print(result)
        

# Input: 
nums = [3,2,4]
target = 6
# Output: [1,2]
result = twoSum(nums, target)
print(result)
        

# Input:
nums = [3,3]
target = 6
# Output: [0,1]
result = twoSum(nums, target)
print(result)
        
# https://leetcode.com/problems/two-sum/submissions/