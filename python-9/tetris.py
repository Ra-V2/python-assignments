import os
import pygame as pg
import random as rd

# Constants
GRID_SIZE = 30
GRID_WIDTH, GRID_HEIGHT = 10, 20
PADDING = 10
WIDTH, HEIGHT = GRID_WIDTH * GRID_SIZE, GRID_HEIGHT * GRID_SIZE
NEXT_SHAPE_WIDTH = 6 * GRID_SIZE
WINDOW_HEIGHT = HEIGHT + 2 * PADDING
WINDOW_WIDTH = WIDTH + NEXT_SHAPE_WIDTH + 3 * PADDING
INITIAL_FPS = 45
DROP_SPEED_INCREASE_INTERVAL = 4
DROP_SPEED_INCREASE_AMOUNT = 1
AUDIO_ON = True

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
GRAY = (128, 128, 128)

# Shapes
I = [[0, 0, 0, 0],
    [1, 1, 1, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0]]

J = [[1, 0, 0],
    [1, 1, 1],
    [0, 0, 0]]

L = [[0, 0, 1],
    [1, 1, 1],
    [0, 0, 0]]

O = [[1, 1],
    [1, 1]]

S = [[0, 1, 1],
    [1, 1, 0],
    [0, 0, 0]]

T = [[0, 1, 0],
    [1, 1, 1],
    [0, 0, 0]]

Z = [[1, 1, 0],
    [0, 1, 1],
    [0, 0, 0]]

SHAPES = [I, J, L, O, S, T, Z]

# Functions

def draw_grid(surface):
    for x in range(PADDING, WIDTH + PADDING + GRID_SIZE, GRID_SIZE):
        pg.draw.line(surface, GRAY, (x, PADDING), (x, HEIGHT + PADDING))
    for y in range(PADDING, HEIGHT + PADDING + GRID_SIZE, GRID_SIZE):
        pg.draw.line(surface, GRAY, (PADDING, y), (WIDTH + PADDING, y))

def draw_shape(surface, shape, x, y, color):
    for i in range(len(shape)):
        for j in range(len(shape[i])):
            if shape[i][j]:
                rect = (x + j * GRID_SIZE, y + i * GRID_SIZE, GRID_SIZE, GRID_SIZE)
                pg.draw.rect(surface, color, rect)
                pg.draw.rect(surface, BLACK, rect, 1)

def check_collision(grid, shape, x, y):
    for i in range(len(shape)):
        for j in range(len(shape[i])):
            if shape[i][j]:
                if x + j < 0 or x + j >= GRID_WIDTH or y + i >= GRID_HEIGHT:
                    return True
                if grid[y + i][x + j]:
                    return True
    return False

def merge_grid(surface, grid, shape, x, y, color):
    for i in range(len(shape)):
        for j in range(len(shape[i])):
            if shape[i][j]:
                grid[y + i][x + j] = color
                rect = ((x + j) * GRID_SIZE + PADDING, (y + i) * GRID_SIZE + PADDING, GRID_SIZE, GRID_SIZE)
                pg.draw.rect(surface, color, rect)
                pg.draw.rect(surface, BLACK, rect, 1)

def check_line(grid, line_clear_sound = None):
    lines = 0
    for i in range(len(grid)):
        if all(grid[i]):
            grid.pop(i)
            grid.insert(0, [0] * GRID_WIDTH)
            lines += 1
            if(line_clear_sound):
                line_clear_sound.play()
    return lines

def new_shape(last_shape=None):
    shape = rd.choice(SHAPES)
    while shape == last_shape:
        shape = rd.choice(SHAPES)
    return shape

def draw_score(surface, score):
    font = pg.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH + NEXT_SHAPE_WIDTH // 2 + 2 * PADDING, PADDING + 20))
    surface.blit(text, text_rect)

def draw_next_shape_label(surface):
    font = pg.font.Font(None, 36)
    text = font.render("Next:", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH + NEXT_SHAPE_WIDTH / 2.8, PADDING + 60))
    surface.blit(text, text_rect)

def draw_next_shape(surface, shape, color):
    draw_next_shape_label(surface)
    x_offset = WIDTH + PADDING * 2 + NEXT_SHAPE_WIDTH // 4 + 60
    y_offset = PADDING + 45 
    for i in range(len(shape)):
        for j in range(len(shape[i])):
            if shape[i][j]:
                rect = (x_offset + j * GRID_SIZE // 2, y_offset + i * GRID_SIZE // 2, GRID_SIZE // 2, GRID_SIZE // 2)
                pg.draw.rect(surface, color, rect)
                pg.draw.rect(surface, BLACK, rect, 1)

def load_sounds_and_music(path):
    global AUDIO_ON
    if AUDIO_ON:
        try:
            music_path = os.path.join(path, "assets", "background_music.mp3")
            pg.mixer.music.load(music_path)
            pg.mixer.music.play(-1)
            line_clear_sound_path = os.path.abspath(os.path.join(path, "assets", "clear.mp3"))
            return pg.mixer.Sound(line_clear_sound_path)
        except pg.error:
            print(f"Unable to load music at {path}")
            return None
    return None

def toggle_audio(screen, button_rect, font):
    global AUDIO_ON
    AUDIO_ON = not AUDIO_ON
    button_text = "Audio: ON" if AUDIO_ON else "Audio: OFF"
    button_color = GREEN if AUDIO_ON else RED
    pg.draw.rect(screen, button_color, button_rect)
    text = font.render(button_text, True, WHITE)
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)
    pg.display.flip()

