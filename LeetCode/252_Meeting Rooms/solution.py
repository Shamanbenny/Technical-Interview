class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Your code goes here
        intervals.sort()    # n log n
        for i in range(len(intervals) - 1):
            if (intervals[i+1][0] < intervals[i][1]):
                # Next meeting starts before the previous ends
                return False
        return True
