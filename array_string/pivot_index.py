def pivotIndex(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums or len(nums) == 1:
        return -1
    left = 0
    al = sum(nums)
    for index, item in enumerate(nums):
        if left == (al - item) / 2:
            return index
        left += item
    return -1


if __name__ == '__main__':
    print(pivotIndex([1,7,3,6,5,6]))
