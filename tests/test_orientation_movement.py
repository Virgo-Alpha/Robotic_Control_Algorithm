import pytest
import sys
sys.path.append('..')
from main import move_robot

def test_move_robot_forward():
    commands = ['F']
    initial_position = (0, 0, 'N')
    final_position = move_robot(commands, initial_position)
    assert final_position == (0, 1, 'N')

def test_move_robot_backward():
    commands = ['B']
    initial_position = (0, 1, 'N')
    final_position = move_robot(commands, initial_position)
    assert final_position == (0, 0, 'N')

def test_move_robot_left():
    commands = ['L']
    initial_position = (0, 0, 'N')
    final_position = move_robot(commands, initial_position)
    assert final_position == (0, 0, 'W')

def test_move_robot_right():
    commands = ['R']
    initial_position = (0, 0, 'N')
    final_position = move_robot(commands, initial_position)
    assert final_position == (0, 0, 'E')
    