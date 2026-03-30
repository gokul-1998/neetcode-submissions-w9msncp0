class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea=0
        stack=[]# pairs of [[index,height]]
        for curr_index,curr_height in enumerate(heights):
            start=curr_index
            while stack and stack[-1][1]>curr_height:
                stack_ind,stack_height=stack.pop()
                maxArea=max(maxArea,stack_height*(curr_index-stack_ind))
                start=stack_ind
            stack.append((start,curr_height))
        
        # no we need to do a for loop for all the heights, less than the current heights
        for stack_ind,stack_height in stack:
            maxArea=max(maxArea,stack_height*(len(heights)-stack_ind))
        return maxArea

    # set maxArea as 0 and stack=[]
    # for index,height in heights
        # set start=index
        # while stack and latest stack height > current height:
            # pop from stack
            # calculate maxarea as max(maxarea,popped_height*(current_index-popped_index))
            # start=index
        # stack.append((start,h))

    # this loop is when the stack height is less than the current height
    # loop over stack, and set maxArea as max(maxArea,h*(len(heights)-i)) return maxArea