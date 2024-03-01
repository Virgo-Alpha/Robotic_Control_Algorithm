import pytest
import sys
sys.path.append('..')
from main import move_robot

def test_move_robot_complex():
    commands = ['F', 'R', 'F', 'L', 'B']
    initial_position = (0, 0, 'N')
    final_position = move_robot(commands, initial_position)
    assert final_position == (1, 0, 'N')

def test_move_robot_past_boundary():
    commands = ['F', 'R', 'F', 'L', 'B', 'B', 'B', 'B', 'B']
    initial_position = (0, 0, 'N')
    final_position = move_robot(commands, initial_position)
    assert final_position == (1, 0, 'N')

def test_move_robot_complex_3():
    commands = ['F', 'R', 'F', 'L', 'B', 'F', 'F', 'F', 'L', 'B', 'B', 'B', 'R', 'F']
    initial_position = (0, 0, 'N')
    final_position = move_robot(commands, initial_position)
    assert final_position == (4, 4, 'N')
