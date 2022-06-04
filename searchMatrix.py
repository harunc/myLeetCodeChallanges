class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target<=matrix[i][len(matrix[0])-1]:
                for j in matrix[i]:
                    if target==j:
                        return True;
                    elif j == matrix[i][len(matrix[0])-1]:
                        return False
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target<=matrix[i][len(matrix[0])-1]:
                l,r=0,len(matrix[i])-1
                while(l<=r):
                    m=(l+r)//2
                    if matrix[i][m]<target:
                        l=m+1
                    elif matrix[i][m]>target:
                        r=m-1
                    elif matrix[i][m]==target:
                        return True
                    else:
                        return False
                    