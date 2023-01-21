import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1200,800))
pygame.display.set_caption("Dodge the blocks! REMASTERED")

active = False

gravity = 0

background = pygame.image.load("bg.png")
player_surf = pygame.image.load("ninja.png")
player_rect = player_surf.get_rect(midbottom = (575,600))
my_font = pygame.font.SysFont('Comic Sans MS', 30)


# Block/Enemy
block = pygame.image.load("block.png")
block_rect = block.get_rect(midbottom = (600,50))

# Block2
block_yellow = pygame.image.load("block_yellow.png")
block_yellow_rect = block_yellow.get_rect(midbottom = (600, 50))


FPS = pygame.time.Clock()
# LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()  
    if active:
        # Keybinds + gravity
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and player_rect.bottom >= 600:
            gravity = -20
        if keys[pygame.K_d] and player_rect.x <1150:
            player_rect.x += 10
        if keys[pygame.K_a] and player_rect.x >10:
            player_rect.x -= 10

        
        screen.blit(background,(0,0))
        screen.blit(player_surf,player_rect)
        screen.blit(block,block_rect)
        screen.blit(block_yellow,block_yellow_rect)

        
        gravity += 1
        player_rect.y += gravity
        if player_rect.bottom >= 600: player_rect.bottom = 600
        block_rect.y += 14
        if block_rect.y > 800:
            block_rect.y = 0
            block_rect.x = random.randint(0,1200)
        block_yellow_rect.y += 10
        if block_yellow_rect.y > 800:
            block_yellow_rect.y = 0
            block_yellow_rect.x = random.randint(0,1200)

        
        # Collisions
        if player_rect.colliderect(block_rect): #DEAD, WIP
            active = False
            print("You Died!")
        if player_rect.colliderect(block_yellow_rect):
            active = False
            print("You Died!")

    else:
        screen.fill("yellow")
        text_surface = my_font.render('Press "P" to start', False, ("green"))
        text_surface2 = my_font.render('Dodge the blocks!', False, ("RED"))
        screen.blit(text_surface, (480,200))
        screen.blit(text_surface2, (480,100))
        screen.blit(player_surf, (575,400))
       
        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
            active = True
            block_rect.y = 0
            block_yellow_rect.y = 0
        

    pygame.display.update()
    FPS.tick(60) #FPS