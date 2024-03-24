import pygame
from PIL import Image
from GameElements import Player, RED, WHITE, Enemy

win = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Space Invaders")


background = pygame.image.load("Pics/StarBackground.gif")
background = pygame.transform.scale(background, (1000, 750))
player = pygame.image.load("Pics/Rakete.png")
enemy_1 = pygame.image.load("Pics/Enemy1.png")


player = Player()



game_over = False

clock = pygame.time.Clock()





enemy = Enemy()

def redrawGameWindow():
    win.blit(background, (0,0))
    player.draw(win)
    #enemy_creator()
    enemy.draw(win)

    #player.shoot(win)
    pygame.display.update()




while not game_over:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.x > player.vel:
        player.left = True
        player.right = False
        player.x -= player.vel
    elif keys[pygame.K_RIGHT] and player.x < 1000 - player.width - player.vel:
        player.left = False
        player.right = True
        player.x += player.vel

    elif keys[pygame.K_SPACE]:
        player.space = True

    else:
        player.left = False
        player.right = False


    redrawGameWindow()

