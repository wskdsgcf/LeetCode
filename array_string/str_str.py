def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if not needle:
        return 0
    return haystack.find(needle)


if __name__ == '__main__':
    print(strStr('aaa', 'b'))