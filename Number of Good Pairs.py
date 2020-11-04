class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count={}
        res=0
        for i in nums:
            count[i]=count.get(i,0)+1
        # C(n,2)
        for i in count.values():
            if i>1:
                res+=(i-1)*i/2
        return res
