#Modified from http://www.pygame.org/project-Very+simple+Pong+game-816-.html
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
import numpy
import pygame
from pygame.locals import *
from sys import exit
import random
import pygame.surfarray as surfarray
import time   #modify
from tkinter import *  #modify
import sqlite3
import datetime

now=datetime.datetime.now()
nowDatetime=now.strftime('%Y-%m-%d %H:%M:%S')

conn=sqlite3.connect('rank.db', isolation_level=None)
c=conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, \
    username text, score INTEGER, regdate text)")

pygame.init()

pygame.mixer.init()  
pygame.mixer.music.load("bgm/bubble_bobble.mp3") # 게임 bgm
pygame.mixer.music.set_volume(0.3) # volume 조절 1 ~ 0.1
pygame.mixer.music.play(-1) 

game_over = pygame.mixer.Sound("bgm/game_over.wav")  # 종료 bgm
pingpong = pygame.mixer.Sound("bgm/pingpongbat.wav") # 게임 효과음


screen = pygame.display.set_mode((640,480),0,32)

#Creating 2 bars, a ball and background.
back = pygame.Surface((640,480))
background = back.convert()
background.fill((0,0,0))
bar = pygame.Surface((10,50))
bar1 = bar.convert()
bar1.fill((255,255,255))
bar2 = bar.convert()
bar2.fill((255,255,255))
circ_sur = pygame.Surface((15,15))
circ = pygame.draw.circle(circ_sur,(255,255,255),(int(15/2),int(15/2)),int(15/2))
circle = circ_sur.convert()
circle.set_colorkey((0,0,0))



# some definitions
bar1_x, bar2_x = 10. , 620.
bar1_y, bar2_y = 215. , 215.
circle_x, circle_y = 307.5, 232.5
bar1_move, bar2_move = 0. , 0.
speed_x, speed_y, speed_circ = 250., 250., 250.
bar1_score, bar2_score = 0,0

#clock and font objects
clock = pygame.time.Clock()
font = pygame.font.SysFont("calibri",40)




#modify +++++++++++++++++++++++++++++++++++++++


def paused():
    loop =1
    BLACK = (0,0,0)
    RED = (255,0,0)
    BLUE = (0,0,255)
    
    myFont = pygame.font.SysFont("arial",30,True,False)
    myFont2 = pygame.font.SysFont("arial", 20, True, False)

    text_pause = myFont.render("PAUSE", True, RED)
    text_continue = myFont2.render("Press space to continue", True,BLUE )
    text_quit = myFont2.render("Press esc to quit", True, BLUE)

    screen.blit(text_pause, (280,150))
    screen.blit(text_continue, (230,260))
    screen.blit(text_quit, (230, 320))



    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop = 0
                    pygame.quit()
                if event.key == pygame.K_SPACE:
                    screen.fill((0,0,0))
                    loop = 0
        pygame.display.update()
        clock.tick(60)                

# +++++++++++++++++++++++++++++++++++++++++++


done = False
while done==False:       
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        if event.type == KEYDOWN:
            if event.key == K_UP:
                bar1_move = -ai_speed
            elif event.key == K_DOWN:
                bar1_move = ai_speed
        elif event.type == KEYUP:
            if event.key == K_UP:
                bar1_move = 0.
            elif event.key == K_DOWN:
                bar1_move = 0.


#modify ****************************************************
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                paused()
            

 # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            
    score1 = font.render(str(bar1_score), True,(255,255,255))
    score2 = font.render(str(bar2_score), True,(255,255,255))

    screen.blit(background,(0,0))
    frame = pygame.draw.rect(screen,(255,255,255),Rect((5,5),(630,470)),2)
    middle_line = pygame.draw.aaline(screen,(255,255,255),(330,5),(330,475))
    screen.blit(bar1,(bar1_x,bar1_y))
    screen.blit(bar2,(bar2_x,bar2_y))
    screen.blit(circle,(circle_x,circle_y))
    screen.blit(score1,(250.,210.))
    screen.blit(score2,(380.,210.))

    bar1_y += bar1_move
        
    # movement of circle
    time_passed = clock.tick(30)
    time_sec = time_passed / 1000.0
        
    circle_x += speed_x * time_sec
    circle_y += speed_y * time_sec
    ai_speed = speed_circ * time_sec
    
    #AI of the computer.
    if circle_x >= 305.:
        if not bar2_y == circle_y + 7.5:
            if bar2_y < circle_y + 7.5:
                bar2_y += ai_speed
            if  bar2_y > circle_y - 42.5:
                bar2_y -= ai_speed
        else:
            bar2_y == circle_y + 7.5
    
    if bar1_y >= 420.: bar1_y = 420.
    elif bar1_y <= 10. : bar1_y = 10.
    if bar2_y >= 420.: bar2_y = 420.
    elif bar2_y <= 10.: bar2_y = 10.
    #since i don't know anything about collision, ball hitting bars goes like this.
    if circle_x <= bar1_x + 10.:
        if circle_y >= bar1_y - 7.5 and circle_y <= bar1_y + 42.5:
            circle_x = 20.
            speed_x = -speed_x
            pygame.mixer.Sound.play(pingpong)

    if circle_x >= bar2_x - 15.:
        if circle_y >= bar2_y - 7.5 and circle_y <= bar2_y + 42.5:
            circle_x = 605.
            speed_x = -speed_x
            pygame.mixer.Sound.play(pingpong)

    if circle_x < 5.:
        bar2_score += 1
        circle_x, circle_y = 320., 232.5
        bar1_y,bar_2_y = 215., 215.
    elif circle_x > 620.:
        bar1_score += 1
        circle_x, circle_y = 307.5, 232.5
        bar1_y, bar2_y = 215., 215.
    if circle_y <= 10.:
        speed_y = -speed_y
        circle_y = 10.
        pygame.mixer.Sound.play(pingpong)

    elif circle_y >= 457.5:
        speed_y = -speed_y
        circle_y = 457.5
        pygame.mixer.Sound.play(pingpong)
        
    if bar2_score == 10:  # ai가 10점 달성시 종료 bgm
        pygame.mixer.music.stop() 
        pygame.mixer.Sound.play(game_over)
        game_over.set_volume(0.3)
        # 게임 오버 메시지
        msg = font.render("Game Over", True, (255, 255, 0)) 
        screen.blit(msg, (230,260))
        pygame.display.update()

        # 4초 대기후 나가기
        pygame.time.delay(4000)
        pygame.quit()
        exit()



    pygame.display.update()
            
pygame.quit()
c.close()