class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target: return mid
            if nums[mid] < target:
                left = mid + 1 # keep the same length of array 
            else:
                right = mid - 1
        return -1 