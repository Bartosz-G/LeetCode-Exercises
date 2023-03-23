/* https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/ */

/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var getLucky = function(s, k) {
    const alphabet = Object.fromEntries("abcdefghijklmnopqrstuvwxyz".split("").map((letter, index) => [letter, index + 1]));
    let nums = s.split("").map(letter => alphabet[letter]).reduce((acc,val) => String(acc) + String(val),"").split("");
    for (i = 0; i < k; i++) {
        nums = nums.reduce((acc,nv) => parseInt(acc) + parseInt(nv));
        if (i == k-1) {
            break;
        } else {
            nums = String(nums).split("");
        }
    }
    return nums
};

let s1 = "iiii", k1 = 1;
let s2= "leetcode", k2 = 2;
let s3 = "zbax", k3 = 2

console.log(getLucky(s1,k1))
console.log(getLucky(s2,k2))
console.log(getLucky(s3,k3))
console.log(getLucky("a",1))
console.log(getLucky("z",2))
