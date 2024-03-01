import tkinter as tk
from tkinter import OptionMenu, StringVar, messagebox
import sys
sys.path.append('..')
from main import move_robot

def move_forward(event=None):
    commands_entry.insert(tk.END, "F ")
    move_robot_and_display()

def move_backward(event=None):
    commands_entry.insert(tk.END, "B ")
    move_robot_and_display()

def turn_left(event=None):
    commands_entry.insert(tk.END, "L ")
    move_robot_and_display()

def turn_right(event=None):
    commands_entry.insert(tk.END, "R ")
    move_robot_and_display()

def move_robot_and_display():
    try:
        initial_position = (
            int(x_var.get()),
            int(y_var.get()),
            orientation_var.get()
        )
        commands = commands_entry.get().split()
        final_position = move_robot(commands, initial_position)
        final_position_label.config(text=f"Final Position: {final_position}")
        draw_robot(final_position)
    except ValueError:
        messagebox.showerror("Error", "Invalid input for initial position.")

def draw_robot(position):
    canvas.delete("all")  # Clear the canvas
    x, y, orientation = position
    cell_size = 30  # Size of each cell in the grid
    robot_size = 10  # Size of the robot
    arrow_length = 10  # Length of the arrow for orientation

    # Draw grid lines
    for i in range(11):
        canvas.create_line(i * cell_size, 0, i * cell_size, 300)  # Vertical lines
        canvas.create_line(0, i * cell_size, 300, i * cell_size)  # Horizontal lines

    # Draw robot
    robot_x = x * cell_size + cell_size // 2
    robot_y = y * cell_size + cell_size // 2
    if orientation == 'N':
        canvas.create_line(robot_x, robot_y, robot_x, robot_y - robot_size, arrow="last", arrowshape=(10, 15, 5))
    elif orientation == 'E':
        canvas.create_line(robot_x, robot_y, robot_x + robot_size, robot_y, arrow="last", arrowshape=(10, 15, 5))
    elif orientation == 'S':
        canvas.create_line(robot_x, robot_y, robot_x, robot_y + robot_size, arrow="last", arrowshape=(10, 15, 5))
    elif orientation == 'W':
        canvas.create_line(robot_x, robot_y, robot_x - robot_size, robot_y, arrow="last", arrowshape=(10, 15, 5))

def update_initial_position(*args):
    draw_robot((int(x_var.get()), int(y_var.get()), orientation_var.get()))

# Create the main window
root = tk.Tk()
root.title("Robot Control UI")

# Create input fields and labels
tk.Label(root, text="Initial Position (x, y):").grid(row=0, column=0, sticky="w")
x_var = StringVar(root)
x_var.set("0")  # Default x coordinate
x_option_menu = OptionMenu(root, x_var, *range(10), command=update_initial_position)
x_option_menu.grid(row=0, column=1)
y_var = StringVar(root)
y_var.set("0")  # Default y coordinate
y_option_menu = OptionMenu(root, y_var, *range(10), command=update_initial_position)
y_option_menu.grid(row=0, column=2)

# Create buttons for movement
forward_button = tk.Button(root, text="Forward (F)", command=move_forward)
forward_button.grid(row=1, column=0)
backward_button = tk.Button(root, text="Backward (B)", command=move_backward)
backward_button.grid(row=1, column=1)
left_button = tk.Button(root, text="Left (L)", command=turn_left)
left_button.grid(row=1, column=2)
right_button = tk.Button(root, text="Right (R)", command=turn_right)
right_button.grid(row=1, column=3)

tk.Label(root, text="Orientation:").grid(row=2, column=0, sticky="w")
orientation_var = StringVar(root)
orientation_var.set("N")  # Default orientation
orientation_option_menu = OptionMenu(root, orientation_var, "N", "E", "S", "W", command=update_initial_position)
orientation_option_menu.grid(row=2, column=1)

tk.Label(root, text="Commands:").grid(row=3, column=0, sticky="w")
commands_entry = tk.Entry(root)
commands_entry.grid(row=3, column=1)

# Create a label to display the final position
final_position_label = tk.Label(root, text="")
final_position_label.grid(row=4, column=0, columnspan=4)

# Create a canvas to draw the grid and robot
canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.grid(row=5, column=0, columnspan=4)

# Bind arrow key presses to movement functions
root.bind("<Up>", move_forward)
root.bind("<Down>", move_backward)
root.bind("<Left>", turn_left)
root.bind("<Right>", turn_right)

# Draw initial robot position
draw_robot((int(x_var.get()), int(y_var.get()), orientation_var.get()))

# Run the Tkinter event loop
root.mainloop()
