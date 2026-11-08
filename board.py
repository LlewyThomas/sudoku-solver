
class Board:
    """
    Represents a Sudoku board.
    """    
        
    def __init__(self, puzzle):
        """
        Initialize the Board object.
        
        Args:
            puzzle (list): 9x9 list of lists representing the sudoku board.
        """

        # Validate puzzle type
        if not isinstance(puzzle, list):
            raise TypeError("Input puzzle must be a list.")
        
        # Validate puzzle dimensions
        if len(puzzle) != 9:
            raise ValueError("Input puzzle must have 9 rows.")
        for row in puzzle:
            if len(row) != 9:
                raise ValueError("Input puzzle must have 9 columns.")
    
        # validate puzzle values
        for row in puzzle:
            for cell in row:
                if not isinstance(cell, int) or cell < 0 or cell > 9:
                    raise ValueError("Each cell must be an integer between 0 and 9 (inclusive).")
    
        self.puzzle = puzzle.deepcopy()