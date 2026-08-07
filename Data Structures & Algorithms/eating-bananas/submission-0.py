class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        minspeed = right

        while left <= right:
            mid = (left + right) // 2
            hours = 0

            for pile in piles:
                hours += (pile + mid - 1) // mid

            if hours > h:
                left = mid + 1
            else:
                minspeed = mid
                right = mid - 1

        return minspeed