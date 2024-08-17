# arrays & hashing
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        # remove the purchaseAmount rounded to nearest multiple of 10
        down = (purchaseAmount // 10)*10
        up = down + 10
        if purchaseAmount % 10 < 5:
            return 100 - down
        return 100 - up

