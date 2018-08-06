def dominantIndex(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    a = max(nums)
    for x in nums:
        if a < 2 * x and a != x:
            return -1
    return nums.index(a)


if __name__ == '__main__':
    print(dominantIndex([1, 2, 3, 4]))
