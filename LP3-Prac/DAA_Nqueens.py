from typing import List

def solve_n_queens(n: int) -> List[List[str]]:
    """
    Return all distinct solutions for n-queens.
    Each solution is represented as a list of strings, where 'Q' is a queen and '.' is empty.
    """

    solutions: List[List[str]] = []
    # Track used columns and diagonals for O(1) safety check
    used_cols = set()
    used_diag = set()      # r - c
    used_antidiag = set()  # r + c
    # current placement: queen_positions[row] = col
    queen_positions = [-1] * n

    def place_row(row: int):
        # If row == n, we've placed queens in all rows -> record solution
        if row == n:
            board = []
            for r in range(n):
                row_str = ['.'] * n
                row_str[queen_positions[r]] = 'Q'
                board.append(''.join(row_str))
            solutions.append(board)
            return

        # Try each column in this row
        for col in range(n):
            d = row - col
            ad = row + col
            if col in used_cols or d in used_diag or ad in used_antidiag:
                continue  # Not safe, skip

            # Place queen
            used_cols.add(col)
            used_diag.add(d)
            used_antidiag.add(ad)
            queen_positions[row] = col

            # Recurse to next row
            place_row(row + 1)

            # Backtrack (remove queen)
            used_cols.remove(col)
            used_diag.remove(d)
            used_antidiag.remove(ad)
            queen_positions[row] = -1

    place_row(0)
    return solutions


# Example usage:
if __name__ == "__main__":
    n = int(input("Enter the number of queens: "))
    sols = solve_n_queens(n)
    print(f"Found {len(sols)} solutions for n = {n}.\n")
    # print first solution nicely
    if sols:
        print("One solution:")
        for line in sols[0]:
            print(line)
