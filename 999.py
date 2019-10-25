class Solution:
    def numRookCaptures(self, board) -> int:
        """
               :type board: List[List[str]]
               :rtype: int
               """

        # counter
        count = 0

        # rook location
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'R':
                    rookRow, rookCol = r, c

        # left
        r = rookRow - 1
        while r >= 0:
            tile = board[r][rookCol]
            if tile == 'p' or tile == 'B':
                count += 1 if tile == 'p' else 0
                break
            r -= 1

        # right
        r = rookRow + 1
        while r < len(board):
            tile = board[r][rookCol]
            if tile == 'p' or tile == 'B':
                count += 1 if tile == 'p' else 0
                break
            r += 1

        # up
        c = rookCol - 1
        while c >= 0:
            tile = board[rookRow][c]
            if tile == 'p' or tile == 'B':
                count += 1 if tile == 'p' else 0
                break
            c -= 1

        # up
        c = rookCol + 1
        while c < len(board[0]):
            tile = board[rookRow][c]
            if tile == 'p' or tile == 'B':
                count += 1 if tile == 'p' else 0
                break
            c += 1

        return count

