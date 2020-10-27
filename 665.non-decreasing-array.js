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
                nums.splice(elem - 1, 1)
                console.log(nums)
                // elem = prev + 1
            }
            // prev = elem
        }
    // });
    }
    
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

