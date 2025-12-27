import pygame

from .config import (
    ALIVE_CELL_COLOR,
    BLACK,
    CELL_SIZE,
    GRID_COLOR,
    HEIGHT,
    TEXT_COLOR,
    WIDTH,
)


def draw_grid_lines(surface: pygame.Surface, color=GRID_COLOR) -> None:
    """Draw vertical and horizontal grid lines."""
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(surface, color, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(surface, color, (0, y), (WIDTH, y))


def draw_cells(surface: pygame.Surface, grid) -> None:
    """Render alive cells as filled rectangles."""
    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            if cell:
                rect = pygame.Rect(
                    col_idx * CELL_SIZE, row_idx * CELL_SIZE, CELL_SIZE, CELL_SIZE
                )
                pygame.draw.rect(surface, ALIVE_CELL_COLOR, rect)


def draw_hud(
    surface: pygame.Surface, font: pygame.font.Font, alive_cells: int, generation: int
) -> None:
    """Render overlay text showing population and generation."""
    pop_surface = font.render(f"Population: {alive_cells}", True, TEXT_COLOR, None)
    gen_surface = font.render(f"Generation: {generation}", True, TEXT_COLOR, None)
    surface.blit(pop_surface, (10, 10))
    surface.blit(gen_surface, (10, 30))

