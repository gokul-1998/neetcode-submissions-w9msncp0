class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[] # [(temp,index)]
        for index,temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                stacktemp,stackind=stack.pop()
                res[stackind]=index-stackind
            stack.append((temperature,index))
        return res 


# steps
# 1) create an empty stack(temp,index) and a result list of 0's
# 2) iterate with index,temp over the temperatures
# 3) while stack and temp>last temp of stack
    # pop the stack elements and update the res[stackind] as
    #  current_index-stackind(original index_of_element_in_the_stack)
    # stack.append(temperature,index)
# 4) return res
