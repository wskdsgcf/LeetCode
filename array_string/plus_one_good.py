def plusOne(self, digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """ 
    result=[]
    if digits[-1]!=9:
        digits[-1]=digits[-1]+1
        result=digits
    else:
        num=0
        digits.reverse()
        for i in range(len(digits)):
            num=num+digits[i]*(10**(i))
        num=str(num+1)
        for j in num:
            result.append(int(j))
    return result
