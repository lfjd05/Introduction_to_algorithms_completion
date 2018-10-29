"""
    给定一个方形整数数组 A，我们想要得到通过 A 的下降路径的最小和。
下降路径可以从第一行中的任何元素开始，并从每一行中选择一个元素。
在下一行选择的元素和当前行所选元素最多相隔一列。

方法：可以尝试用beam search试试
"""


class Solution:
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        if len(A) == 1:
            return A[0][0]

        result = []
        line_sum = 0
        n_line = len(A)
        i = 0
        next_j = [0]

        while i < n_line:
            for j in next_j:
                line_sum += A[i][j]
            result.append(line_sum)
            if j == 0:
                next_j = [j, j+1]
            elif j == n_line:
                next_j = [j - 1, j]
            else:
                next_j = [j-1, j, j + 1]
            i += 1
        return min(result)


print(Solution().minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))
