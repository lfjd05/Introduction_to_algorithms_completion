class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        maxint = 0x7fffffff
        minint = 0x80000000
        max = 0x80000000
        ans = 0
        flag = False
        st = 0
        while st < len(str) and str[st] == ' ':
            st += 1
        if st < len(str) and str[st] == '+':
            st += 1
        else:
            if st < len(str) and str[st] == '-':
                flag = True
                st += 1
        for i in range(st, len(str)):
            try:
                if 9 >= int(str[i]) >= 0:
                    ans = ans * 10 + int(str[i])

                    if ans > maxint:
                        ans = max
            except ValueError:
                break

        if flag:
            ans = -ans
            if ans < -minint:
                ans = -minint
        if ans > maxint:
            ans = maxint
        return ans


# print int(3.14159)
# a = " 42"
# a = "4193 with words"
# a = "words and 987"
# a = "3.14159"
# a = '+100'
a = "+-2"
print Solution().myAtoi(a)
