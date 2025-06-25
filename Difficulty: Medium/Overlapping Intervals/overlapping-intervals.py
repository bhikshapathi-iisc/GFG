class Solution:
	def mergeOverlap(self, intervals):
		#Code here
		intervals.sort(key=lambda x:x[0])
        index=0
        res=[]
        for i in range(1,len(intervals)):
            if intervals[index][1]>=intervals[i][0]:
                intervals[index][1]=max(intervals[index][1],intervals[i][1])
            else:
                index+=1
                intervals[index]=intervals[i]
        for i in range(index+1):
            res.append(intervals[i])
        return res