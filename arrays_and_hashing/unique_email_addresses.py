# https://leetcode.com/problems/unique-email-addresses 

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        unique_emails = set()

        for i in range(0,len(emails)):
            names = emails[i].split('@')
            local_name = names[0]
            domain_name = names[1]

            local_name = local_name.split('+')[0]
            local_name = local_name.replace('.','')

            unique_emails.add(local_name + '@' + domain_name)
        
        return len(unique_emails)