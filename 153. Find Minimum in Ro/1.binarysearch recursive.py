class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return self.binarySearch(nums, 0, len(nums) - 1)

    def binarySearch(self, nums, low, high):
        if low == high:
            return nums[low]
        mid = (low + high) // 2
        if nums[mid] > nums[high]:
            return self.binarySearch(nums, mid + 1, high)
        else:
            return self.binarySearch(nums, low, mid)