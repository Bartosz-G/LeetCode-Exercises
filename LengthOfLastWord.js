/* https://leetcode.com/problems/length-of-last-word/ */




/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    s = s.trim();

    let last = s.lastIndexOf(" ");

    if (last === -1) {
        return s.length;
    }

    return s.length - last - 1;

};