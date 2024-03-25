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



    if enemys.enemys == []:
        game_over = True

    """for enemy in enemys.enemys:
        for bullet in player.bullets:
            bullet[1] -= 10
            pygame.draw.rect(win, RED, (bullet[0], bullet[1], player.bullet_width, player.bullet_height))

            if bullet[1] < 0:
                bullet[0] = player.x
                bullet[1] = player.y
                player.bullets.remove(bullet)

            if (enemy[0] - 70 <= bullet[0] <= enemy[0] + 70) and (enemy[1] - 50 <= bullet[1] <= enemy[1] + 50):
                enemys.enemys.remove(enemy)
                player.stroke_enemy = True
                bullet[0] = player.x + 55
                bullet[1] = player.y
                player.bullets.remove(bullet)
                # self.abgefeuert = False
                # self.space = False
                player.stroke_enemy = False"""

    if not player.bullets == []:
        for bullet in player.bullets:
            bullet[1] -= 10
            pygame.draw.rect(win, RED, (bullet[0], bullet[1], player.bullet_width, player.bullet_height))

            for enemy in enemys.enemys:
                if (enemy[0] - 70 <= bullet[0] <= enemy[0] + 70) and (enemy[1] - 50 <= bullet[1] <= enemy[1] + 50):
                    enemys.enemys.remove(enemy)
                    #player.stroke_enemy = True
                    #bullet[0] = player.x + 55
                    #bullet[1] = player.y
                    player.bullets.remove(bullet)
                    # self.abgefeuert = False
                    # self.space = False
                    #player.stroke_enemy = False

                elif bullet[1] < 0:
                    bullet[0] = player.x
                    bullet[1] = player.y
                    player.bullets.remove(bullet)



    pygame.display.update()




while not game_over:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                player.space = True
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
        #player.space = True
        pass
    else:
        player.left = False
        player.right = False


    redrawGameWindow()
