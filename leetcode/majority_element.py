def majorityElement(nums: [int]) -> int:
    max_num = 0
    hashmap = {}
    for i in range(len(nums)):
        if nums[i] in hashmap:
            hashmap[nums[i]] = hashmap[nums[i]]+1
        else:
            hashmap[nums[i]] = 1
    for j in hashmap:
        if max_num == 0:
            max_num = j
        elif hashmap[j] > hashmap[max_num]:
            max_num = j
    return max_num

# Input:
nums = [3,2,3]
# Output: 3
result = majorityElement(nums)
print(result)



# Example 2:
# Input: 
nums = [2,2,1,1,1,2,2]
# Output: 2
result = majorityElement(nums)
print(result)
