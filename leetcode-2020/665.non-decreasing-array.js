/*
 * @lc app=leetcode id=665 lang=javascript
 *
 * [665] Non-decreasing Array
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var checkPossibility = function(nums) {
    if (nums.length == 0) {
        return true
    }

    let flipped = false;
    let prev = null;

    // note: don't use foreach when needing to break xDD
    // nums.forEach(function(elem, ind) { // to break a foreach loop need to throw an exception
    
    // nums.some(elem => {
    let asdf;
    for (let elem of nums.keys()) {
        console.log(prev, nums[elem], flipped)
        if (prev == null) {
            prev = nums[elem]
        }
        else {        
            if (prev > nums[elem - 1] && flipped == true) {
                console.log("trrruuuuuuuuuuue")
                return false;
            }
            else if (prev > nums[elem] && flipped == false) {
                flipped = true
                console.log(nums)
                asdf = [...nums].splice(1, elem).sort()
                console.log(nums, asdf)
                nums.splice(elem - 1, 1)
                // elem = prev + 1
            }
            prev = nums[elem]
        }
        console.log()
    // });
    }
    console.log(asdf)
    const sorted = [...nums].sort()
    console.log(sorted, nums)
    for (let i = 0; i < nums.length; i++) {
        if (sorted[i] != nums[i]) {
            return false
        }
    }
    return true

};
// @lc code=end

