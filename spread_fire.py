import copy


def spread_fire(grid, grid_size):
    update_grid = copy.deepcopy(grid)

    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == 1:
                # Check neighboring cells (up, down, left, right) for fire (value 2)
                neighbors = []
                
                # Check if the cell above exists and is a valid index
                if i > 0:
                    neighbors.append(grid[i-1][j])
                # Check if the cell below exists and is a valid index
                if i < grid_size - 1:
                    neighbors.append(grid[i+1][j])
                # Check if the cell to the left exists and is a valid index
                if j > 0:
                    neighbors.append(grid[i][j-1])
                # Check if the cell to the right exists and is a valid index
                if j < grid_size - 1:
                    neighbors.append(grid[i][j+1])
                
                # If one of the neighbors is fire (2), spread the fire
                if 2 in neighbors:
                    update_grid[i][j] = 2

    return update_grid
