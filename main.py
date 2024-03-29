import pygame
import sys
import random

from betterconf import Config, field

from settings import *
from neural_network import outputs
from model import Player


class GameConfig(Config):
    game_mode = field(default = GAME_MODE_DEFAULT)
    green_player = field(default = GREEN_PLAYER_DEFAULT)
    green_player_coordinate = field(default = GREEN_PLAYER_COORDINATE_DEFAULT)
    red_player_coordinate = field(default = RED_PLAYER_COORDINATE_DEFAULT)

cfg = GameConfig()

green_player = Player(GREEN_PLAYER_COORDINATE_DEFAULT[0] , GREEN_PLAYER_COORDINATE_DEFAULT[1])
green_player = Player(RED_PLAYER_COORDINATE_DEFAULT[0] , RED_PLAYER_COORDINATE_DEFAULT[1])

pygame.init()
win = pygame.display.set_mode((X_FIELD, Y_FIELD))
pygame.display.set_caption('Andrii Dovgalyuk')


def reset():
    cfg.green_player = GREEN_PLAYER_DEFAULT
    cfg.green_player_coordinate = GREEN_PLAYER_COORDINATE_DEFAULT
    cfg.red_player_coordinate = RED_PLAYER_COORDINATE_DEFAULT


def check_win():
    if cfg.green_player_coordinate[1] >= Y_FIELD - 2 * HEIGHT:
        print('Зелений виграв')
        sys.exit()
    elif cfg.red_player_coordinate[1] <= HEIGHT:
        print('Червоний виграв')
        sys.exit()


def game():
    walls = []

    while True:
        pygame.time.delay(100)

        check_win()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.MOUSEBUTTONDOWN:

                if cfg.green_player:
                    print('ходить зелений')
                else:
                    print('ходить червоний')

                
                pos = event.pos

                if cfg.game_mode == 1 and not cfg.green_player:
                    pos = (cfg.red_player_coordinate[0] + random.randint(-100,101), cfg.red_player_coordinate[1] + random.randint(-100,101))
                elif cfg.game_mode == 0 and not cfg.green_player:
                    outputs_list = outputs.tolist()
                    pos = (cfg.red_player_coordinate[0] - (outputs_list[0][0] + outputs_list[1][0]) * 100, cfg.red_player_coordinate[1] - (outputs_list[2][0] + outputs_list[3][0]) * 100)
                
                next_step = (pos[0]//100 * 100, pos[1]//100 * 100)

                shift =  (pos[0] - next_step[0], pos[1] - next_step[1])



                if sum(shift) < 100:

                    if cfg.green_player:
                        coordinate = cfg.green_player_coordinate
                    else:
                        coordinate = cfg.red_player_coordinate
                    

                    road = (abs((coordinate[0] - next_step[0])/2 + coordinate[0]), abs((coordinate[1] - next_step[1])/2 + coordinate[1]))

                    if abs(coordinate[0] - next_step[0]) + abs(coordinate[1] - next_step[1]) <= 200 and road not in walls:
                        if cfg.green_player:
                            cfg.green_player_coordinate = next_step
                        else:
                            cfg.red_player_coordinate = next_step
                        
                        cfg.green_player = not cfg.green_player
                    
                
                elif shift[0] > shift[1]:
                    walls.append((pos[0]//50 * 50, pos[1]//50 * 50))
                    walls.append((pos[0]//50 * 50, pos[1]//50 * 50 + 50))
                    cfg.green_player = not cfg.green_player
                
                elif shift[0] < shift[1]:
                    walls.append((pos[0]//50 * 50, pos[1]//50 * 50))
                    walls.append((pos[0]//50 * 50 + 50, pos[1]//50 * 50))
                    cfg.green_player = not cfg.green_player
                
            

            elif event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_2:
                    cfg.game_mode = 2

                elif event.key == pygame.K_1:
                    cfg.game_mode = 1
                
                elif event.key == pygame.K_0:
                    cfg.game_mode = 0
                
                reset()
                walls = []

        
        x, y = 0, 0
        while x < X_FIELD:
            while y < Y_FIELD:

                if (x, y) == cfg.red_player_coordinate:
                    pygame.draw.rect(win, (255,0,0), (x, y, WIDTH, HEIGHT))
                elif (x, y) == cfg.green_player_coordinate:
                    pygame.draw.rect(win, (0,255,0), (x, y, WIDTH, HEIGHT))
                else:
                    pygame.draw.rect(win, (0,0,255), (x, y, WIDTH, HEIGHT))

                y += 100
            
            y = 0
            x += 100
        
        for wall in walls:
            pygame.draw.rect(win, (255,255,0), (wall[0], wall[1], WIDTH, HEIGHT))
        
        
        pygame.display.update()


if __name__=='__main__':
    game()
    pygame.quit()