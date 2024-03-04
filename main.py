# Improvements:
# TODO: Use OOP
# ! the functionality for moving backwards and forwards was unfortunately inverted.

def move_robot(commands, initial_position):
    # Define grid dimensions
    grid_width = 10
    grid_height = 10

    # validate the input
    if not isinstance(commands, list):
        raise ValueError("Commands should be a list of strings.")
    
    if not all(isinstance(command, str) for command in commands):
        raise ValueError("Commands should be a list of strings.")
    
    if not isinstance(initial_position, tuple):
        raise ValueError("Initial position should be a tuple.")
    
    if len(initial_position) != 3:
        raise ValueError("Initial position should be a tuple of 3 elements.")
    
    # Unpack initial position tuple
    x, y, orientation = initial_position

    # Validate initial position
    if not isinstance(x, int) or not isinstance(y, int):
        raise ValueError("Initial position coordinates should be integers.")
    
    if not (0 <= x < grid_width) or not (0 <= y < grid_height):
        raise ValueError("Initial position coordinates should be within the grid.")
    
    if orientation not in ['N', 'E', 'S', 'W']:
        raise ValueError("Orientation should be one of 'N', 'E', 'S', 'W'.")
    
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
            # Check boundary conditions to be less than grid width and height (10, 10)
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
