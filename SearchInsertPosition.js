/* https://leetcode.com/problems/search-insert-position/ */


/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target, recursive = false) {
    if (recursive === false) {
        this.cut = 0;
    }
    if (nums.length === 1) {
        if (nums[0] >= target) {
            return this.cut;
        } else {
            return this.cut + 1;
        }
    }

    let mid = Math.floor(nums.length / 2);
    if (nums[mid] === target) {
        return this.cut + mid
    } else if (nums[mid] < target) {
        this.cut += mid;
        return searchInsert.call(this, nums.slice(mid), target, true);
    } else {
        return searchInsert.call(this, nums.slice(0, mid), target, true);
    }

};