# PingPong Game
Pygame 을 사용하여 만들어진 핑퐁게임입니다. AI를 상대로 게임이 진행되며 AI가 10점을 달성시 종료됩니다.
종료시 플레이어의 이름,점수,날짜가 랭킹에 기록됩니다.


Requirements
----------
- python 2 or 3
- pygame
- numpy



Getting started
-----------
Pygame 모듈 설치가 필요합니다.

Python 2 또는 3의 환경에서 사용 가능합니다.



Original game source
-----------
```
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
```

1. 공을 받아칠 하얀색 직사각형 바 2개(**bar1, bar2**)를 생성하고, 하얀색 공(**circle**)을 만듭니다.



```
bar1_x, bar2_x = 10. , 620.
bar1_y, bar2_y = 215. , 215.
circle_x, circle_y = 307.5, 232.5
bar1_move, bar2_move = 0. , 0.
speed_x, speed_y, speed_circ = 250., 250., 250.
bar1_score, bar2_score = 0,0

#clock and font objects
clock = pygame.time.Clock()
font = pygame.font.SysFont("calibri",40)

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
  ```
  
  2. 공이 바에서 튕기면 반대쪽 방향의 랜덤위치로 이동하는 코드입니다.
  여기서, 플레이어가 우측 상단의 X 키를 눌러 종료하면 게임이 꺼집니다. 
  플레이어는 키보드의 위아래 방향키를 이용하여 바를 움직일 수 있습니다.
  
  
  
```
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
    if circle_x >= bar2_x - 15.:
        if circle_y >= bar2_y - 7.5 and circle_y <= bar2_y + 42.5:
            circle_x = 605.
            speed_x = -speed_x
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
    elif circle_y >= 457.5:
        speed_y = -speed_y
        circle_y = 457.5

    pygame.display.update()
```

3. AI의 움직임을 설정한 코드입니다.
AI의 바가 공을 튕기지 못하고 벽을 지나치면 플레이어가 점수 1점을 획득합니다.
이후 공의 위치가 초기화 되어 다시 움직입니다.
마찬가지로 플레이어가 공을 튕기지 못하면 AI가 점수를 획득하고, 공 위치가 초기화됩니다.
    
    
    
# Modified game source


## 음향 추가

 ```
 music = os.path.join('bgm','bubble_bobble.wav')
bgm = pygame.mixer.Sound(music)
bgm.play(-1) 
bgm.set_volume(0.3) 

music2 = os.path.join('bgm',"game_over.wav")
game_over = pygame.mixer.Sound(music2)

music3  = os.path.join('bgm',"pingpongbat.wav")
pingpong = pygame.mixer.Sound(music3)

music4  = os.path.join('bgm', "click.wav")
click = pygame.mixer.Sound(music4)
```

1. **'bgm'** 폴더안에서 상황에 맞는 음악을 가져와 적절하게 설정해줍니다.


`<pingpong.play()>`

```
    if circle_x <= bar1_x + 10.:
        if circle_y >= bar1_y - 7.5 and circle_y <= bar1_y + 42.5:
            circle_x = 20.
            speed_x = -speed_x
            pingpong.play()
```    

2. 공이 바에 닿을때, 공을 받아내지 못했을때 등 각 상황에 맞게 소리가 나게 브금을 추가해 줍니다.




```
 if bar2_score == 3:  # ai가 10점 달성시 종료 bgm
        c.execute("INSERT INTO users('username', 'score', 'regdate') VALUES(?,?,?)", \
            ('playern', bar1_score, nowDatetime))
        bgm.stop()
        game_over.play()
        game_over.set_volume(0.3)
        # 게임 오버 메시지
        msg = font.render("Game Over", True, (255, 255, 0)) 
        screen.blit(msg, (230,260))
        pygame.display.update()
```

3. `if bar2_score == 3:` 해당 라인을 통해, 특정 조건이 되었을때 게임이 종료되고 
`<bgm.stop()>` 원래 나오던 브금을 종료, `<game_over.play()>` 새로운 종료 브금이 나오도록 추가해 줍니다.
  AI가 특정 점수를 획득시 게임이 종료되는 문구가 표시되고, 4초후 프로그램이 종료되도록 설정합니다.



## 랭킹 제도 추가 

```
now=datetime.datetime.now()
nowDatetime=now.strftime('%Y-%m-%d %H:%M:%S')
```

1. `datetime` 을 이용하여 게임 시간을 기록하는 변수를 설정합니다.



```
conn=sqlite3.connect('rank.db', isolation_level=None)
c=conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, \
    username text, score text, regdate text)")
```

2.  db 경로와 커서를 연결하고 테이블을 생성합니다.
점수가 기록되면 따로 insert 해주지 않아도 1씩 증가 되게 합니다.
      
      
      
```
def pg_rank():
    rankwindow()
    loop=1

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop = 0
                    pygame.quit()
        pygame.display.update()
        clock.tick(60)
```

3. 시작화면의 Ranking 버튼을 클릭하면 해당 함수가 실행되어 `rankwindow()` 함수를 통해 랭킹 화면이 나오게 합니다.




```
def rankwindow():
    screen.fill(white)
    BLACK = (0,0,0)
    RED = (255,0,0)
    BLUE = (0,0,255)
    
    myFont = pygame.font.SysFont("arial",30,True,False)
    myFont2 = pygame.font.SysFont("arial", 14, True, False)
    myFont3 = pygame.font.SysFont("arial", 25, True, False)

    text_rank = myFont.render("RANKING", True, RED)
    text_back = myFont2.render("Press space to go back", True,RED )
    text_row=myFont.render("NAME    SCORE   REGDATE", True, (0,0,0))
    screen.blit(text_rank, (240,30))
    screen.blit(text_row, (140, 90))
  
```

