import pygame
import random
import sys


# 스네이크 게임 만들기 
pygame.init()

# 화면 설정
WIDTH, HEIGHT = 600, 600
CELL = 20
COLS = WIDTH // CELL
ROWS = HEIGHT // CELL

WHITE  = (255, 255, 255)
BLACK  = (0,   0,   0)
GREEN  = (50,  200, 50)
DGREEN = (30,  140, 30)
RED    = (220, 50,  50)
GRAY   = (40,  40,  40)
YELLOW = (255, 220, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
font_big  = pygame.font.SysFont("consolas", 48, bold=True)
font_small = pygame.font.SysFont("consolas", 24)


def draw_grid():
    for x in range(0, WIDTH, CELL):
        pygame.draw.line(screen, (30, 30, 30), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL):
        pygame.draw.line(screen, (30, 30, 30), (0, y), (WIDTH, y))


def draw_snake(snake):
    for i, (x, y) in enumerate(snake):
        color = GREEN if i > 0 else DGREEN
        rect = pygame.Rect(x * CELL + 1, y * CELL + 1, CELL - 2, CELL - 2)
        pygame.draw.rect(screen, color, rect, border_radius=4)
        # 머리에 눈 표시
        if i == 0:
            pygame.draw.circle(screen, WHITE,
                               (x * CELL + CELL // 3, y * CELL + CELL // 3), 3)
            pygame.draw.circle(screen, WHITE,
                               (x * CELL + 2 * CELL // 3, y * CELL + CELL // 3), 3)


def draw_food(fx, fy):
    rect = pygame.Rect(fx * CELL + 2, fy * CELL + 2, CELL - 4, CELL - 4)
    pygame.draw.ellipse(screen, RED, rect)
    pygame.draw.ellipse(screen, YELLOW, rect.inflate(-6, -6))


def spawn_food(snake):
    while True:
        pos = (random.randint(0, COLS - 1), random.randint(0, ROWS - 1))
        if pos not in snake:
            return pos


def show_screen(title, subtitle):
    screen.fill(GRAY)
    draw_grid()
    t = font_big.render(title, True, GREEN)
    s = font_small.render(subtitle, True, WHITE)
    screen.blit(t, t.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30)))
    screen.blit(s, s.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30)))
    pygame.display.flip()
    wait_key()


def wait_key():
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if e.type == pygame.KEYDOWN:
                return


def game_loop():
    snake = [(COLS // 2, ROWS // 2)]
    direction = (1, 0)
    next_dir = direction
    food = spawn_food(snake)
    score = 0
    speed = 10

    while True:
        clock.tick(speed)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key in (pygame.K_UP,    pygame.K_w) and direction != (0,  1):
                    next_dir = (0, -1)
                elif e.key in (pygame.K_DOWN,  pygame.K_s) and direction != (0, -1):
                    next_dir = (0,  1)
                elif e.key in (pygame.K_LEFT,  pygame.K_a) and direction != (1,  0):
                    next_dir = (-1, 0)
                elif e.key in (pygame.K_RIGHT, pygame.K_d) and direction != (-1, 0):
                    next_dir = (1,  0)
                elif e.key == pygame.K_ESCAPE:
                    return score

        direction = next_dir
        hx, hy = snake[0]
        nx, ny = hx + direction[0], hy + direction[1]

        # 벽 충돌
        if not (0 <= nx < COLS and 0 <= ny < ROWS):
            return score
        # 자기 몸 충돌
        if (nx, ny) in snake:
            return score

        snake.insert(0, (nx, ny))

        if (nx, ny) == food:
            score += 10
            food = spawn_food(snake)
            speed = 10 + score // 50  # 점수 오를수록 빨라짐
        else:
            snake.pop()

        # 그리기
        screen.fill(GRAY)
        draw_grid()
        draw_food(*food)
        draw_snake(snake)

        score_surf = font_small.render(f"Score: {score}", True, WHITE)
        screen.blit(score_surf, (8, 8))
        pygame.display.flip()

    return score


def main():
    show_screen("SNAKE", "Press any key to start")

    while True:
        final = game_loop()

        screen.fill(GRAY)
        draw_grid()
        over = font_big.render("GAME OVER", True, RED)
        sc   = font_small.render(f"Score: {final}", True, YELLOW)
        hint = font_small.render("Press any key to retry  |  ESC to quit", True, WHITE)
        screen.blit(over, over.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50)))
        screen.blit(sc,   sc.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 10)))
        screen.blit(hint, hint.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 55)))
        pygame.display.flip()

        # 재시작 또는 종료 선택
        waiting = True
        while waiting:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit(); sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        pygame.quit(); sys.exit()
                    waiting = False


if __name__ == "__main__":
    main()
