class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        s = logs
        if len(logs)==0:
            return logs

        # print(len(logs))
        end = len(logs)
        i = 0
        while i < end:
            line = logs[i].split()
            if line[-1].isdigit():    # is number
                a = s.pop(i)
                s.append(a)
                end -= 1
            i += 1
        return s


print(Solution().reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))