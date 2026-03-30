class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        row,column=len(matrix),len(matrix[0])
        left=0
        right=row*column-1 # 
        while left<=right:
            mid=(left+right)//2
            m_row=mid//column
            m_col=mid%column
            print(m_row,m_col)
            if matrix[m_row][m_col]==target:
                return True
            elif matrix[m_row][m_col]<target:# if mid is less than target : then target is in the right side, so left pointer comes to the right
                left=mid+1
            elif matrix[m_row][m_col]>target:
                right=mid-1
        return False