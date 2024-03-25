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





enemys = Enemy()

def redrawGameWindow():
    global game_over
    win.blit(background, (0,0))
    player.draw(win)
    #enemy_creator()
    enemys.draw(win)



    if enemys == []:
        game_over = True

    for enemy in enemys.enemys:
        if (enemy[0] - 70 <= player.bullet_x <= enemy[0] + 70) and (enemy[1] - 50 <= player.bullet_y <= enemy[1] + 50):
            print(f"Player: ({player.bullet_x}/{player.bullet_y})\nEnemy: {enemy}")
            enemys.enemys.remove(enemy)
            player.stroke_enemy = True



    pygame.display.update()




while not game_over:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.x > player.vel:
        print(f"Player x: {player.x}")
        print(f"Bullet_x : {player.bullet_x}")
        player.left = True
        player.right = False
        player.x -= player.vel
    elif keys[pygame.K_RIGHT] and player.x < 1000 - player.width - player.vel:
        print(f"Player x: {player.x}")
        print(f"Bullet_x : {player.bullet_x}")

        player.left = False
        player.right = True
        player.x += player.vel

    elif keys[pygame.K_SPACE]:
        player.space = True

    else:
        player.left = False
        player.right = False


    redrawGameWindow()

