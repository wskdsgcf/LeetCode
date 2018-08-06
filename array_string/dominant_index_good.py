def dominantIndex(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    maxn=max(nums)
    
    for item in nums:
        if maxn<2*item and maxn!=item:
            return -1
    return nums.index(maxn)
