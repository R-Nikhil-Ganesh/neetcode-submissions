from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        li = sorted(d, key=d.get)
        res = []
        while k > 0:
            res.append(li.pop())
            k -= 1
        return res