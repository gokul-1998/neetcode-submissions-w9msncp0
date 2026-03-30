class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area_so_far=0
        l=0
        r=len(heights)-1

        while l<r:
            area=min(heights[l],heights[r])*(r-l)
            max_area_so_far=max(area,max_area_so_far)
            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1
        return max_area_so_far
