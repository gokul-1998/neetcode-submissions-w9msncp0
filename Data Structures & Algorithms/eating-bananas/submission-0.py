class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n=len(piles)
        low=1
        high=max(piles)

        def can_koko_eat_banana(k):
            hours=0
            for pile in piles:
                hours+=math.ceil(pile/k)
            return hours<=h

        while low<=high:
            mid=(low+high)//2

            if can_koko_eat_banana(mid):
                eating_rate=mid
                high=mid-1
            else:
                low=mid+1
        return eating_rate