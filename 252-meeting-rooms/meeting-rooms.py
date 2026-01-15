class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Given an array of meeting time: [[1,2], [2,3], ...]
        # The meetings last the entire interval
        intervals.sort(key=lambda x:x[0]) # sort by start time
        for i in range(1, len(intervals)): # loop starting from the second
            if intervals[i][0] < intervals[i-1][1]: # compare start with prev end
                return False # return False 
        return True #return True