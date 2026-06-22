class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row,col=len(board),len(board[0])

        seen = set()

        for r in range(row):
            for c in range(col):
                val = board[r][c]
                if  not val.isdigit():
                    continue
                row_key = f"row_{r}_{val}"
                col_key =  f"col_{c}_{val}"
                box_key = f"box_{r//3}_{c//3}_{val}"

                if row_key in seen or col_key in seen or box_key in seen:
                    return False
                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)
        return True



       