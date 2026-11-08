from matplotlib import pyplot as plt


class BoardPlot:
    """
    Class for plotting sudoku boards.
    """
        
    def __init__(self, puzzle):
        self.puzzle = puzzle


    def draw(self):
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

        # Add puzzle values
        for row in range(9):
            for col in range(9):
                if self.puzzle[row][col] != 0:
                    self.ax.text(col+0.5, row+0.5, str(self.puzzle[row][col]), ha='center', va='center', fontsize=16)
        
        return self.fig, self.ax

if __name__ == "__main__":
    
    # A valid input sudoku puzzle
    puzzle = [[5,3,0,0,7,0,0,0,0],
              [6,0,0,1,9,5,0,0,0],
              [0,9,8,0,0,0,0,6,0],
              [8,0,0,0,6,0,0,0,3],
              [4,0,0,8,0,3,0,0,1],
              [7,0,0,0,2,0,0,0,6],
              [0,6,0,0,0,0,2,8,0],
              [0,0,0,4,1,9,0,0,5],
              [0,0,0,0,8,0,0,7,9]]


    # Plot puzzle
    fig, ax = BoardPlot(puzzle).draw()
    plt.show() 