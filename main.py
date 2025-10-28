#.\.venv\Scripts\Activate.ps1
import pygame
import pprint

def create_board():
    game_board = {}
    for x in range(1, 16):
        for y in range(1, 16):
            game_board[x, y] = " "
    
# print(pprint.pprint(game_board))

def main():

    # pygame setup
    pygame.init()

    pygame.display.set_caption("Snake Game")
    screen = pygame.display.set_mode((900, 720))
    clock = pygame.time.Clock()
    running = True

    # Movement flags
    moving_up = False
    moving_right = False
    moving_down = False
    moving_left = False
    direction = ""

    dt = 0

    player_pos = pygame.Vector2(screen.get_width() / 4, screen.get_height() / 2)
    
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
        pygame.draw.circle(screen, "red", player_pos, 20)


        if direction == "UP":
            player_pos.y -= 300 * dt

        if direction == "DOWN":
            player_pos.y += 300 * dt

        if direction == "LEFT":
            player_pos.x -= 300 * dt

        if direction == "RIGHT":
            player_pos.x += 300 * dt

            

        # flip() the display to put your work on screen
        pygame.display.flip()

        dt = clock.tick(60) / 1000

main()