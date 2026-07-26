class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check = set()
        #row
        for i in range(len(board)):
            check = set()
            
            for j in range(len(board)):

                if board[i][j] == ".":
                    continue 

                if board[i][j] in check:
                    return False

                check.add(board[i][j])

        #column
        for i in range(len(board)):
            check = set()
            
            for j in range(len(board)):

                if board[j][i] == ".":
                    continue 

                if board[j][i] in check:
                    return False

                check.add(board[j][i])

        #square
        for i in range(0,9,3):
            
            for j in range(0,9,3):
                check = set()
                for r in range(i,i+3):
                    for c in range(j,j+3):
                        
                        if board[r][c] == ".":
                            continue

                        if board[r][c] in check:
                            return False

                        check.add(board[r][c])
                
        return True



            