import copy
import json
import os
import random
import sys

from typing import Iterable, Tuple

from .config import COLS, ROWS

Grid = list[list[int]]


def make_grid(rows: int = ROWS, cols: int = COLS) -> Grid:
    """Return a rows x cols grid filled with 0s."""
    return [[0 for _ in range(cols)] for _ in range(rows)]


def clear_grid(grid: Grid) -> None:
    """Set every cell to 0."""
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            grid[row][col] = 0


def randomize_grid(grid: Grid) -> None:
    """Randomly toggle cells to alive."""
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            grid[row][col] = 1 if random.randint(0, len(grid[0]) - 1) == col else 0


def set_cell_alive(grid: Grid, row: int, col: int) -> None:
    """Mark a single cell as alive if the coordinate is valid."""
    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        grid[row][col] = 1


def pixel_to_cell(pos: Tuple[int, int], cell_size: int) -> Tuple[int, int]:
    """Convert a pixel coordinate to a cell coordinate."""
    x, y = pos
    return y // cell_size, x // cell_size


def count_alive(grid: Iterable[Iterable[int]]) -> int:
    return sum(map(sum, grid))


def _apply_life_rules(alive_neighbors: int, grid: Grid, row: int, col: int) -> int:
    if grid[row][col] == 1 and alive_neighbors in (2, 3):
        return 1
    if grid[row][col] == 0 and alive_neighbors == 3:
        return 1
    return 0


def step(grid: Grid) -> Grid:
    """Run a single Game of Life tick."""
    new_grid = copy.deepcopy(grid)
    rows = len(grid)
    cols = len(grid[0])
    adjacent_offsets = [
        (0, -1),
        (0, 1),
        (-1, 0),
        (1, 0),
        (-1, -1),
        (1, 1),
        (-1, 1),
        (1, -1),
    ]

    for row in range(rows):
        for col in range(cols):
            alive_neighbors = 0
            for d_row, d_col in adjacent_offsets:
                n_row, n_col = row + d_row, col + d_col
                if 0 <= n_row < rows and 0 <= n_col < cols:
                    alive_neighbors += grid[n_row][n_col]
            new_grid[row][col] = _apply_life_rules(alive_neighbors, grid, row, col)
    return new_grid


def get_saved_file_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def save_grid(grid: Grid) -> None:
    """Save the current pattern"""
    print("Saved the pattern\n", grid)
    file_path = get_saved_file_path("saved_files/life_pattern.json")
    with open(file_path, "w", encoding="utf-8") as wf:
        json.dump(grid, wf)


def load_saved_grid() -> Grid:
    """Load the saved grid data"""
    file_path = get_saved_file_path("saved_files/life_pattern.json")
    with open(file_path, "r", encoding="utf-8") as rf:
        saved_grid = json.load(rf)
    print("Loading the pattern\n", saved_grid)
    return saved_grid
