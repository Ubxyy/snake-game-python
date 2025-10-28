#.\.venv\Scripts\Activate.ps1
import pygame
import pprint

WHITE = (200, 200, 200)
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

def draw_board(screen):
    for x in range(0, SCREEN_WIDTH, CELL_SIZE):
        for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, WHITE, rect, 1)

def main():

    # pygame setup
    pygame.init()

    pygame.display.set_caption("Snake Game")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True


    direction = ""



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

        draw_board(screen)
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