class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            sorted_s = ''.join(sorted(i))
            if sorted_s in d:
                d[sorted_s] += [i]
            else:
                d[sorted_s] = [i]
        
        return list(d.values())