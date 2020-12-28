s = 'ACAABAACCBBBBBB'
# (A, 1)(C, 1)(B, 1)(A, 2)(C, 2)(B, 6)

# q = []
# prev = s[0]
# prevind = 0
# for i in range(1, len(s)):
#     if s[i] != prev:
#         # print(prev, i-prevind)
#         q.append((prev, i-prevind))
#         prev = s[i]
#         prevind = i
#     if i == len(s) - 1:
#         # print(s[i], i-prevind+1)
#         q.append((s[i], i-prevind+1))

# print(q)         

# (A, 1)
# > (C, 1)... gap = 1
# > (B, 1)... gap = 2
# > (A=A, 2)
# > (C, 2)... gap = 4 > 2 [done]
# end; count = 3
k=2

gap = 0

pivot = None
count = 0
max = 0
# for block in q:
#     print(block)
#     if pivot is None:
#         pivot = block[0]
#         count = block[1]

#     elif block[0] != pivot:
#         gap += block[1]

#     if gap > k:
#         print("end; count = ", count)
#         count = 0
#         pivot = block
#         # pivot reste


# (A, 1)(C, 1)(B, 1)(A, 2)(C, 2)(B, 6)
'''
A: [0, 3]
B: [2]
C: [1, 4]
'''
s = "AABABBA"

q = []
prev = s[0]
prevind = 0
for i in range(1, len(s)):
    if s[i] != prev:
        # print(prev, i-prevind)
        q.append((prev, i-prevind))
        prev = s[i]
        prevind = i
    if i == len(s) - 1:
        # print(s[i], i-prevind+1)
        q.append((s[i], i-prevind+1))

print(q)         

tracking = {}
for ind, elem in enumerate(q):
    print(ind, elem)
    if elem[0] in tracking:
        tracking[elem[0]].append(ind)
    else:
        tracking[elem[0]] = [ind]

print(tracking)

currmax = 0
for ind, elem in enumerate(q):
    print(ind, elem)

    count = 0
    gap = 0
    for i in range(ind, len(q)):
        print(q[i], count)


        # print(q[i][0], elem[0], elem[1])
        if q[i][0] == elem[0]:
            count += q[i][1]
        else:
            if gap > 2:
                print("ct of: ", elem, ", ", count)
                if count > currmax:
                    currmax = count
                count = 0
                break
            count += q[i][1]
            gap += q[i][1]
        print("count: ", count, ' gap: ', gap)

    if count > currmax:
        currmax = count
    print()
# return currmax
print(currmax)


# 0 ('A', 1)
# 1 ('C', 1)
# 2 ('A', 2)
# 3 ('B', 1)
# 4 ('A', 2)
# 5 ('C', 2)
# 6 ('B', 6)
# {'A': [0, 2, 4], 'C': [1, 5], 'B': [3, 6]}