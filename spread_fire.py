import copy

def spread_fire(grid, grid_size):
    """Update the forest grid based on fire spreading rules."""
    update_grid = copy.deepcopy(grid)

    for i in range(grid_size):  # Iterate over the entire grid (including the last row)
        for j in range(grid_size):  # Iterate over the entire grid (including the last column)
            if grid[i][j] == 1:
                # Check neighboring cells (up, down, left, right) for fire (value 2)
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
