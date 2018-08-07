def pascalTriangle(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    ret = []
    for i in range(0, numRows):
        ret.append((i+1) * [1])
        for j in range(1, i):
            ret[i][j] = ret[i-1][j-1] + ret[i-1][j]
    return ret


if __name__ == '__main__':
    print(pascalTriangle(100))