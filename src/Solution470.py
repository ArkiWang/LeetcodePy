def rand7():
    pass

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            row = rand7()
            col = rand7()
            idx = col + 7 * (row - 1)
            if idx <= 40:
                break
        return (idx - 1)%10 + 1

