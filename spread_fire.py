import copy

def spread_fire(grid):
    update_grid = copy.deepcopy(grid)
    
    for i in range(len(grid)):  # Use len(grid) to iterate through the grid
        for j in range(len(grid)):  # Use len(grid) to iterate through the grid
            if grid[i][j] == 1:  # If there is a tree
                neighbors = []

                # Check if the cell above exists (i > 0)
                if i > 0:
                    neighbors.append(grid[i-1][j])  # Cell above
                # Check if the cell below exists (i < len(grid) - 1)
                if i < len(grid) - 1:
                    neighbors.append(grid[i+1][j])  # Cell below
                # Check if the cell to the left exists (j > 0)
                if j > 0:
                    neighbors.append(grid[i][j-1])  # Cell to the left
                # Check if the cell to the right exists (j < len(grid) - 1)
                if j < len(grid) - 1:
                    neighbors.append(grid[i][j+1])  # Cell to the right
                
                # If one of the neighbors is fire (2), spread the fire to this tree (1)
                if 2 in neighbors:
                    update_grid[i][j] = 2

    return update_grid
