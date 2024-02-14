class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = [-n for n in nums]
        heapq.heapify(h)
        print(h)

        for _ in range(k - 1):
            temp = heapq.heappop(h)
            print(temp)

        ans = -heapq.heappop(h)
        return ans