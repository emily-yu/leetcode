def findWord(s, wordDict):
    # edge cases
    if len(wordDict) == 0 or len(s) == 0:
        return []
    if len(s) == 1:
        if s in wordDict:
            return [s]
        else:
            return []

    mapping = set(wordDict) # implemented as a hash, so lookup is O(1)
    print(mapping)

    queue = []

    for i in range(len(s) + 1):
        # print(s[:i], s[i:])
        result = None
        if s[:i] in mapping:
            # print("in set; start iterating with ", s[:i]) # needs to start with first word
            # recurse(s[:i], s[i:])
            result = s[:i]
            queue.append((s[:i], s[i:]))
    
    # breadth first - takes too long 31/36 test cases
    print("queue: ", queue)
    q = queue
    result = []
    while len(q) > 0:
        base, remaining = queue.pop()
        # print(base, remaining)
        if remaining == "":
            print("RETURN: ", base)
            result.append(base)
        else:
            # print(findWord(base, remaining))
            # q = []
            for i in range(len(remaining) + 1):
                # print(remaining[:i])
                if remaining[:i] in mapping:
                    print("new iter with base:", base + " " + remaining[:i], ", remainig: ", remaining[i:])
                    q.append((base + " " + remaining[:i], remaining[i:]))

            # print(q)

    return result

print(findWord("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))
print()
print(findWord("a", []))
print()
print(findWord("apple", ["pear","apple","peach"]))
print()
print(findWord("applepie", ["pie","pear","apple","peach"]))
print()
# print(findWord("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))