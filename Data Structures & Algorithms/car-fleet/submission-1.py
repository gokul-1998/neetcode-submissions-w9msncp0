class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs=[[p,s] for p,s in zip(position,speed)]
        stack=[]
        for p,s in sorted(pairs)[::-1]:
            stack.append((target-p)/s)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)

    # 1) zip the position,speed in a list called pairs and create an empty stack
    # 2) loop over sorted reverse order stack and append (target-p)/s
    # 3) we just appended the new time, if stack is just one(wont be empty at all)
    # 4) if we have atleast 2 elems in the stack, we check if the recent one is smaller
    # than or equal to previous one.if so then we pop, because the recent one will merge 
    # with the old one. return len(stack) 