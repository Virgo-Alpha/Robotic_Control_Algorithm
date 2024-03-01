def move_robot(commands, initial_position):
    # Define grid dimensions
    grid_width = 10
    grid_height = 10
    
    # Unpack initial position tuple
    x, y, orientation = initial_position
    
    # Define orientation changes for left and right turns
    orientation_changes = {
        'N': {'L': 'W', 'R': 'E'},
        'E': {'L': 'N', 'R': 'S'},
        'S': {'L': 'E', 'R': 'W'},
        'W': {'L': 'S', 'R': 'N'}
    }
    
    # Define movement changes based on orientation
    movement_changes = {
        'N': (0, 1),
        'E': (1, 0),
        'S': (0, -1),
        'W': (-1, 0)
    }
    
    # Iterate through commands
    for command in commands:
        if command == 'F':
            dx, dy = movement_changes[orientation]
            x += dx
            y += dy
            # Check boundary conditions
            x = max(0, min(x, grid_width - 1))
            y = max(0, min(y, grid_height - 1))
        elif command == 'B':
            dx, dy = movement_changes[orientation]
            x -= dx  
            y -= dy 
            # Check boundary conditions
            x = max(0, min(x, grid_width - 1))
            y = max(0, min(y, grid_height - 1))
        elif command in ['L', 'R']:
            orientation = orientation_changes[orientation][command]
    
    # Return final position
    return (x, y, orientation)

# Example usage:
commands = ['F', 'R', 'F', 'L', 'B']  # Sample commands
initial_position = (0, 0, 'N')  # Sample initial position
final_position = move_robot(commands, initial_position)
print("Final Position:", final_position) # Output: (1, 1, 'N')
