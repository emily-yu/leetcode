/*
 * @lc app=leetcode id=605 lang=javascript
 *
 * [605] Can Place Flowers
 */

// @lc code=start
/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function(flowerbed, n) {
    if (n == 0) {
        return true
    }
    else if (flowerbed.length == 1) {
        if (flowerbed[0] == 1) {
            return false
        }
        return true
    }

    // c style loops
    for (var ind = 0; ind < flowerbed.length; ind++) {
        // let left = flowerbed[ind-1];
        // let right = flowerbed[ind+1];
        // console.log(ind, "lr: ", left, right, "n=", n)

        if (flowerbed[ind-1] != 1 && flowerbed[ind+1] != 1 && flowerbed[ind] != 1) { // valid placement
            n -= 1
            flowerbed[ind] = 1;
            if (n === 0) {
                return true
            }
        }
    }
    return false
};
// @lc code=end

