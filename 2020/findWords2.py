# def findWord(s, wordDict):
    # # edge cases
    # if len(wordDict) == 0 or len(s) == 0:
    #     return []
    # if len(s) == 1:
    #     if s in wordDict:
    #         return [s]
    #     else:
    #         return []

    # mapping = set(wordDict) # implemented as a hash, so lookup is O(1)
    # print(mapping)

    # # queue = []

    # # for i in range(len(s) + 1):
    # #     # print(s[:i], s[i:])
    # #     result = None
    # #     if s[:i] in mapping:
    # #         # print("in set; start iterating with ", s[:i]) # needs to start with first word
    # #         # recurse(s[:i], s[i:])
    # #         result = s[:i]
    # #         queue.append((s[:i], s[i:]))
    
    # # # breadth first - takes too long 31/36 test cases
    # # print("queue: ", queue)
    # # q = queue
    # # result = []
    # # while len(q) > 0:
    # #     base, remaining = queue.pop()
    # #     # print(base, remaining)
    # #     if remaining == "":
    # #         print("RETURN: ", base)
    # #         result.append(base)
    # #     else:
    # #         # print(findWord(base, remaining))
    # #         # q = []
    # #         for i in range(len(remaining) + 1):
    # #             # print(remaining[:i])
    # #             if remaining[:i] in mapping:
    # #                 print("new iter with base:", base + " " + remaining[:i], ", remainig: ", remaining[i:])
    # #                 q.append((base + " " + remaining[:i], remaining[i:]))

    # #         # print(q)

    # # recursive attempt
    # def recurse(remaining):
    #     print("remaining: ", remaining)
    #     if remaining in mapping:
    #         return [remaining]

    #     search = ""
    #     start = 0
    #     found = []
    #     for elem in remaining:
    #         search += elem
    #         start += 1
    #         print("search: ", search)
    #         if search in mapping:
    #             found.append(search)

    #             # new base
    #             print("BASE: ", remaining[:start], " ===========")
    #             print("new iteration: recurse(", search, remaining[start:], ")")

    #             # split remaining into substrings[] (recurse here)
    #             substrings = recurse(remaining[start:])
    #             print("foudn from previous iteration (substrings): ", substrings)
    #         # append all substrings[] combinations of remaining[start:]
    #         # for elem in found:
    #         #     while len(found) > 0:
    #         #         toadd = found.pop()
    #         #     for i in range(len(substrings)):
    #         #         substrings[i] = elem + " " + substrings[i]
    #             print("found from this iteration: ", found)
    #             for i in range(len(substrings)):
    #                 for elem in found:
    #                     found[i] = found[i] + " " + substrings[i]

    #     print("result -------------- ", substrings, found)
    #     return found

    # bases = []
    # for i in range(len(s) + 1):
    #     # print(s[:i], s[i:])
    #     result = None
    #     if s[:i] in mapping:
    #         print("-------------------------------------------------------------------------------------------------------------")
    #         print("in set; start iterating with ", s[:i], s[i:]) # needs to start with first word
    #         bases.append(s[:i])
            
    #         res = recurse(s[i:]) # split that string into all possible substrings
    #         print("end recurse...", res)
    #         result = s[:i]
    #         # queue.append((s[:i], s[i:]))
    
    # print(bases)
    # return result

def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: Set[str]
    :rtype: List[str]
    """
    return helper(s, wordDict, {})
    
def helper(s, wordDict, memo):
    if s in memo: return memo[s]
    if not s: return []
    
    res = []
    for word in wordDict:
        if not s.startswith(word):
            continue
        if len(word) == len(s):
            res.append(word)
        else:
            resultOfTheRest = helper(s[len(word):], wordDict, memo)
            for item in resultOfTheRest:
                item = word + ' ' + item
                res.append(item)
    memo[s] = res
    return res

print(wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))
# print()
# print(findWord("a", []))
# print()
# print(findWord("apple", ["pear","apple","peach"]))
# print()
# print(findWord("applepie", ["pie","pear","apple","peach"]))
# print()
# print(findWord("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))