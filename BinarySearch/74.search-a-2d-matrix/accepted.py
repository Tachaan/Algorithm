class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        """
        * 上下方向の探索は、rightの最大探索幅をlen(matrix)-2した区画で、midとmid+1を比較することで実現させる
        * left == right == len(matrix)-2 に到達しても条件に合わないなら、y == len(matrix) - 1, すなわち最後の配列で探索する
        """
        
        # y軸方向の探索

        left = 0
        right = len(matrix) - 2
        y = 0
        
        # 1行のみならifをスルー
        if len(matrix) == 2: # 2行なら
            if matrix[0][0] <= target and target < matrix[1][0]:
                y = 0
            else:
                y = 1
        elif len(matrix) > 2: # 3行以上ある場合
            while left <= right:
                mid = (left + right) // 2
                if matrix[mid][0] <= target and target < matrix[mid+1][0]:
                    y = mid
                    break
                elif matrix[mid][0] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                
                if mid == len(matrix) - 2:
                    y = mid + 1
                    break
            
        print("y: {}".format(y))
        # x軸方向の探索
        left = 0
        right = len(matrix[0]) - 1

        if len(matrix[0]) == 2:
            if matrix[y][0] == target or matrix[y][1] == target:
                return True
        else:
            while left <= right:
                mid = (left + right) // 2
                print("y: {}, left: {}, right: {}, mid: {}".format(y,left,right, mid))
                if matrix[y][mid] == target:
                    return True
                elif matrix[y][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return False