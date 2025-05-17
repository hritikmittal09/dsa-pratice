from collections import deque
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x: x[1])
        res = [intervals[0]]
        remove = 0

        for current in intervals[1:]:
            last = res[-1]
            if last[1] > current[0]:
                remove += 1
            else:
                res.append(current)

        return remove