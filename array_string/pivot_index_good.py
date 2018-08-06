def pivotIndex(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    total = sum(nums)
    sum_l = 0
    for i in range(len(nums)):
        if (sum_l << 1) + nums[i] != total:
            sum_l += nums[i]
        else:
            return i
    return -1
