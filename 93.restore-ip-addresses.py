#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # try 1
        # 85/147 cases passed (N/A)
        '''
        if len(s) == 4:
            return [".".join(list(s))]
        if len(s) < 4:
            return []

        # last two spots are auto candidates (< 255, not three digits)
        candidates = [len(s) - 1, len(s) - 2]
        print(candidates)

        # pick out ones with 1 or 2 to right
        for i in range(len(s) - 1):
            # print(s[i], s[i+1])
            if s[i+1] == "1" or s[i+1] == "2": # candidate
                # print("candidate: ", s[i], s[i+1])
                candidates.append(i+1)
            if s[i+1] == "0" and s[i] == "0":
                candidates.append(i+1)

        candidates.sort()
        print(candidates)

        # search for blocks of 4 numbers
        # index_blocks = []
        print("to_check, dot locations")
        def recurse(base, select, res):
            # print("selection: ", select)
            ind = 0
            for elem in select:
                # print("base: ", base)
                # print("elem: ", elem)
                # print("base: ", base + [elem])

                if elem not in base:
                    if len(base + [elem]) == 3:
                        res += [base + [elem]]
                    else:
                        # print(select[ind:])
                        recurse(base + [elem], select[ind+1:], res)
                    ind += 1
            return res

        print(len(candidates) - 3)
        index_blocks = []
        for i in range(1, len(candidates) - 2):
            print(candidates[i-1:i], candidates[i:])
            index_blocks += recurse(candidates[i-1:i], candidates[i:], [])
        print(index_blocks)
        print(len(index_blocks))

        print("slicing")
        # for block in index_blocks:
        for i in range(len(index_blocks)):
            res = ""
            start = 0
            # for index in index_blocks[i]:
            block = index_blocks[i]
            # print("new block: ", block)
            for j in range(len(block)):
                ind = block[j]
                numb = int(s[start: ind])
                # print(numb)
                block[j] = s[start: ind]
                start = ind
            block.append(s[start:])
            # print("res", res)
            # print("done: ", block, index_blocks)
        # print(res)
        print("...")
        print(index_blocks)

        ind = 0
        for elem in index_blocks:
            for numb in elem:
                if numb[0] == '0' and len(numb) > 1:
                    index_blocks[ind] = None

                numb = int(numb)
                if numb > 255 or numb < 0:
                    index_blocks[ind] = None
                    
            ind += 1

        res = []     
        for elem in index_blocks:
            if elem is not None:
                res.append(".".join(elem))
        
        return list(set(res))
        '''

        # try 2 - attempt to code from memory
        # https://www.youtube.com/watch?v=JfB3BugMht8&ab_channel=AmellPeralta

        def isValid(inp):
            if len(inp) > 4 or len(inp) == 0:
                return False
            if inp[0] == "0" and len(inp) > 1:
                return False
            intput = int(inp)
            if intput > 255 or intput < 0:
                return False

            return True

        start = 0
        res = []
        for elem1 in range(start, start + 4 + 1):
            # print(elem1)
            # print("elem1: ", s[start:elem1])
            elem1str = s[start:elem1]
            if isValid(elem1str): # isValid
                for elem2 in range(elem1 + 1, elem1 + 4):
                    # print(elem2)
                    # print("elem1: ", s[start:elem1])
                    # print("elem2: ", s[elem1 + 1: elem2])
                    elem2str = s[elem1: elem2]
                    if isValid(elem2str): #isValid
                        for elem3 in range(elem2 + 1, elem2 + 4):
                            elem3str = s[elem2: elem3]
                            elem4str = s[elem3:]
                            # print("elem1: ", s[start:elem1])
                            # print("elem2: ", s[elem1: elem2])
                            # print("elem3: ", s[elem2: elem3])
                            # print("elem4: ", s[elem3:])
                            print(elem1str, elem2str, elem3str, elem4str)
                            if isValid(elem3str) and isValid(elem4str):
                                print("elem4: ", s[elem3:])
                                print("made it")
                                print("-------")
                                res.append(elem1str + "." + elem2str + "." + elem3str + "." + elem4str)
        return res
                
# @lc code=end

