/* https://leetcode.com/problems/longest-common-prefix/ */

/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    let longestprefix = strs.reduce(function(accumulator, currentValue) {
        let prefix = "";
        for (i = 0; i < accumulator.length && i < currentValue.length; i++) {
            if (accumulator[i] === currentValue[i]) {
                prefix += accumulator[i];
            } else {
                return prefix;
            }
        }
        return prefix;
    });
    return longestprefix
};

le.log(longestCommonPrefix(strs2))