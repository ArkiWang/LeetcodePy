import numpy as np
class Solution:
    def maximalRectangle(self, matrix: [[str]]) -> int:
        width, height = len(matrix), len(matrix[0])
        dp = np.zeros((width, height))
        for i in range