4. 랭킹 화면이 나타나는 함수입니다. 
`<screen.fill(white)>` 하얀색 배경으로 된 창에 "RANKING", "NAME    SCORE   REGDATE", "Press space to go back" 글씨가 나타나게 합니다. 




```
def wait_key():
    waiting = True
    while waiting:
        clock.tick(600)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                running = False
            if event.type == pygame.K_SPACE:
                waiting = False
                running = False        
```

5. `clock.tick(600)`을 이용해 시간을 600초로 임의로 설정한뒤, 
`<if event.type == pygame.K_SPACE:>` Space 키를 누르면 다시 돌아가게 설정합니다.




```
  for row, length in zip(c.execute("SELECT username, score, regdate FROM users ORDER BY score desc LIMIT 5"), range(140,610,30)):
        row=(','.join(row)).split(',')
        for s, width in zip(row, [140, 270, 320]):
            rank=myFont3.render(s, True, BLACK)
            screen.blit(rank, (width, length))

    screen.blit(text_back, (240,380))
```

6. **함수 rankwindow()** 부분중, 랭킹을 클릭하면 그동안 저장된 데이터를
`ORDER BY score desc LIMIT 5` score 기준 내림차순 정렬하여 5개 값을 출력합니다.




```
 if bar2_score == 3:  # ai가 10점 달성시 종료 bgm
        c.execute("INSERT INTO users('username', 'score', 'regdate') VALUES(?,?,?)", \
            ('playern', bar1_score, nowDatetime))
```

7. AI 가 특정 점수를 획득하면, `execute` 를 이용하여 각 데이터를 db에 저장합니다.



## 시작화면 추가

```
class Button:
    def __init__(self, color, x, y, width, height, text = ''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
    
    def draw(self, win, outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)
        
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
        
    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False
 ```
 
 1. Button 클래스 안에 색, 좌표, 크기, 텍스트 를 추가합니다. 
 `<def draw(self, win, outline=None):>` 해당 함수에서 외곽선 및 버튼을 그립니다.
 `<def isOver(self, pos):>` 함수에서 버튼의 크기를 정해줍니다.
 
 
 
 
 ```
 def intro():
    i=True
    StartButton = Button((0, 255, 0), 450, 100, 50, 50, 'Click')
    RankingButton = Button((0, 255, 0), 450, 200, 50, 50, 'Click')
    QuitButton = Button((0, 255, 0), 450, 300, 50, 50, 'Click')

    Start = font.render('Start', True,(255,255,255))
    Ranking = font.render('Ranking', True,(255,255,255))
    Quit = font.render('Quit', True,(255,255,255))
    while i:
        
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            keyp = action()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if keyp!=None or event.type==pygame.KEYDOWN :
                try:
                    if keyp=='c' or event.key==pygame.K_c :
                        i=False
                except:
                    continue
            if event.type == pygame.MOUSEBUTTONDOWN:
                if StartButton.isOver(pos):
                    click.play()
                    i=False
                elif RankingButton.isOver(pos):
                    click.play()
                    i=False
                    pg_rank()
                elif QuitButton.isOver(pos):
                    click.play()
                    pygame.quit()
                    quit()
        image = pygame.image.load(pong_title_path)
        screen.blit(image,(0,0))
        screen.blit(Start,(450.,100.))
        screen.blit(Ranking,(450.,200.))
        screen.blit(Quit,(450.,300.))
        pygame.display.update()
        clock.tick(15)
```

2. `<image = pygame.image.load(pong_title_path)>` 를 통해 배경화면을 설정합니다.
위치에 맞게 Start, Ranking, Quit 버튼을 클래스를 활용해 추가해줍니다.
`< if event.type == pygame.MOUSEBUTTONDOWN:>` 마우스를 클릭했을때의 이벤트를 추가하여 
**Ranking** 버튼을 눌렀을때는 랭킹 화면이 나타나도록 `pg_rank()` 해당함수를 추가합니다.
마찬가지로 Quit 버튼을 눌렀을때는 게임이 종료되도록 `pygame.quit()` 해당 라인을 추가합니다.




```
def action():
    global blist
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    for tup in blist:
        if tup[0] + tup[2] > mouse[0] > tup[0] and tup[1] + tup[3] > mouse[1] > tup[1]:
            if click[0] == 1:
                return tup[4]
    return None
intro()    
```

3. 현재 마우스 클릭 좌표를 기준으로 버튼을 구현합니다.



## 정지기능 추가

```
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
```

1. 사용할 색을 지정해주고, 글씨 폰트와 크기를 설정해
"PAUSE", "Press space to continue", "Press esc to quit" 문구를 위치에 맞게 추가해줍니다.
 
 
 
```

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
```

2. `< if event.type == pygame.KEYDOWN:>` 를 이용해 키가 눌러졌을때의 이벤트를 살핍니다.
`if event.key == pygame.K_ESCAPE:` Esc키를 누르면 게임 프로그램 종료,
`if event.key == pygame.K_SPACE:`   Space 키를 누르면 게임이 재시작 되게 합니다.





Games
--------
- [Pong](https://github.com/DanielSlater/PyGamePlayer/blob/master/games/pong.py)
