# %%
# Install pygame if missing (Jupyter magic)
%pip install pygame

from secrets import choice
import sys
try:
    import pygame
    from pygame import sprite
    from pygame.math import Vector2
except ModuleNotFoundError:
    # Try reinstalling and invalidating import caches; you may need to restart the kernel
    %pip install pygame --upgrade
    import importlib
    importlib.invalidate_caches()
    try:
        import pygame
        from pygame import sprite
        from pygame.math import Vector2
    except ModuleNotFoundError as e:
        raise ModuleNotFoundError(
            "pygame could not be imported even after installation. "
            "If you're in Jupyter, please restart the kernel and run this cell again."
        ) from e

# --- constants ---
CELL_SIZE = 24
COLUMNS = 10
ROWS = 20
PADDING = 10
LIGHT_COLOR = (200, 200, 200)
GRAY = (30, 30, 30)
GAME_WIDTH = COLUMNS * CELL_SIZE
GAME_HEIGHT = ROWS * CELL_SIZE
WINDOW_WIDTH = GAME_WIDTH + PADDING * 2
WINDOW_HEIGHT = GAME_HEIGHT + PADDING * 2
UPDATE_START_SPEED = 1000  # milliseconds
MOVE_WAIT_TIME = 150  # milliseconds

# --- small Timer helper compatible with the original intent ---
class Timer:
    def __init__(self, interval, repeat, callback):
        self.interval = int(interval)
        self.repeat = bool(repeat)
        self.callback = callback
        self.active = False
        self._last = pygame.time.get_ticks()

    def activate(self):
        self.active = True
        self._last = pygame.time.get_ticks()

    def update(self):
        if not self.active:
            return
        now = pygame.time.get_ticks()
        if now - self._last >= self.interval:
            self._last = now
            if callable(self.callback):
                self.callback()
            if not self.repeat:
                self.active = False

# --- Block sprite ---
class Block(sprite.Sprite):
    def __init__(self, group, pos, color):
        super().__init__(group)
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill(color)
        self.pos = Vector2(pos)
        self.rect = self.image.get_rect(topleft=(int(self.pos.x * CELL_SIZE), int(self.pos.y * CELL_SIZE)))

    def horizontal_colide(self, x):
        return not (0 <= x < COLUMNS)

    def update(self):
        self.rect.x = int(self.pos.x * CELL_SIZE)
        self.rect.y = int(self.pos.y * CELL_SIZE)

# --- tetromino definitions and class ---
TETROMINOS = {
    'L': {'shape': [Vector2(0, 0), Vector2(0, 1), Vector2(0, 2), Vector2(1, 2)], 'color': (255, 165, 0)},
}

class Tetromino:
    def __init__(self, group, pos=(3, 0), shape='L'):
        self.group = group
        self.shape = shape
        template = TETROMINOS[self.shape]
        self.block_positions = template['shape']
        self.color = template['color']
        self.blocks = [Block(self.group, (pos[0] + int(p.x), pos[1] + int(p.y)), self.color) for p in self.block_positions]
self.create_new_tetromino = create_new_tetromino
def next_move_horizontal(self, amount):
        return any(b.horizontal_colide(int(b.pos.x + amount)) for b in self.blocks)

    def move_horizontal(self, amount):
        if not self.next_move_horizontal(amount):
            for b in self.blocks:
                b.pos.x += amount

    def next_move_vertical(self, amount):
        return any(int(b.pos.y + amount) >= ROWS for b in self.blocks)

    def move_down(self):
        if not self.next_move_vertical(1):
            for b in self.blocks:
                b.pos.y += 1
else:
self.create_new_tetromino()
# --- Game class ---
class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Pygame Window")
        self.surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.lines_surface = pygame.Surface(self.surface.get_size(), flags=pygame.SRCALPHA)
        self.sprites = sprite.Group()
        self.tetromino = Tetromino(self.sprites, pos=(3, 0))
        self.clear_lines_surface()
    def create_new_tetromino(self):
        #tetromino
        self.field_data = [[0 for x in range(COLUMNS)] for y in range(ROWS)]
        for row in self.field_data:
            print(row) vccx v
        self.tetromino = Tetromino(choice(list(TETROMINOS.keys())), self.sprites, self_create_new_tetromino)













        self.timers = {
            'vertical_move': Timer(UPDATE_START_SPEED, True, self.move_down),
            'horizontal_move': Timer(MOVE_WAIT_TIME, True, lambda: None)
        }
        self.timers['vertical_move'].activate()

        self.clock = pygame.time.Clock()

    def draw_border(self):
        border_rect = pygame.Rect(PADDING, PADDING, self.surface.get_width(), self.surface.get_height())
        pygame.draw.rect(self.display_surface, LIGHT_COLOR, border_rect, 1)

    def clear_lines_surface(self):
        self.lines_surface.fill((0, 0, 0, 0))

    def draw_grid(self):
        # draw grid onto the transparent lines surface, then blit onto main surface
        self.clear_lines_surface()
        for col in range(COLUMNS):
            x = col * CELL_SIZE
            pygame.draw.line(self.lines_surface, LIGHT_COLOR, (x, 0), (x, self.surface.get_height()), 1)
        for row in range(ROWS):
            y = row * CELL_SIZE
            pygame.draw.line(self.lines_surface, LIGHT_COLOR, (0, y), (self.surface.get_width(), y), 1)
        self.surface.blit(self.lines_surface, (0, 0))

    def input(self):
        keys = pygame.key.get_pressed()
        if not self.timers['horizontal_move'].active:
            if keys[pygame.K_LEFT]:
                self.tetromino.move_horizontal(-1)
                self.timers['horizontal_move'].activate()
            if keys[pygame.K_RIGHT]:
                self.tetromino.move_horizontal(1)
                self.timers['horizontal_move'].activate()

    def move_down(self):
        self.tetromino.move_down()

    def update(self, dt: float = 0):
        for timer in self.timers.values():
            timer.update()
        self.sprites.update()

    def run(self):
        running = True
        while running:
            dt = self.clock.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.input()
            self.update(dt)
            self.surface.fill(GRAY)
            self.sprites.draw(self.surface)
            self.draw_grid()
            self.draw_border()
            self.display_surface.fill((0, 0, 0))
            self.display_surface.blit(self.surface, (PADDING, PADDING))
            pygame.display.flip()
        pygame.quit()

# run interactively when cell is executed
if __name__ == '__main__':
    Game().run()

# %% [markdown]
# 


