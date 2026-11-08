from matplotlib import pyplot as plt


class BoardPlot:
    """
    Class for plotting sudoku boards.
    """

    def __init__(self, puzzle):
        """
        Initialize the BoardPlot object.
        
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
                
            # Each value must be an integer between 0 and 9 (inclusive)                
            for value in row:
                if not isinstance(value, int) or value < 0 or value > 9:
                    raise ValueError("Each value must be an integer between 0 and 9 (inclusive).")

        # Store puzzle
        self.puzzle = puzzle


    def plot_empty_board(self):
        """
        Plot the empty puzzle with grid lines.
        """
        # Create figure and axis
        self.fig, self.ax = plt.subplots()

        # Plot lines
        for i in range(10):
            # Draw horizontal lines, with thicker lines every 3rd line
            self.ax.axhline(i, color='black', linewidth=2 if i % 3 == 0 else 1, clip_on=False)
            # Draw vertical lines, with thicker lines every 3rd line
            self.ax.axvline(i, color='black', linewidth=2 if i % 3 == 0 else 1, clip_on=False)

        self.ax.set_xlim(0, 9)
        self.ax.set_ylim(9, 0) # Invert y-axis, so (0,0) is at the top left

        self.ax.set_aspect('equal')

        # Remove ticks
        self.ax.set_xticks([])
        self.ax.set_yticks([])

        # Remove label
        self.ax.set_xlabel('')
        self.ax.set_ylabel('')
        
        return self.fig, self.ax


if __name__ == "__main__":
    
    # Plot empty puzzle
    fig, ax = BoardPlot([[0]*9 for _ in range(9)]).plot_empty_board()
    plt.show() 