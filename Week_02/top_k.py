class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lookup = collections.Counter(nums)
        res = []
        heap = []
        for num, freq in lookup.items():
            if len(heap) == k:
                if heap[0][0] < freq:
                    heapq.heapreplace(heap, (freq, num))
            else:
                heapq.heappush(heap, (freq, num))
        while heap:
            re_num = heapq.heappop(heap)[1]
            res.append(re_num)
        return res