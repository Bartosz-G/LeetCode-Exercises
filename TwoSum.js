/* https://leetcode.com/problems/two-sum/description/ */

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const nums_checked = new Map();
    let i = 0;
    for (const x of nums) {
        let cur_dif = target - x;
        if (nums_checked.has(cur_dif)) {
            return[i, nums_checked.get(cur_dif)];
        }
        nums_checked.set(x,i);
        i++;
    }
    return [];
}