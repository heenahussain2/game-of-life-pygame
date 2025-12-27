# Game of Life - Pygame

Interactive Conway's Game of Life built with Pygame. Draw cells with the mouse, start and pause the simulation, and iterate on new rules or visuals in a modular codebase.

## Features
- Click to set live cells; clear or randomize the grid from the keyboard.
- Save and load patterns to `saved_files/life_pattern.json`.
- Configurable window size, FPS, and cell size.
- Modular layout (`grid_life/`) separating config, state logic, rendering, and the app loop for easy experimentation.

## Run the game
- Download and run the Windows executable: [GameOfLife](https://github.com/heenahussain2/game-of-life-pygame/raw/refs/heads/master/dist/GameOfLife.exe) from the project folder or the release you downloaded.

## Controls
- `Mouse click` - Toggle a cell alive.
- `Enter` - Start/Resume simulation.
- `P` - Pause simulation.
- `C` - Clear grid.
- `R` - Randomize grid.
- `S` - Save current pattern.
- `L` - Load saved pattern.

## Project layout
- `main.py` - Entrypoint that launches the app.
- `grid_life/config.py` - Screen, color, and grid constants.
- `grid_life/state.py` - Grid creation, randomization, Game of Life rules, and stepping.
- `grid_life/renderer.py` - Drawing cells, grid lines, and HUD text.
- `grid_life/app.py` - `GameApp` class wiring together events, update loop, and rendering.
- `saved_files/` - Saved pattern file (`life_pattern.json`).
- `experiments/` - Scratch scripts used during development.
- `notes/` - Project notes and logs.

## Extending
- Adjust grid parameters in `grid_life/config.py` (e.g., `CELL_SIZE`, `WIDTH`, `HEIGHT`, `FPS`).
- Tweak behavior in `grid_life/state.py` (e.g., swap in alternate life-like rules or add new neighbor logic).
- Customize visuals in `grid_life/renderer.py` (colors, text, overlays).

