/**
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

var twoSum = function (nums, target) {
  let result = []
  let exist = {}

  for (var i = 0; i < nums.length; i++) {
    if (typeof exist[target - nums[i]] !== 'undefined') {
      result.push(exist[target - nums[i]])
      result.push(i)
    }

    exist[nums[i]] = i
  }

  return result
}

let given_nums = [2, 7, 11, 15]
let target = 9

console.log(twoSum(given_nums, target))

// Runtime: 72 ms, faster than 88.25% of JavaScript online submissions for Two Sum.
// Memory Usage: 38.3 MB, less than 9.77% of JavaScript online submissions for Two Sum.
