def arrayPairSum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    return sum(nums[::2])


if __name__ == '__main__':
    print(arrayPairSum([1,4,3,2]))