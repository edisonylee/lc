from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1. Initialize storage for seen numbers
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        # 2. Iterate through every cell in the 9x9 grid
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                # 3. Skip empty cells
                if val == ".":
                    continue
                # 4. Check if the value already exists in the current Row, Col, or Box
                # Box index is (r // 3, c // 3)
                if (val in rows[r] or 
                    val in cols[c] or   
                    val in boxes[(r // 3, c // 3)]):
                    return False
                # 5. Add the value to our trackers
                rows[r].add(val)
                cols[c].add(val)
                boxes[(r // 3, c // 3)].add(val)
        
        # 6. If we finish the loops without returning False, the board is valid
        return True