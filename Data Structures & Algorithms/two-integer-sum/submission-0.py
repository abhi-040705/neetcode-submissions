class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, item in enumerate(nums):
            res = target -  item
            if res in seen:
                return [seen[res], index]
            seen[item] = index
        return []
        