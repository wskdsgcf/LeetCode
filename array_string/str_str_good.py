def strStr(self, haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    try:
        index = haystack.index(needle)
        return index
    except:
        return -1
