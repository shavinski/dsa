class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool


        first loop, get acces to first row
            have row list, have nums
            have col list, have nums

            second loop, loop through row
                check the first element of each row

                if string not equal to '.' AND string does not exist in list
                    append number to list
                else 
                    return false

                if string not equal to '.' AND string does not exist in list
                    append number to list
                else 
                    return false

        """
        sudokuLength = len(board)

        for x in range(sudokuLength):
            row = []
            col = []

            for y in range(sudokuLength):

                # CHECK ROWS
                if board[x][y] in row and board[x][y] != '.':
                    return False
                row.append(board[x][y])
                   
                # CHECK COLUMNS
                if board[y][x] in col and board[y][x] != '.':
                    return False
                col.append(board[y][x])

        return True
        