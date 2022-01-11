import pygame
import sys


green_player = True
x_field, y_field = 550, 550
width, height = 50, 50


pygame.init()
win = pygame.display.set_mode((x_field, y_field))

pygame.display.set_caption('Andrii Dovgalyuk')

green_payer_coordinate = ((3-1)*2*height, (1-1)*2*width)
red_payer_coordinate = ((4-1)*2*height, (6-1)*2*width)


while True:
    pygame.time.delay(100)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            next_step = (event.pos[0]//100 * 100, event.pos[1]//100 * 100)

            
            if green_player:
                if abs(green_payer_coordinate[0] - next_step[0]) == 100 or abs(green_payer_coordinate[1] - next_step[1]) == 100:
                    green_payer_coordinate = next_step
                    green_player = False
            else:
                if abs(red_payer_coordinate[0] - next_step[0]) == 100 or abs(red_payer_coordinate[1] - next_step[1]) == 100:
                    red_payer_coordinate = next_step
                    green_player = True
                

    
    x, y = 0, 0


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
