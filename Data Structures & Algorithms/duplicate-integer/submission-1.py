class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # cc = set()
        # for i in nums:
        #     if i in cc:
        #         return True
        #     cc.add(i)
        # return False
        # cc = []
        # for i in nums:
        #     if i in cc:
        #         return True
        #     cc.append(i)
        # return False
        return len(set(nums)) < len(nums)

        