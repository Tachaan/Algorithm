# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n - 1

        while left <= right:
            mid = (left + right) // 2
            print("left:{}, right:{}, mid:{}".format(left,right,mid))
            if not isBadVersion(mid) and isBadVersion(mid+1):
                return mid + 1
            elif isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return 1

