from typing import List
import copy

class Solution:

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        (i,j)=self.getNext(board,0,0)
        self.helper(board,i,j)
        for i in range(0,9):
            for j in range(0,9):
                print(self.res[i][j])
                board[i][j]=self.res[i][j]
        print(self.res)
        print(board)

    def getNext(self, board: List[List[str]], r: int, c: int) -> tuple:
        for i in range(r,9):
            for j in range(0,9):
                if i==r and j>=c and board[i][j]=='.':
                    return (i,j)
                elif i>r and board[i][j]=='.':
                    return (i,j)
        return (-1,-1)
    flag = True
    res = List[List[str]]
    def helper(self, board: List[List[str]], r: int, c: int) -> None:
        if self.flag and r<9 and c <9:
            for i in range(1, 10):
                if self.isOk(board, r, c, i):
                    board[r][c] = str(i)
                    (nr,nc) = self.getNext(board, r, c);
                    if (nr,nc)!=(-1,-1):self.helper(board, nr,nc)
                    else:
                        self.flag=False
                        self.res=copy.deepcopy(board)
                    board[r][c] = '.'




    def isOk(self, board :List[List[str]], r: int, c: int, key: int) -> bool:
        for i in range(0,9):#check row and column
            if (board[r][i]!='.' and board[r][i]==str(key))or(board[i][c]!='.'and board[i][c]==str(key)):
                return False
        rb = int(r/3)*3; cb = int(c/3)*3
        for i in range(rb, rb+3):
            for j in range(cb,cb+3):
                if board[i][j]!='.' and board[i][j]==str(key):
                    return False
        return True


board=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
solution=Solution()
solution.solveSudoku(board)
