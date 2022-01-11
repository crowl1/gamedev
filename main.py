import pygame


x_field, y_field = 550, 550
width, height = 50, 50


pygame.init()
win = pygame.display.set_mode((x_field, y_field))

pygame.display.set_caption('Cubes Game')


run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    x, y = 0, 0

    while x < x_field:
        while y < y_field:
            pygame.draw.rect(win, (0,0,255), (x, y, width, height))

            y += 100
        
        y = 0
        x += 100
    
    
    pygame.display.update()


pygame.quit()
