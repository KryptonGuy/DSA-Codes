# Runtime: 94 ms, faster than 57.24% of Python3 online submissions for Unique Email Addresses.
# Memory Usage: 14.1 MB, less than 36.27% of Python3 online submissions for Unique Email Addresses.

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for email in emails:
            if len(email)<0:
                continue  
            user, domain = email.split('@')
            if '+' in user:
                user = user.split('+')[0]            
            s.add(f"{user.replace('.','')}@{domain}")
        return len(s)
            