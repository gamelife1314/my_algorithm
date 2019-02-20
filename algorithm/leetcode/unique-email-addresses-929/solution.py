
class Solution:

    def numUniqueEmails(self, emails: 'List[str]') -> 'int':
        sets = set()
        for email in emails:
            sets.add(self.fix_email(email))
        print(sets)
        return len(sets)

    def fix_email(self, email: str):
        local, domain = tuple(email.split('@'))
        plus_index = local.find('+')
        if plus_index != -1:
            local = local[:plus_index]
        local = local.replace('.', '')
        return '{local}@{domain}'.format(local=local, domain=domain)


if __name__ == '__main__':
    s = Solution()
    print(s.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))