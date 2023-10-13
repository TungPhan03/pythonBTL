import pygame,random
import mouse
from sys import exit
pygame.init()
def dis_screen():
    screenn = pygame.display.set_mode((1296,768))
    pygame.display.set_caption('Flappy Bird Bài Tập Lớn')
    return screenn
def dis_background():
    screen.blit(bg,(0,0))
def rotate_bird(birdd): 
    new_bird = pygame.transform.rotozoom(birdd,-bird_move*3,1)
    return new_bird
def dis_bird(): 
    global bird_move 
    bird_move+=0.3
    rotated_bird = rotate_bird(bird)
    bird_dis.centery+=bird_move
    screen.blit(rotated_bird,bird_dis)
def bird_animation():
    new_bird = bird_list[bird_index]
    new_bird_dis = new_bird.get_rect(center=(100,bird_dis.centery))
    return new_bird, new_bird_dis
def create_pipe():
    random_pipe_post = random.choice(range(400,800,100))
    bottom_pipe = pipe_surface.get_rect(midtop =(1150,random_pipe_post))
    top_pipe = pipe_surface.get_rect(midtop=(1000,random_pipe_post-850))
    return bottom_pipe,top_pipe
def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx-=5
    return pipes
def dis_pipe(pipes):
    global pipe_list
    pipe_list = move_pipe(pipe_list)
    for pipe in pipes:
        if pipe.bottom >= 700:
            screen.blit(pipe_surface,pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface,False,True)
            screen.blit(flip_pipe,pipe)
def dis_floor():  
    global fl_x
    fl_x-=1
    screen.blit(fl,(fl_x,650))
    if fl_x==-432//3: fl_x = 0
def check_collision(pipes):
    global bird_dis
    for pipe in pipes:
        if bird_dis.colliderect(pipe):
            hit_sound.play()
            return False
    if bird_dis.top<=-75 or bird_dis.top >=650: 
        hit_sound.play()
        return False
    return True
def dis_score(game_state):
    if game_state == True:
        score_surface = game_font.render('Score: %d'%int(score),True,('grey'))
        score_rect = score_surface.get_rect(center=(648,100))
        screen.blit(score_surface,score_rect)
    if game_state == False:
        score_surface = game_font.render('Score: %d'%int(score),True,('grey'))
        score_rect = score_surface.get_rect(center=(648,100))
        screen.blit(score_surface,score_rect)

        high_score_surface = game_font.render('High score: %d'%int(high_score),True,('grey'))
        high_score_rect = high_score_surface.get_rect(center=(648,150))
        screen.blit(high_score_surface,high_score_rect)
def show_level(x):
    if x==60: screen.blit(dis_level_de,dis_level_de_rect)
    if x == 100: screen.blit(dis_level_kho,dis_level_kho_rect)
    if x == 80: screen.blit(dis_level_thuong,dis_level_thuong_rect)
    if x == 120: screen.blit(dis_level_sieukho,dis_level_sieukho_rect) 
screen = dis_screen()
clock = pygame.time.Clock()

game_active = True

bg = pygame.image.load(r"background-1.jpg")

fl = pygame.image.load(r"floor6.png")
fl = pygame.transform.scale2x(fl)
fl_x = 0 

bird_move = 0 
bird_down = pygame.image.load(r"birddown.png")
bird_mid = pygame.image.load(r"birddown.png")
bird_up = pygame.image.load(r"birdup.png")
bird_list = [bird_down,bird_mid,bird_up]
for i in range(0,3): bird_list[i] = pygame.transform.scale2x(bird_list[i])
bird_index = 0
bird = bird_list[bird_index]
bird_dis = bird.get_rect(center=(100,384))
birdflap= pygame.USEREVENT+1
pygame.time.set_timer(birdflap,200)

pipe_surface = pygame.transform.scale2x(pygame.image.load(r"pipe1.png"))
pipe_list = []
spawnpipe = pygame.USEREVENT
pygame.time.set_timer(spawnpipe,1200)

game_font = pygame.font.Font(r"04B_19.TTF",40)
score = 0
high_score = 0

game_welcome = pygame.image.load(r"welcome.png")
game_over_surface = pygame.image.load(r"end.png")
game_over_surface1 = pygame.transform.scale2x(pygame.image.load(r"pressspace.png"))
dis_level = pygame.image.load(r'level.png')
dis_level_de = pygame.image.load(r'level-de_transparent.png')
dis_level_thuong = pygame.image.load(r'level-thuong_transparent.png')
dis_level_kho = pygame.image.load(r'level-kho_transparent.png')
dis_level_sieukho = pygame.image.load(r'level-sieukho_transparent.png')
game_welcome_rect= game_welcome.get_rect(center=(648,150))
game_over_rect = game_over_surface.get_rect(center=(648,500))
game_over_rect1 = game_over_surface1.get_rect(center=(648,400))
dis_level_rect = dis_level.get_rect(center=(650,350))
dis_level_de_rect = dis_level_de.get_rect(center=(650,350))
dis_level_thuong_rect = dis_level_thuong.get_rect(center=(650,350))
dis_level_kho_rect = dis_level_kho.get_rect(center=(650,350))
dis_level_sieukho_rect = dis_level_sieukho.get_rect(center=(650,350))

flap_sound = pygame.mixer.Sound(r'sfx_wing.wav')
hit_sound = pygame.mixer.Sound(r'sfx_hit.wav')
score_sound = pygame.mixer.Sound(r'sfx_point.wav')
cnt = 0
press = 0

level = 60
check = True
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  
            exit()
        if event.type == pygame.KEYDOWN:
            if game_active == False or press == 1:
                if event.key == pygame.K_1:
                    level = 60
                    score_sound.play() 
                if event.key == pygame.K_2:
                    level = 80
                    score_sound.play() 
                if event.key == pygame.K_3:
                    level = 100
                    score_sound.play() 
                if event.key == pygame.K_4:
                    level = 120
                    score_sound.play() 
            if event.key == pygame.K_SPACE:
                press+=1
                bird_move = -9
                flap_sound.play()
            if event.key == pygame.K_SPACE and game_active==False:
                game_active=True
                pipe_list.clear()
                bird_dis.center = (100,384)
                bird_move = 0
                score = 0
        if event.type == spawnpipe: 
            pipe_list+=create_pipe()
        if event.type == birdflap:
            bird_index+=1 if bird_index<2 else 0
            bird, bird_dis = bird_animation()
    dis_background()
    if press == 0 or press == 1:
        if press==0: 
            screen.blit(game_over_surface1,game_over_rect1)
            screen.blit(game_welcome,game_welcome_rect)
        if press==1:
            screen.blit(dis_level,dis_level_rect) 
            show_level(level)
    else:
        if game_active==True: 
            dis_bird()  
            game_active = check_collision(pipe_list)
            dis_pipe(pipe_list) 
            score+=0.01
            cnt+=1
            if(cnt%100==0): score_sound.play() 
            dis_floor()
            dis_score(True)
        else:  
            screen.blit(game_over_surface,game_over_rect)
            screen.blit(dis_level,dis_level_rect)
            high_score = max(score,high_score)
            dis_score(False) 
            dis_floor()
            show_level(level)
    pygame.display.update()
    clock.tick(level)