def main():
    pg.init()
    screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pg.display.set_caption("Tetris")
    clock = pg.time.Clock()

    display_start_screen(screen)

    grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
    shape = new_shape()
    next_shape = new_shape(shape)
    x, y = GRID_WIDTH // 2 - len(shape[0]) // 2, 0
    color = rd.choice([RED, GREEN, BLUE, CYAN, MAGENTA, YELLOW, ORANGE])
    next_color = rd.choice([RED, GREEN, BLUE, CYAN, MAGENTA, YELLOW, ORANGE])
    score = 0
    total_lines_cleared = 0
    fps = INITIAL_FPS
    drop_speed = 1

    drop_delay = 0
    rotation_delay = 0
    move_delay = 0

    project_folder = os.path.dirname(__file__)
    line_clear_sound = load_sounds_and_music(project_folder)

    running = True
    while running:
        screen.fill(BLACK)
        draw_grid(screen)
        for i in range(GRID_HEIGHT):
            for j in range(GRID_WIDTH):
                if grid[i][j]:
                    pg.draw.rect(screen, grid[i][j], (j * GRID_SIZE + PADDING, i * GRID_SIZE + PADDING, GRID_SIZE, GRID_SIZE))
                    pg.draw.rect(screen, BLACK, (j * GRID_SIZE + PADDING, i * GRID_SIZE + PADDING, GRID_SIZE, GRID_SIZE), 1)
        draw_shape(screen, shape, x * GRID_SIZE + PADDING, y * GRID_SIZE + PADDING, color)
        draw_score(screen, score)
        draw_next_shape(screen, next_shape, next_color)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        keys = pg.key.get_pressed()
        move_delay += 1
        if move_delay >= fps // 10:
            if keys[pg.K_LEFT]:
                if not check_collision(grid, shape, x - 1, y):
                    x -= 1
            if keys[pg.K_RIGHT]:
                if not check_collision(grid, shape, x + 1, y):
                    x += 1
            move_delay = 0

        if keys[pg.K_DOWN]:
            if not check_collision(grid, shape, x, y + 1):
                y += 1

        rotation_delay += 1
        if keys[pg.K_UP] and rotation_delay >= fps // 2:
            rotated_shape = list(zip(*reversed(shape)))
            if not check_collision(grid, rotated_shape, x, y):
                shape = rotated_shape
            rotation_delay = 0

        drop_delay += drop_speed
        if drop_delay >= fps:
            if not check_collision(grid, shape, x, y + 1):
                y += 1
            else:
                merge_grid(screen, grid, shape, x, y, color)
                lines = check_line(grid, line_clear_sound)
                if lines:
                    score += lines * 100
                    total_lines_cleared += lines
                    if total_lines_cleared % DROP_SPEED_INCREASE_INTERVAL == 0:
                        drop_speed += DROP_SPEED_INCREASE_AMOUNT
                shape = next_shape
                next_shape = new_shape(shape)
                x, y = GRID_WIDTH // 2 - len(shape[0]) // 2, 0
                color = next_color
                next_color = rd.choice([RED, GREEN, BLUE, CYAN, MAGENTA, YELLOW, ORANGE])
                if check_collision(grid, shape, x, y):
                    display_end_screen(screen, score)
                    running = False
            drop_delay = 0

        pg.display.flip()
        clock.tick(fps)

    pg.quit()

def display_end_screen(screen, score):
    pg.mixer.music.stop()
    screen.fill(BLACK)
    font = pg.font.Font(None, 74)
    text = font.render("Game Over", True, RED)
    text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))
    screen.blit(text, text_rect)

    font = pg.font.Font(None, 36)
    score_text = font.render(f"Final Score: {score}", True, WHITE)
    score_rect = score_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 20))
    screen.blit(score_text, score_rect)

    pg.display.flip()
    pg.time.wait(3000)

def display_start_screen(screen):
    screen.fill(BLACK)
    font = pg.font.Font(None, 74)
    text = font.render("TETRIS", True, WHITE)
    shadow = font.render("TETRIS", True, GRAY)
    shadow_rect = shadow.get_rect(center=(WINDOW_WIDTH // 2 + 5, WINDOW_HEIGHT // 2 - 100))
    screen.blit(shadow, shadow_rect)
    text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 95))
    screen.blit(text, text_rect)

    controls_text = [
        "Controls:",
        "Arrow keys to move",
        "Up arrow to rotate",
        "Down arrow to drop faster",
        " "
    ]

    font = pg.font.Font(None, 28)
    for i, line in enumerate(controls_text):
        text = font.render(line, True, WHITE)
        shadow = font.render(line, True, GRAY)
        shadow_rect = shadow.get_rect(center=(WINDOW_WIDTH // 2 + 2, WINDOW_HEIGHT // 2 + 52 + i * 30))
        text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50 + i * 30))
        screen.blit(shadow, shadow_rect)
        screen.blit(text, text_rect)

    text = font.render("Press any key to start", True, WHITE)
    shadow = font.render("Press any key to start", True, GRAY)
    shadow_rect = shadow.get_rect(center=(WINDOW_WIDTH // 2 + 2, WINDOW_HEIGHT // 2 + 52 + len(controls_text) * 36))
    text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50 + len(controls_text) * 36))
    screen.blit(shadow, shadow_rect)
    screen.blit(text, text_rect)

    button_rect = pg.Rect(WINDOW_WIDTH - 110, 10, 100, 50)
    font = pg.font.Font(None, 22)
    toggle_audio(screen, button_rect, font)

    pg.display.flip()
    waiting = True
    while waiting:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                waiting = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    toggle_audio(screen, button_rect, font)

    screen.fill(BLACK)

    pg.display.flip()
    pg.time.wait(1000)


if __name__ == "__main__":
    main()