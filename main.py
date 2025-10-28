#.\.venv\Scripts\Activate.ps1
import pygame
import pprint
import random

WHITE = (200, 200, 200)
BLACK = (10, 10, 10)
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
CELL_SIZE = SCREEN_WIDTH//15
player_cell = [7, 7]
move_delay = 200   # milliseconds between moves



def create_board():
    game_board = {}
    for x in range(1, 16):
        for y in range(1, 16):
            game_board[x, y] = " "
    return game_board


# print(pprint.pprint(game_board))

def draw_board(screen, apple_x, apple_y):
    for x in range(0, SCREEN_WIDTH, CELL_SIZE):
        for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            
            if x == apple_x * CELL_SIZE and y == apple_y * CELL_SIZE:
                pygame.draw.circle(screen, BLACK, (CELL_SIZE * apple_y+CELL_SIZE/2, CELL_SIZE * apple_x + CELL_SIZE/2), 15)
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

    apple_x = random.randint(1, 15)
    apple_y = random.randint(1, 15)

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
        screen.fill("green")
 
        # RENDER YOUR GAME HERE

        draw_board(screen, apple_x, apple_y)
        pygame.draw.circle(screen, "red", (CELL_SIZE * player_cell[0] + CELL_SIZE/2, CELL_SIZE * player_cell[1] + CELL_SIZE/2), CELL_SIZE//2 - 5)
        print(player_cell)

        current_time = pygame.time.get_ticks()
        if current_time - last_move_time > move_delay:
            last_move_time = current_time
            
            if direction == "UP":
                player_cell[1] -= 1

            if direction == "DOWN":
                player_cell[1] += 1

            if direction == "LEFT":
                player_cell[0] -= 1

            if direction == "RIGHT":
                player_cell[0] += 1

      

            

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)

main()