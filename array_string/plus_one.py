def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    i = 1
    insert = []
    length = len(digits)
    while i <= length:
        num = digits.pop(-1)
        if num < 9:
            insert.insert(0, num + 1)
            digits.extend(insert)
            return digits
        insert.insert(0, 0)
        i += 1
    digits = [1]
    digits.extend(insert)
    return digits

if __name__ == '__main__':
    a = plusOne([9, 9, 9 , 9])
    for i in a:
        print(i)