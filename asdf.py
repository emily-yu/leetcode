# def findNthDigit(n):
#     def helper(num, power, digitct):
#         if num - 10 < 0:
#             return digitct + 1 # add the ones digit
        
#         # process data
#         remainder = num % 10

#         tens = 10**power
#         num = num // tens
#         power += 1
#         print(tens)
#         print(tens, len(str(tens)) * tens * 9)
#         digitct += len(str(tens)) * tens * 9
        
#         print(num, remainder, digitct)
#         return helper(num, power, digitct)
        
#     return helper(n, 1, 0)

def findNthDigit(n):
    
    if n < 10:
        return n
        
    power = 0
    tens = 10**power
    val = len(str(tens)) # length value of each in power
    valLimit = val * tens * 9 # if exceeds, subtract and go onto next power

    # find range to search
    while (valLimit < n):
        print(valLimit, n)
        n -= valLimit

        # next level
        power += 1
        tens = 10 ** power
        val = len(str(tens))
        valLimit = val * tens * 9

    print("in range: ", valLimit, tens, n)

    remainder = n % val
    completedNum = n // val # index in the range
    # search for the number in the range; completedNum = 1 is first number
    actual = 0
    # while (completedNum >= val):
    #     completedNum -= val
    #     actual += 1
    actual += completedNum
    print("actual num: ", actual)
    # actual += tens

    print(remainder, completedNum)
    
    # if len(str(actual)) > len(str(completedNum)):
    actual += tens
    #     print("actual num: ", actual)
    # elif len(str(actual)) <= remainder:
    #     actual += tens
    #     print("actual num: ", actual)
    # elif actual == tens:
    #     actual += tens

    # strNum = str(completedNum - 1)[remainder + len(str(actual - 1)) - val + 1]
    if remainder == 0:
        actual -= 1
        return str(actual)[-1]
    else:
        strNum = str(actual)[remainder - 1]
    # print(strNum)
    # print()

    return strNum


print(findNthDigit(311))
print()
print(findNthDigit(99)) # 4
print()
print(findNthDigit(219)) # 9
print()
print(findNthDigit(10)) # 1
print()
print(findNthDigit(12)) # 1
