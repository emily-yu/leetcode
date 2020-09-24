#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if len(coins) == 0:
            return -1
        if len(coins) == 1 and amount < coins[0]:
            return -1

        tracking = [None] * (amount + 1)
        # print(tracking)

        # coins that will never have a solution
        # for i in range(1, min(coins)):
        #     tracking[i] = 999
        # print(tracking)
        for coin in coins: 
            tracking[coin] = 1

        # print("=============START==========")
        for i in range(min(coins), amount + 1):
            coinCountSet = set()
            for coin in coins:
                print("for coin value: ", coin, " at index ", i)
                numCoins = 0
                remainingAmount = i

                # validity of coin itself
                if coin <= i: # coin can be used here
                    numCoins = 1
                else:
                    # print("coin value too large")
                    numCoins = None

                if numCoins:
                    # validity of pairing with coin
                    remainingAmount -= coin
                    if remainingAmount == 0:
                        pass
                    # elif remainingAmount > 0:
                    #     numCoins = tracking[remainingAmount] + numCoins
                    elif tracking[remainingAmount] is None: # no valid value to get there from that coin
                        numCoins = None
                        # print("coin pairing gone wrong")
                        # dead end
                    else:
                        numCoins = tracking[remainingAmount] + numCoins

                # print("add ", numCoins)
                coinCountSet.add(numCoins)

                print("remainingAmount ", remainingAmount, " numCoins ", numCoins, tracking)
            print(coinCountSet)
            coinCountSet = list(filter(None, coinCountSet))
            if len(coinCountSet) > 0:
                tracking[i] = min(coinCountSet)
            else:
                tracking[i] = None
            # print("=====================")
        print(tracking)
        
        if tracking[-1] is not None:
            return tracking[-1]
        return -1
                    
# @lc code=end

