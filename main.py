# freecodecamp beatmaker
import pygame
from pygame import mixer
pygame.init()

WIDTH = 900
HEIGHT = 600

black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('BeatMaker')
label_font = pygame.font.Font('freesansbold.ttf', 20)

fps = 60
timer = pygame.time.Clock()
beats = 8
instruments = 6


def draw_grid():
    left_box = pygame.draw.rect(screen, gray, [0, 0, 150, HEIGHT - 150], 5)
    bottom_box = pygame.draw.rect(
        screen, gray, [0, HEIGHT - 150, WIDTH, 150], 5)
    boxes = []
    colors = [gray, white, gray]
    hi_hat_text = label_font.render('Hi Hat', True, white)
    screen.blit(hi_hat_text, (30, 30))
    snare_text = label_font.render('Snare', True, white)
    screen.blit(snare_text, (30, 105))
    kick_text = label_font.render('Bass Drum', True, white)
    screen.blit(kick_text, (30, 180))
    crash_text = label_font.render('Crash', True, white)
    screen.blit(crash_text, (30, 260))
    Clap_text = label_font.render('Clap', True, white)
    screen.blit(Clap_text, (30, 330))
    Flor_text = label_font.render('Floor Tom', True, white)
    screen.blit(Flor_text, (30, 400))
    for i in range(instruments):
        pygame.draw.line(screen, gray, (0, (i * 75) + 75),
                         (145, (i * 75) + 75), 3)
    for i in range(beats):
        for j in range(instruments):
            rect = pygame.draw.rect(screen, gray, [i * ((WIDTH - 150) // beats) + 150, (j * 75), 
            ((WIDTH - 150) // beats), ((HEIGHT - 150) //instruments)], 5, 5)

run=True
while run:
    timer.tick(fps)
    screen.fill(black)
    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

    pygame.display.flip()
pygame.quit()
