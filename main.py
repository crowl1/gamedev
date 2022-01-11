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

    green_payer_point = (3,1)
    green_payer_coordinate = ((green_payer_point[0]-1)*2*height, (green_payer_point[1]-1)*2*width)

    red_payer_point = (4,6)
    red_payer_coordinate = ((red_payer_point[0]-1)*2*height, (red_payer_point[1]-1)*2*width)

    while x < x_field:
        while y < y_field:

            if (x, y) == red_payer_coordinate:
                pygame.draw.rect(win, (255,0,0), (x, y, width, height))
            elif (x, y) == green_payer_coordinate:
                pygame.draw.rect(win, (0,255,0), (x, y, width, height))
            else:
                pygame.draw.rect(win, (0,0,255), (x, y, width, height))

            y += 100
        
        y = 0
        x += 100
    
    
    pygame.display.update()


pygame.quit()
