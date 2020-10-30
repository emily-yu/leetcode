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






# def findNthDigit(n):
    
#     if n < 10:
#         return n
        
#     power = 0
#     tens = 10**power
#     val = len(str(tens)) # length value of each in power
#     valLimit = val * tens * 9 # if exceeds, subtract and go onto next power

#     # find range to search
#     while (valLimit < n):
#         print(valLimit, n)
#         n -= valLimit

#         # next level
#         power += 1
#         tens = 10 ** power
#         val = len(str(tens))
#         valLimit = val * tens * 9

#     print("in range: ", valLimit, tens, n)

#     remainder = n % val
#     completedNum = n // val # index in the range
#     # search for the number in the range; completedNum = 1 is first number
#     actual = 0
#     # while (completedNum >= val):
#     #     completedNum -= val
#     #     actual += 1
#     actual += completedNum
#     print("actual num: ", actual)
#     # actual += tens

#     print(remainder, completedNum)
    
#     # if len(str(actual)) > len(str(completedNum)):
#     actual += tens
#     #     print("actual num: ", actual)
#     # elif len(str(actual)) <= remainder:
#     #     actual += tens
#     #     print("actual num: ", actual)
#     # elif actual == tens:
#     #     actual += tens

#     # strNum = str(completedNum - 1)[remainder + len(str(actual - 1)) - val + 1]
#     if remainder == 0:
#         actual -= 1
#         return str(actual)[-1]
#     else:
#         strNum = str(actual)[remainder - 1]
#     # print(strNum)
#     # print()

#     return strNum


# print(findNthDigit(311))
# print()
# print(findNthDigit(99)) # 4
# print()
# print(findNthDigit(219)) # 9
# print()
# print(findNthDigit(10)) # 1
# print()
# print(findNthDigit(12)) # 1



# def addStrings(num1, num2):
#         print(num1, num2)
#         print(len(num1), len(num2))
#         if len(num1) > len(num2):
#             print("1")
#             shorter, longer = num2, num1
#         else:
#             print("2")
#             shorter, longer = num1, num2

#         # make shorter one equal length
#         diff = len(longer) - len(shorter)
#         shorter = ("0" * diff) + shorter
#         print(":diff", diff, shorter, longer)

#         carry = 0
#         result_str = ""
#         for i in range(len(longer), 0, -1):
#             print(int(shorter[i-1]), int(longer[i-1]))
#             result = int(shorter[i-1]) + int(longer[i-1])
#             if carry:
#                 result += 1
#                 carry = 0
            
#             if result > 9: # not end
#                 carry = 1
#                 result -= 10

#             result_str = str(result) + result_str

#         if carry: # last element
#             result_str = "1" + result_str
        
#         print(result_str)
#         return result_str
        

# addStrings("415", "1692")
# print()
# addStrings("0", "0")
# print()
# addStrings("1", "9")
# print()
# addStrings("9", "99")
# print()
# addStrings("98", "9")


