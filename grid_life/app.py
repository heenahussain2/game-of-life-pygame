import sys

import pygame
from pygame.locals import *

from . import renderer, state
from .config import BG_COLOR, CELL_SIZE, COLS, FPS, HEIGHT, ROWS, WIDTH


class GameApp:
    def __init__(self) -> None:
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Grid Life Lab")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 24)

        self.grid = state.make_grid(ROWS, COLS)
        self.run_sim = False
        self.running = True
        self.generation = 0
        self.frame_count = 0

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == QUIT:
            self.running = False
        elif event.type == MOUSEBUTTONDOWN:
            row, col = state.pixel_to_cell(event.pos, CELL_SIZE)
            state.set_cell_alive(self.grid, row, col)
        elif event.type == KEYDOWN:
            if event.key == K_c:
                state.clear_grid(self.grid)
                self.generation = 0
                self.frame_count = 0
                self.run_sim = False
            elif event.key == K_r:
                state.randomize_grid(self.grid)
            elif event.key == K_RETURN:
                self.run_sim = True
            elif event.key == K_p:
                self.run_sim = False
            elif event.key == K_s:
                state.save_grid(self.grid)
            elif event.key == K_l:
                self.grid = state.load_saved_grid()

    def update_grid(self) -> None:
        self.frame_count += 1
        if self.run_sim and self.frame_count % FPS == 0:
            self.grid = state.step(self.grid)
            self.generation += 1

    def draw(self) -> None:
        self.screen.fill(BG_COLOR)
        renderer.draw_cells(self.screen, self.grid)
        renderer.draw_grid_lines(self.screen)
        renderer.draw_hud(
            self.screen,
            self.font,
            alive_cells=state.count_alive(self.grid),
            generation=self.generation,
        )

    def run(self) -> None:
        while self.running:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                self.handle_event(event)
            self.update_grid()
            self.draw()
            pygame.display.flip()

        pygame.quit()
        sys.exit()
