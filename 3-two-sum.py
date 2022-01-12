'''
https://leetcode.com/problems/two-sum/
3. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''    

# def two_sum(nums, target):
#   #loop over the nums
#   for i in range(len(nums)):
#     # loop over the nums again
#     for j in range(len(nums)):
#       #add each number together and see if they equal target
#       if i == j: continue
#       if nums[i] + nums[j] == target:
#         return [i, j]
def two_sum(nums, target):
  hash_table = {}
  # loop over nums
  for i in range(len(nums)):
    # find the difference and store its key
    difference = target - nums[i]
    if difference not in hash_table:
    # store the index as the value
      hash_table[difference] = i
    else:
      return [hash_table[difference], i]

def two_sum(nums, target):
    table = {}

    for idx,i in enumerate(nums):
      if i in table:
        return [table[i], idx]
      else:
        table[target - i] = idx
