class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        verify = set(nums)
        if len(verify) != len(nums):
            return True
        else:
            return False