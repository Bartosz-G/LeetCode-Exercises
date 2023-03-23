/* https://leetcode.com/problems/palindrome-number/ */

/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let y = String(x);
    if (y.length === 1) {
        return true;
    }

    let mid = y.length / 2;

    for (let i = 0; i <= mid; i++) {
        if (y[i] !== y[y.length - i - 1]) {
            return false;
        }
    }
    return true
};
