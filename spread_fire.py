import random
import copy
import matplotlib.pyplot as plt
from IPython.display import display, clear_output

def initialize_forest(grid_size=30, p_tree=0.6):
    """Initialize a grid for the forest fire simulation."""
    grid = []
    for _ in range(grid_size):
        row = [0] * grid_size
        grid.append(row)

    for i in range(grid_size):
        for j in range(grid_size):
            if random.random() < p_tree:
                grid[i][j] = 1  # Place a tree

    grid[grid_size // 2][grid_size // 2] = 2  # Set the center tree on fire
    return grid


def spread_fire(grid, grid_size):
    """Update the forest grid based on fire spreading rules."""
    update_grid = copy.deepcopy(grid)

    for i in range(grid_size):  # Iterate through entire grid, including last row
        for j in range(grid_size):  # Iterate through entire grid, including last column
            if grid[i][j] == 1:  # If there is a tree
                neighbors = []

                # Check if the cell above exists
                if i > 0:
                    neighbors.append(grid[i-1][j])  # Cell above
                # Check if the cell below exists
                if i < grid_size - 1:
                    neighbors.append(grid[i+1][j])  # Cell below
                # Check if the cell to the left exists
                if j > 0:
                    neighbors.append(grid[i][j-1])  # Cell to the left
                # Check if the cell to the right exists
                if j < grid_size - 1:
                    neighbors.append(grid[i][j+1])  # Cell to the right
                
                # If one of the neighbors is fire (2), spread the fire
                if 2 in neighbors:
                    update_grid[i][j] = 2

    return update_grid


# Set up the grid
grid_size = 30
p_tree = 0.6  # Probability that a cell contains a tree

grid = initialize_forest(grid_size, p_tree)

# Run the fire simulation
fig, ax = plt.subplots()
steps = 0
burning_cells_prev = sum([row.count(2) for row in grid])  # Count initial burning cells

# Loop for fire spreading
for i in range(100):  # Max steps to prevent infinite loop
    update_grid = spread_fire(grid, grid_size)
    
    # Count the number of burning cells after the update
    burning_cells_current = sum([row.count(2) for row in update_grid])

    # Stop if no new cells are burning
    if burning_cells_current == burning_cells_prev:
        break

    grid = update_grid
    burning_cells_prev = burning_cells_current
    
    # Display the grid
    ax.imshow(grid, cmap='YlOrRd', vmin=0, vmax=2)
    ax.set_title(f'Step {i}')
    display(fig)
    clear_output(wait=True)
    plt.pause(0.01)
