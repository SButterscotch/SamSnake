import pygame
import random

# Initializing PyGame
pygame.init()

# Setting Game clock
clock = pygame.time.Clock()
FPS = 30

# Setting up Screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Storing Colors
black = (0, 0, 0)
white = (255, 255, 255)
silver = (190, 190, 190)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
aqua = (0, 255, 255)
magenta = (255, 0, 255)
dgreen = (0, 150, 0)
dred = (150, 0, 0)
purple = (128, 0, 128)
grey = (100, 100, 100)

# Setting Caption
pygame.display.set_caption("SamSlither")

# Setting Icon
# icon = pygame.image.load('icon.png')
# pygame.display.set_icon(icon)

# Various size
block_size = 20
apple_thickness = 20


# Making Player
def player(player_list):
    for element in player_list:
        screen.fill(dgreen, rect=(element[0], element[1], block_size, block_size))


# Making Apple
def apple(apple_x, apple_y):
    screen.fill(red, rect=(apple_x, apple_y, apple_thickness, apple_thickness))


# Setting Fonts
text_over = pygame.font.Font('freesansbold.ttf', 30)
text_again = pygame.font.Font('freesansbold.ttf', 30)
text_quit = pygame.font.Font('freesansbold.ttf', 30)

text_score = pygame.font.Font('freesansbold.ttf', 20)


# Setting GameOver Font
def GameOver(text, color):
    message = text_over.render(text, True, color)
    screen.blit(message, (screen_width - 700, screen_height / 2 - 150))


def Again(text, color):
    message = text_again.render(text, True, color)
    screen.blit(message, (screen_width - 700, screen_height / 2 - 100))


def Quit(text, color):
    message = text_quit.render(text, True, color)
    screen.blit(message, (screen_width - 700, screen_height / 2 - 50))


# Setting Score Font
def Score(text, color):
    message = text_score.render(text, True, color)
    screen.blit(message, (screen_width / 2 - 30, 20))


# Defining Game Loop
def GameLoop():
    # Initializing FPS
    clock.tick(FPS)

    # Initializing Score
    score_value = 0

    # Setting Player
    player_list = []
    player_length = 1
    player_x = screen_width / 2
    player_y = screen_height / 2
    player_x_change = 0
    player_y_change = 0
    player_speed = 10

    # Setting Apple
    apple_x = random.randint(0, screen_width - apple_thickness)
    apple_y = random.randint(0, screen_height - apple_thickness)

    # Running Game Loop
    run = True
    over = False
    while run:
        clock.tick(FPS)
        # What happens when the user loses
        while over:
            screen.fill(aqua)
            GameOver("Game Over:", dred)
            Again("Press R to play again", dred)
            Quit("Press Q to quit game", dred)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        GameLoop()
                    if event.key == pygame.K_q:
                        run = False
                        over = False
            pygame.display.update()

        # Setting Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    player_y_change += player_speed
                    player_x_change = 0
                if event.key == pygame.K_UP:
                    player_y_change -= player_speed
                    player_x_change = 0
                if event.key == pygame.K_LEFT:
                    player_x_change -= player_speed
                    player_y_change = 0
                if event.key == pygame.K_RIGHT:
                    player_x_change += player_speed
                    player_y_change = 0

        # Calling and setting functions
        screen.fill(silver)

        player_x += player_x_change
        player_y += player_y_change
        player_head = [player_x, player_y]
        player_list.append(player_head)
        if len(player_list) > player_length:
            del player_list[0]
        if player_x <= 0:
            player_x = screen_width - block_size
        if player_x >= screen_width:
            player_x = block_size
        if player_y <= 0:
            player_y = screen_height - block_size
        if player_y >= screen_height:
            player_y = block_size
        for each in player_list[:-1]:
            if each == player_head:
                over = True

        player(player_list)

        # Setting Collision
        if apple_x < player_x < apple_x + apple_thickness or apple_x < player_x + block_size < apple_x + apple_thickness:
            if apple_y < player_y < apple_y + apple_thickness:
                apple_x = random.randint(0, screen_width - apple_thickness)
                apple_y = random.randint(0, screen_height - apple_thickness)
                score_value += 1
                player_length += 1
            elif apple_y < player_y + block_size < apple_y + apple_thickness:
                apple_x = random.randint(0, screen_width - apple_thickness)
                apple_y = random.randint(0, screen_height - apple_thickness)
                score_value += 1
                player_length += 1
        apple(apple_x, apple_y)

        Score("Score: " + str(score_value), grey)
        pygame.display.update()
    pygame.quit()
    quit()


GameLoop()