class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        """
        * 行と列を1D matrixとして扱い、そのindexを行・列に分解して位置を特定している
        """
        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1 # highは行・列の最大位置

        while low <= high:
            mid = (low+high) // 2
            num = matrix[mid // cols][mid % cols]
            # 行方向: index // 列数
            # 列方向: index % 列数

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1

        return False