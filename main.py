#.\.venv\Scripts\Activate.ps1
import pygame
import pprint
import random

WHITE = (200, 200, 200)
BLACK = (10, 10, 10)
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
CELL_SIZE = SCREEN_WIDTH//15
snake = [[7, 7]]
move_delay = 250   # milliseconds between moves


def create_board():
    game_board = {}
    for x in range(1, 16):
        for y in range(1, 16):
            game_board[x, y] = " "
    return game_board


# print(pprint.pprint(game_board))

def draw_board(screen, apple_x, apple_y, apple_rect):
    for x in range(0, SCREEN_WIDTH, CELL_SIZE):
        for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            
            if x == apple_x * CELL_SIZE and y == apple_y * CELL_SIZE:
                pygame.draw.rect(screen, BLACK, apple_rect)
            else:
                pygame.draw.rect(screen, WHITE, rect, 1)

def main():

    # pygame setup
    pygame.init()

    pygame.display.set_caption("Snake Game")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True


    direction = ""

    apple_x = random.randint(0, 14)
    apple_y = random.randint(0, 14)

    # If apple in player position set to default position
    if apple_x == 7 and apple_y == 7:
        apple_x = 2
        apple_y = 2

    last_move_time = pygame.time.get_ticks()
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s and direction != "UP":
                    direction = "DOWN"
                elif event.key == pygame.K_w and direction != "DOWN":
                    direction = "UP"
                elif event.key == pygame.K_a and direction != "RIGHT":
                    direction = "LEFT"
                elif event.key == pygame.K_d and direction != "LEFT":
                    direction = "RIGHT"     


        # fill the screen with a color to wipe away anything from last frame
        screen.fill("lime")
 
        # RENDER YOUR GAME HERE

        apple_rect = pygame.Rect(apple_x * CELL_SIZE + 10, apple_y * CELL_SIZE + 10, 40, 40)

        head_x, head_y = snake[0]
        tail_x, tail_y = snake[-1]
 

        draw_board(screen, apple_x, apple_y, apple_rect)

        # Drawing snake
        for sx, sy in snake:
            seg_rect = pygame.Rect(sx * CELL_SIZE + 10, sy * CELL_SIZE + 10, 40, 40)
            pygame.draw.rect(screen, "red", seg_rect)
      
        # If player hits the edge of screen they lose
        if head_x > 14 or head_y > 14:
            running = False

        current_time = pygame.time.get_ticks()
        if current_time - last_move_time > move_delay:
            last_move_time = current_time
            
            if direction == "UP":
                head_y -= 1
        
            if direction == "DOWN":
                head_y += 1

            if direction == "LEFT":
                head_x -= 1

            if direction == "RIGHT":
                head_x += 1

            for i in range(len(snake) - 1, 0, -1):
                snake[i] = snake[i-1][:]

        snake[0] = [head_x, head_y]
            

        # Handle Collisions
        if head_x == apple_x and head_y == apple_y:
            # Spawn new apple somewhere else
            apple_x = random.randint(0, 14)
            apple_y = random.randint(0, 14)
            if direction == "UP":
                snake.append([tail_x, tail_y])
            elif direction == "DOWN":
                snake.append([tail_x, tail_y])
            elif direction == "LEFT":
                snake.append([tail_x, tail_y])
            elif direction == "RIGHT":
                snake.append([tail_x, tail_y])
            

        print(snake)
        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)

main()