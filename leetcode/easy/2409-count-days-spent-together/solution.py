class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        overlap_start = max(arriveAlice,arriveBob)
        overlap_end = min(leaveAlice,leaveBob)
        if overlap_start > overlap_end:
            return 0
        each_month_dates = [31,28,31,30,31,30,31,31,30,31,30,31]

        def no_of_days(date):
            month, day = map(int , date.split('-'))
            return sum(each_month_dates[:month - 1]) + day
        return no_of_days(overlap_end) -  no_of_days(overlap_start) + 1
        