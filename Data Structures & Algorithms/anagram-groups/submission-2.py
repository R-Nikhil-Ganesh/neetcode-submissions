class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for i in strs:
            su = "".join(sorted(i))
            if su not in mp:
                mp[su] = []
            mp[su].append(i)
        return [mp[x] for x in mp]