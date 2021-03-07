class Solution:
    #40s
    def isMatch(self, s, p):
        def find(s, p):
            for i in range(len(s) - len(p) + 1):
                if all(p[j] in (s[i+j], '?') for j in range(len(p))):
                    return i
            return -1
        parts = p.split('*')
        if len(parts) == 1:
            return len(s) == len(p) and find(s, p) >= 0
        if find(s, parts[0]) != 0:
            return False
        s = s[len(parts.pop(0)):]
        n = len(s) - len(parts[-1])
        if find(s[n:], parts.pop()) != 0:
            return False
        s = s[:n]
        for part in parts:
            index = find(s, part)
            if index < 0:
                return False
            s = s[index + len(part):]
        return True


    #220 ms
    def isMatch(self, s, p):
        length = len(s)
        if len(p) - p.count('*') > length:
            return False
        dp = [True] + [False]*length
        for i in p:
            if i != '*':
                for n in reversed(range(length)):
                    dp[n+1] = dp[n] and (i == s[n] or i == '?')
            else:
                for n in range(1, length+1):
                    dp[n] = dp[n-1] or dp[n]
            dp[0] = dp[0] and i == '*'
        return dp[-1]