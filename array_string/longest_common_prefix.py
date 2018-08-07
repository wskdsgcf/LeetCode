def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs:
        return ''
    a, prefix = min(strs, key=len), ''
    for i in a:
        prefix += i
        for j in strs:
            if not j.startswith(prefix):
                return prefix[:-1]
    return prefix


if __name__ == '__main__':
    print(longestCommonPrefix(['car']))