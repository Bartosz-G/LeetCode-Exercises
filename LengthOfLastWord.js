/* https://leetcode.com/problems/length-of-last-word/ */




/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    let rs = s.split("").reverse().join("");
    let len = 0;
    let spaces = 0;
    for (let lt of rs) {
        if (lt !== " ") {
            break;
        } else {
            spaces++;
        }
    }
    for (i = spaces; i<rs.length; i++) {
        if (rs[i] !== " ") {
            len++;
        } else {
            break;
        }
    }
    return len;
};
