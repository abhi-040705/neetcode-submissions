class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #    freq = Counter(nums)
    #    res = heapq.nlargest(k, freq.keys(), key=freq.get)
    #    return res
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        return heapq.nlargest(k, count.keys(), key=count.get)