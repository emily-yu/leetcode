#
# @lc app=leetcode id=929 lang=python3
#
# [929] Unique Email Addresses
#

# @lc code=start
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        uniq = set()

        for i in range(len(emails)):
            endidx = emails[i].index('@')
            emailid = emails[i][:endidx]
            # if contains a plus, remove after the index of dot
            if '+' in emailid:
                idx = emailid.index('+')
                emailid = emailid[:idx]

            # parse out dots
            emailid = emailid.replace('.', '')
            
            # add to set
            uniq.add(emailid + emails[i][endidx:])
        
        return len(uniq)
# @lc code=end

