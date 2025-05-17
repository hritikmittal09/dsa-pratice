class Solution:
    def merge(self, intervals: List[List[int]]) :
        if not intervals:
            return []

    # Step 1: Sort intervals by start time
        intervals.sort()

    # Step 2: Start with the first interval
        result = [intervals[0]]

        for current in intervals[1:]:
            last = result[-1]

        # Check if current interval overlaps with last
            if current[0] <= last[1]:
            # Merge: update the end of the last interval
                last[1] = max(last[1], current[1])
            else:
            # No overlap: add current interval
                result.append(current)
        return result        

       




        
        