# Robotic Control Algorithm

## Overview
This program simulates a robotic algorithm for controlling a two-wheeled differential drive robot in a grid-based environment. The robot is capable of moving forward, backward, turning left, and turning right within a predefined grid.

## Features
- Allows users to input commands via a user interface (UI) to control the robot's movements.
- Displays the final position of the robot after executing the commands.
- Provides a visual representation of the robot's movements within the grid.

## Prerequisites
- Python 3.6 or above

## Installation
1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/Virgo-Alpha/Robotic_Control_Algorithm
    ```

2. Navigate to the project directory:

    ```bash
    cd Robotic_Control_Algorithm
    ```

3. Activate the venv:

    ```bash
    source venv/bin/activate
    ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage
### Using the Tkinter UI (for Tinker version)
1. Run the program using Python:

    ```bash
    python robot_ui.py &
    ```

2. The Tkinter UI window will open, allowing you to input the initial position of the robot (x, y) and its orientation (N, E, S, W). 
3. Use the buttons to enter movement commands (F for forward, B for backward, L for turn left, R for turn right) or manually type the commands in the Commands field.
4. Press Enter or click the movement buttons to execute the commands.
5. The final position of the robot will be displayed, along with a visual representation of its movements within the grid.

## Testing
I have implemented unit tests using pytest in the tests folder

### Running unit tests
2. Navigate to the tests directory:

    ```bash
    cd tests/
    ```

3. Run the command:

    ```bash
    pytest
    ```

3. Sometimes the command above does not work unless you either delete the __pycache__ folder or specify the python files:

    ```bash
    pytest *.py
    ```

## Contributing
Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the [Open Source Licence](LICENSE).