def sortColors(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    if len(nums) == 0 or len(nums) == 1:
        return
    
    '''
    (2) (0) 2 1 1 0 0 1 2
        i = 2, i+1 = 0

        check for 1 or 2 values
            i == 2: 2s = 0, 2e = 0
            i == 0: none

        2 > 0 = swap i, i+1 = i+1, i
        (0) (2) 2 1 1 0 0 1 2

    0 (2) (2) 1 1 0 0 1 2 
        i = 2, i+1 = 2
        check for 1 or 2 values
            i == 2 and i+1 == 2: 2s = 0, 2e = 1
            equal, no swap
        2 == 2: continue

    0 2 (2) (1) 1 0 0 1 2  
        i = 2, i+1 = 1
        check for 1 or 2 values
            i   == 2
            i+1 == 1

        2 > 1: swap with 2s, reset 2s/2e and 1s/1e
        0 (1) 2 (2) 1 0 0 1 2  

    0 1 2 (2) (1) 0 0 1 2  
        i = 2, i+1 = 1
        check for 1 or 2 values
            i   == 2
            i+1 == 1
        2 > 1: swap
        0 1 (1) 2 (2) 0 0 1 2

    0 1 1 2 (2) (0) 0 1 2
        2 > 0: swap with 2s
        0 1 1 (0) (2) (2) 0 1 2

    0 1 1 0 2 (2) (0) 1 2
        2 > 0: swap with 2s
        0 1 1 0 (0) 2 (2) 1 2
    
    0 1 1 0 0 2 (2) (1) 2 [key]
        i = 2, swap = i+1 = 1                           ind = 6, swapInd = 6+1 = 7
        2 > 1: swap with 2s                             swap values nums[swapInd], nums[2s=5]... swap indexes swapInd, 2s
        0 1 1 0 0 (1) 2 (2) 2

        swap = 1, swap-1 = 0 != 1; swap 1e+1            if nums[swapInd] != nums[swapInd - 1], not adjacent to own kind, swap again with 1e
        0 1 1 (0) 0 (1) 2 2 2 = 0 1 1 (1) 0 (0) 2 2 2   

    at the end, deal with the 0's
    0 1 1 1 0 0 2 2 2
        2 will always be at end because comparing 2 > 1
        for 1s=3 to 1e=1: 
            2s=6 to 2e=8:
            1startInd = 6 - 1 - (3-1) = start -> prevSpace -> spaceFor1's
            for 1s to 1e, set to 0

    ex) start with 1
    (1) 0 2 2 0 1
    0 (1) 2 2 0 1 
    0 1 (2) 2 0 1
    0 1 2 (2) 0 1
    0 1 0 2 (2) 1
    0 1 0 1 2 (2) + swap 1 to 1's
    '''

    s2 = None # start 2
    e2 = None

    if nums[0] == 2: # found first 2
        s2 = 0
        e2 = 0

    for i in range(len(nums) - 1):
        # else: 
        first = nums[i]
        second = nums[i+1]
        # print("elements: ", first, second)
        # print((s2, e2))
        
        if second == 2 and e2 is None:
            s2 = i+1
            e2 = i+1

        if first == 2 and second == 1:
            # print(nums)
            nums[s2], nums[i+1] = nums[i+1], nums[s2] # values
            # print(nums)

            # shift the 2's over right
            s2 += 1 # indexes
            e2 += 1
        
        if first == second:
            if first == 2:
                e2 += 1

        # simple swap
        if second == 0: 
            if first == 1:
                nums[i], nums[i+1] = nums[i+1], nums[i] # values
            if first == 2:
                nums[s2], nums[i+1] = nums[i+1], nums[s2] # values
                s2 += 1
                e2 += 1
        print(nums)

    # # shift over the 1's next to the 0's
    # if 1 not in nums:
    #     return 

    # print
    # print(nums[::-1])
    # [1,2,0]
    

    #   '[0, 1, 1, 0, 2, 2]
    #   '[1, 0, 2]
    #   '[0, 1, 2]
    # while there is a blank space right
        # if one element
    # print(numberofOnes)

    # if only 1 and 0:
    # numbOnes = endInd - startInd + 1
    # while (numbOnes > 0):
    #     nums[len(nums) - 1 - numbOnes] = 1
    #     numbOnes -= 1

    '''
    # even number of 0's
    # odd number of 0's - radiating is fine
    numbZero = s2-1-endInd
    # numbOnes = endInd - startInd + 1
    print("zeros to right: ", s2 - 1 - endInd)
    print("ones: ", numbOnes)
    # if numbOnes % 2 == 1:
    #     nums[endInd] = 1
    for i in range(0, s2-1-endInd):
        print(endInd - i - 1, endInd + i + 1)
        if endInd - i - 1 >= 0: # process
            nums[endInd - i - 1] = 0
            print("1")
        nums[endInd + i + 1] = 1
        print("2")
    '''
    if 1 not in nums:
        return

    startInd = nums.index(1)
    endInd = len(nums) - 1 - nums[::-1].index(1)

    # if 0, 1
    if s2 is None: # no 2's
        s2 = len(nums)

    # if 0, 1, 2
    numbOnes = endInd - startInd + 1
    numbZero = s2-1-endInd
    # numbOnes = endInd - startInd + 1
    print("zeros to right: ", s2 - 1 - endInd)
    print("ones: ", numbOnes)

    # if numbOnes % 2 == 1:
    #     nums[endInd] = 1

    # for i in range(0, s2-1-endInd):
    #     print(endInd - i - 1, endInd + i + 1)
    #     if endInd - i - 1 >= 0: # process
    #         nums[endInd - i - 1] = 0
    #         print("1")
    #     nums[endInd + i + 1] = 1
    #     print("2")

    for i in range(s2 - 1, -1, -1):
        if numbOnes > 0:
            nums[i] = 1
            numbOnes -= 1
        # if nums[i] == 0: 
        #     break
        # print(i)
        else:
            nums[i] = 0
        

    # if 0, 2: nothing
    # if 1, 2: nothing
        
        
        # if more than one element
    # no blank spaces to the right
    print("=================================================NUMS: ", nums)

sortColors([1,1,0])
sortColors([1, 2, 0])
sortColors([0, 1, 2])
sortColors([2,0,2,1,1,0])

sortColors([0, 1, 0])
sortColors([0, 0])
sortColors([0, 2])