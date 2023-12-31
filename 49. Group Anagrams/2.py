class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker = collections.defaultdict(list)
        for i in strs:
            sort = ''.join(sorted(i))
            tracker[sort].append(i)
        return list(tracker.values())