import pygame, sys, random

pygame.init()

class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)
#Tỉ lệ màn hình
Width = 1280
Height = 900
SCREEN = pygame.display.set_mode((Width, Height))
surface = pygame.Surface((Width, Height), pygame.SRCALPHA)
#Tốc độ khung hình
fps = 60
timer = pygame.time.Clock()
timer.tick(fps)
#Bảng màu
WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (192,192,192)
GREEN = (0,255,0)
#Tiêu đề chương trình
pygame.display.set_caption("Menu")
#Background
BG = pygame.image.load("Image/Forest-and-Trees-Free-Pixel-Backgrounds5.png")
EBG = pygame.image.load("Image/easypic.png")
MBG = pygame.image.load("Image/mediumpic.png")
HBG = pygame.image.load("Image/hardpic.png")
#Icon
icon1 = pygame.image.load(r'Icon\bullfinch.png')
icon2 = pygame.image.load(r'Icon\clown-fish.png')
icon3 = pygame.image.load(r'Icon\crab.png')
icon4 = pygame.image.load(r'Icon\elephant.png')
icon5 = pygame.image.load(r'Icon\ladybug.png')
icon6 = pygame.image.load(r'Icon\lion.png')
icon7 = pygame.image.load(r'Icon\panda.png')
icon8 = pygame.image.load(r'Icon\sheep.png')
icon9 = pygame.image.load(r'Icon\whale.png')
icon10 = pygame.image.load(r'Icon\frog.png')
icon11 = pygame.image.load(r'Icon\turtle.png')
icon12 = pygame.image.load(r'Icon\rhino.png')
icon13 = pygame.image.load(r'Icon\penguin.png')
icon14 = pygame.image.load(r'Icon\hedgehog.png')
icon15 = pygame.image.load(r'Icon\owl.png')
icon16 = pygame.image.load(r'Icon\burger.png')
icon17 = pygame.image.load(r'Icon\pizza.png')
icon18 = pygame.image.load(r'Icon\pop-corn.png')
icon19 = pygame.image.load(r'Icon\pudding.png')
icon20 = pygame.image.load(r'Icon\strawberry.png')
icon21 = pygame.image.load(r'Icon\donut.png')

scaled_image1 = pygame.transform.scale(icon1, (70,70))
scaled_image2 = pygame.transform.scale(icon2, (70,70))
scaled_image3 = pygame.transform.scale(icon3, (70,70))
scaled_image4 = pygame.transform.scale(icon4, (70,70))
scaled_image5 = pygame.transform.scale(icon5, (70,70))
scaled_image6 = pygame.transform.scale(icon6, (70,70))
scaled_image7 = pygame.transform.scale(icon7, (70,70))
scaled_image8 = pygame.transform.scale(icon8, (70,70))
scaled_image9 = pygame.transform.scale(icon9, (70,70))
scaled_image10 = pygame.transform.scale(icon10, (70,70))
scaled_image11 = pygame.transform.scale(icon11, (70,70))
scaled_image12 = pygame.transform.scale(icon12, (70,70))
scaled_image13 = pygame.transform.scale(icon13, (70,70))
scaled_image14 = pygame.transform.scale(icon14, (70,70))
scaled_image15 = pygame.transform.scale(icon15, (70,70))
scaled_image16 = pygame.transform.scale(icon16, (70,70))
scaled_image17 = pygame.transform.scale(icon17, (70,70))
scaled_image18 = pygame.transform.scale(icon18, (70,70))
scaled_image19 = pygame.transform.scale(icon19, (70,70))
scaled_image20 = pygame.transform.scale(icon20, (70,70))
scaled_image21 = pygame.transform.scale(icon21, (70,70))
scaled_check = pygame.transform.scale(pygame.image.load('Icon/check.png'), (70,70))
scaled_error = pygame.transform.scale(pygame.image.load('Icon/error.png'), (70,70))
#Tiếng click chuột
click = pygame.mixer.Sound('Sound Effect/minimal-pop-click-ui-1-198301.mp3')
couple = pygame.mixer.Sound('Sound Effect/button-pressed-38129.mp3')
error = pygame.mixer.Sound('Sound Effect/error-10-206498.mp3')
win = pygame.mixer.Sound('Sound Effect/tada-234709.mp3')
lose = pygame.mixer.Sound('Sound Effect/game-over-arcade-6435.mp3')
countdown = pygame.mixer.Sound('Sound Effect/beepbeepbeep-53921.mp3')
#Các biến, mảng liên quan đến tạo hình và kiểm tra cặp chọn đúng
options_list = []
space = []
used = []
first_guess = False
second_guess = False
pause = False
volume_check = True
sfx_check = True
first_guess_num = 0
second_guess_num = 0
match = 0
#Design font chữ và cỡ chữ
def get_font(size): 
    return pygame.font.Font("font.ttf", size)
#Dừng lại
def Pause():
    if pause:
        pygame.draw.rect(surface, (128, 128, 128, 150), [0, 0, Width, Height])
        SCREEN.blit(surface, (0,0))
        OPTIONS_TEXT = get_font(45).render("Press any key to continue.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 450))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
#Countdown
def Count_down(n, z):
    if n <= 5:
        countdown.play()
        countdown.set_volume(0.3)
    if n == 0 or z == 0:
        countdown.set_volume(0)
        Lose()
#Chiến thắng
def Winner():
    global win
    while True:
        win.play()
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        WIN_TEXT = get_font(45).render("You win!!!!", True, "Black")
        WIN_RECT = WIN_TEXT.get_rect(center=(640, 260))
        REPLAY_TEXT = get_font(30).render("Click PLAY AGAIN to play.", True, "Black")
        REPLAY_RECT = REPLAY_TEXT.get_rect(center=(600, 300))
        SCREEN.blit(WIN_TEXT, WIN_RECT)
        SCREEN.blit(REPLAY_TEXT, REPLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="PLAY AGAIN", font=get_font(75), base_color="Black", hovering_color="Green")

        PLAY_BACK.changeColor(OPTIONS_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    click.play()
                    play()

        pygame.display.update()

def Lose():
    global lose
    while True:
        lose.play()
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        LOSE_TEXT = get_font(45).render("You lose!!!!", True, "Black")
        LOSE_RECT = LOSE_TEXT.get_rect(center=(640, 260))
        REPLAY_TEXT = get_font(30).render("Click PLAY AGAIN to play.", True, "Black")
        REPLAY_RECT = REPLAY_TEXT.get_rect(center=(600, 300))
        SCREEN.blit(LOSE_TEXT, LOSE_RECT)
        SCREEN.blit(REPLAY_TEXT, REPLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="PLAY AGAIN", font=get_font(75), base_color="Black", hovering_color="Green")

        PLAY_BACK.changeColor(OPTIONS_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    click.play()
                    play()

        pygame.display.update()
#Chế độ dễ
def easy():
    pygame.display.set_caption("Easy")

    global options_list, space, used, first_guess, second_guess, first_guess_num, second_guess_num, match, correct, error, countdown, click, pause, volume_check
    score = 10
    #Gán các icon
    image = [scaled_image1, scaled_image2, scaled_image3, scaled_image4, scaled_image5, scaled_image6, scaled_image7, scaled_image8]

    #Nhạc nền chế độ chơi
    if volume_check:
        pygame.mixer_music.load('Sound Effect/funny-bgm-240795.mp3')
        pygame.mixer_music.set_volume(0.2)
        pygame.mixer_music.play(-1)

    #Tạo 1 bảng với 4 cột, 4 dòng
    rows = 4
    cols = 4

    #1 mảng correct sẽ thay đổi khi chọn đúng 1 cặp
    correct = [[0,0,0,0],
               [0,0,0,0],
               [0,0,0,0],
               [0,0,0,0]]
    
    #Thời gian trò chơi
    current_seconds = 60
    pygame.time.set_timer(pygame.USEREVENT, 1000)

    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(EBG,(0,0))

         #Phân danh sách thành cặp
        for item in range(rows*cols//2):
            options_list.append(item)

        #Thêm 2 lần danh sách -> 1 cặp theo thứ tự ngẫu nhiên vào mảng rỗng
        for item in range(rows*cols):
            piece = options_list[random.randint(0, len(options_list)-1)]
            space.append(piece)
            #Sau khi thêm lần 2 sẽ kiểm tra nếu xuất hiện giá trị piece đã có trong mảng used thì sẽ lập tức xóa giá trị đó trong mảng cặp option_list
            if piece in used:
                used.remove(piece)
                options_list.remove(piece)
            else:
                used.append(piece)

        #Countdown
        if current_seconds >=0:
            seconds = current_seconds % 60
            minute = int(current_seconds/60)

        #Vẽ khung trò chơi
        top_menu = pygame.draw.rect(SCREEN, BLACK, [0,0,Width,110], 4, 15)
        title_button = pygame.draw.rect(SCREEN, GRAY, [580,10,130,40],0,15)
        restart_button = pygame.draw.rect(SCREEN, GRAY, [30,5,230,40],0,15)
        mainmenu_button = pygame.draw.rect(SCREEN, GRAY, [30,55,300,40],0,15)
        life_button = pygame.draw.rect(SCREEN, GRAY, [1010,10,260,40],0,15)
        time_button = pygame.draw.rect(SCREEN, GRAY, [970,60,300,40],0,15)
        pause_button = pygame.draw.rect(SCREEN, GRAY, [620,55,50,40],0,15)
        play_rect = pygame.draw.rect(SCREEN, BLACK, [300,250,700,600],4,5)
        timer_text = get_font(25).render(f'Time: {minute:02}:{seconds:02}', True, BLACK)
        title_text = get_font(25).render('Easy',True,BLACK)
        restart_text = get_font(30).render('Restart', True, BLACK)
        mainmenu_text = get_font(30).render('Main Menu', True, BLACK)
        life_text = get_font(25).render(f'Life:  {score}', True, BLACK)
        pause_text = get_font(15).render('||', True, BLACK)
        SCREEN.blit(title_text, (600,20))
        SCREEN.blit(life_text, (1025,20))
        SCREEN.blit(restart_text, (45,10))
        SCREEN.blit(timer_text, (980,70))
        SCREEN.blit(mainmenu_text, (45,60))
        SCREEN.blit(pause_text, (630,70))

        #Vẽ hình
        board_list = []

        #Vẽ các hình theo tỉ lệ cho trước
        for i in range(cols):
            for j in range (rows):
                piece = pygame.draw.rect(SCREEN, WHITE, (i*150 + 390, j*140 + 300, 100,100),0,10)
                board_list.append(piece)
        #Khi chọn đúng 1 cặp đúng sẽ vẽ viền xanh lá xung quanh 2 hình
        for r in range(rows):
            for c in range(cols):
                if correct[r][c] == 1:
                    image_index = space[c * rows + r]
                    hinh = image[image_index]
                    SCREEN.blit(hinh, (c*150 + 405, r*140 + 315))
                    pygame.draw.rect(SCREEN, GREEN, [c*150 +387, r*140 + 300, 105,105],5,12)

        #Kiểm tra cặp khi 2 hình được nhấn                   
        if first_guess and second_guess:
            if(space[first_guess_num] == space[second_guess_num]):
                col1 = first_guess_num // rows
                col2 = second_guess_num // rows
                row1 = first_guess_num - (first_guess_num // rows * rows)
                row2 = second_guess_num - (second_guess_num // rows * rows)
                if(correct[row1][col1] == 0 and correct[row2][col2]==0):
                    correct[row1][col1] = 1
                    correct[row2][col2] = 1
                    match +=1
                    couple.play()  
            else:
                score -=1
                error.play()
            pygame.time.delay(150)
            first_guess = False
            second_guess = False 
        #Xử lí sự kiện (Đếm ngược, thoát, click chuột)
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT and not pause:
                current_seconds-=1
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if pause_button.collidepoint(event.pos):
                        if not pause:
                            pygame.mixer_music.pause()
                            pause = True
            if event.type == pygame.KEYDOWN:
                if pause == True:
                    pygame.mixer_music.unpause()
                    pause = False
            if event.type == pygame.MOUSEBUTTONDOWN and not pause:
                if event.button ==1:
                    click.play()
                    for i in range(len(board_list)):
                        button = board_list[i]
                        if button.collidepoint(event.pos) and not first_guess:
                            first_guess = True
                            first_guess_num = i
                        if button.collidepoint(event.pos) and not second_guess and first_guess and i != first_guess_num:
                            second_guess = True
                            second_guess_num = i
                    if restart_button.collidepoint(event.pos):
                        options_list = []
                        used = []
                        space = []
                        first_guess = False
                        second_guess = False
                        first_guess_num = 0
                        second_guess_num = 0
                        score = 10
                        match = 0
                        correct = [[0,0,0,0],
                                   [0,0,0,0],
                                   [0,0,0,0],
                                   [0,0,0,0]]
                        current_seconds = 60
                    if mainmenu_button.collidepoint(event.pos):
                        main_menu()
        #Chiến thắng
        if match == rows * cols //2:
            #Màn hình xuất hiện khi chiến thắng
            SCREEN.fill("white")
            Winner_TEXT = get_font(45).render(f"You win with: {score}", True, "Black")
            Winner_RECT = Winner_TEXT.get_rect(center=(640, 260))
            SCREEN.blit(Winner_TEXT, Winner_RECT)
            PLAY_AGAIN = Button(image=None, pos=(640, 460), 
                    text_input="PLAY AGAIN", font=get_font(40), base_color="Black", hovering_color="Green")
            PLAY_AGAIN.changeColor(OPTIONS_MOUSE_POS)
            PLAY_AGAIN.update(SCREEN)

            #Reset lại game
            options_list = []
            used = []
            space = []
            first_guess = False
            second_guess = False
            first_guess_num = 0
            second_guess_num = 0
            score = 10
            match = 0
            correct = [[0,0,0,0],
                        [0,0,0,0],
                        [0,0,0,0],
                        [0,0,0,0]]
            current_seconds = 60 
            Winner()     
        
        if first_guess:
            image_index = space[first_guess_num]
            hinh = image[image_index]
            location = (first_guess_num // rows *150 + 405, (first_guess_num -(first_guess_num // rows * rows))*140 + 315)
            SCREEN.blit(hinh, (location))

        if second_guess:
            image_index = space[second_guess_num]
            hinh = image[image_index]
            location = (second_guess_num // rows *150 + 405, (second_guess_num -(second_guess_num // rows * rows))*140 + 315)
            SCREEN.blit(hinh, (location))
        
        #Đếm ngược và thua cuộc              
        Count_down(current_seconds, score)

        #Dừng lại
        Pause()

        pygame.display.update()
#Chế độ trung bình
def medium():
    pygame.display.set_caption("Medium")

    global options_list, space, used, first_guess, second_guess, first_guess_num, second_guess_num, match, correct, error, countdown, click, pause, volume_check
    score = 20
    #Gán các icon
    image = [scaled_image1, scaled_image2, scaled_image3, scaled_image4, scaled_image5, scaled_image6, scaled_image7, scaled_image8, scaled_image9, scaled_image10, scaled_image11, scaled_image12, scaled_image13, scaled_image14, scaled_image15]

    #Nhạc nền chế độ chơi
    if volume_check:
        pygame.mixer_music.load('Sound Effect/funny-bgm-240795.mp3')
        pygame.mixer_music.set_volume(0.2)
        pygame.mixer_music.play(-1)

    #Tạo 1 bảng với 4 cột, 4 dòng
    rows = 5
    cols = 6

    #1 mảng correct sẽ thay đổi khi chọn đúng 1 cặp
    correct = [[0,0,0,0,0,0],
               [0,0,0,0,0,0],
               [0,0,0,0,0,0],
               [0,0,0,0,0,0],
               [0,0,0,0,0,0]]
    
    #Thời gian trò chơi
    current_seconds = 150
    pygame.time.set_timer(pygame.USEREVENT, 1000)

    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(MBG,(0,0))

         #Phân danh sách thành cặp
        for item in range(rows*cols//2):
            options_list.append(item)

        #Thêm 2 lần danh sách -> 1 cặp theo thứ tự ngẫu nhiên vào mảng rỗng
        for item in range(rows*cols):
            piece = options_list[random.randint(0, len(options_list)-1)]
            space.append(piece)
            #Sau khi thêm lần 2 sẽ kiểm tra nếu xuất hiện giá trị piece đã có trong mảng used thì sẽ lập tức xóa giá trị đó trong mảng cặp option_list
            if piece in used:
                used.remove(piece)
                options_list.remove(piece)
            else:
                used.append(piece)

        #Countdown
        if current_seconds >=0:
            seconds = current_seconds % 60
            minute = int(current_seconds/60)

        #Vẽ khung trò chơi
        top_menu = pygame.draw.rect(SCREEN, BLACK, [0,0,Width,110], 4, 15)
        title_button = pygame.draw.rect(SCREEN, GRAY, [550,10,180,40],0,15)
        restart_button = pygame.draw.rect(SCREEN, GRAY, [30,5,230,40],0,15)
        mainmenu_button = pygame.draw.rect(SCREEN, GRAY, [30,55,300,40],0,15)
        score_button = pygame.draw.rect(SCREEN, GRAY, [1010,10,260,40],0,15)
        time_button = pygame.draw.rect(SCREEN, GRAY, [970,60,300,40],0,15)
        pause_button = pygame.draw.rect(SCREEN, GRAY, [620,55,50,40],0,15)
        play_rect = pygame.draw.rect(SCREEN, BLACK, [240,175,800,630],4,5)
        timer_text = get_font(25).render(f'Time: {minute:02}:{seconds:02}', True, BLACK)
        title_text = get_font(25).render('Medium',True,BLACK)
        restart_text = get_font(30).render('Restart', True, BLACK)
        mainmenu_text = get_font(30).render('Main Menu', True, BLACK)
        score_text = get_font(25).render(f'Life:  {score}', True, BLACK)
        pause_text = get_font(15).render('||', True, BLACK)
        SCREEN.blit(title_text, (570,20))
        SCREEN.blit(score_text, (1025,20))
        SCREEN.blit(restart_text, (45,10))
        SCREEN.blit(timer_text, (980,70))
        SCREEN.blit(mainmenu_text, (45,60))
        SCREEN.blit(pause_text, (630,70))

        #Vẽ hình
        board_list = []

        #Vẽ các hình theo tỉ lệ cho trước
        for i in range(cols):
            for j in range (rows):
                piece = pygame.draw.rect(SCREEN, WHITE, (i*130 + 265, j*120 + 200, 100,100),0,10)
                board_list.append(piece)
        #Khi chọn đúng 1 cặp đúng sẽ vẽ viền xanh lá xung quanh 2 hình
        for r in range(rows):
            for c in range(cols):
                if correct[r][c] == 1:
                    image_index = space[c * rows + r]
                    hinh = image[image_index]
                    SCREEN.blit(hinh, (c*130 + 280, r*120 + 220))
                    pygame.draw.rect(SCREEN, GREEN, [c*130 +262, r*120 + 200, 105,105],5,12)

        #Kiểm tra cặp khi 2 hình được nhấn                   
        if first_guess and second_guess:
            if(space[first_guess_num] == space[second_guess_num]):
                col1 = first_guess_num // rows
                col2 = second_guess_num // rows
                row1 = first_guess_num - (first_guess_num // rows * rows)
                row2 = second_guess_num - (second_guess_num // rows * rows)
                if(correct[row1][col1] == 0 and correct[row2][col2]==0):
                    correct[row1][col1] = 1
                    correct[row2][col2] = 1
                    match +=1
                    couple.play()  
            else:
                score -=1
                error.play()
            pygame.time.delay(150)
            first_guess = False
            second_guess = False 
            
        #Xử lí sự kiện (Đếm ngược, thoát, click chuột)
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT and not pause:
                current_seconds-=1
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if pause_button.collidepoint(event.pos):
                        if not pause:
                            pygame.mixer_music.pause()
                            pause = True
            if event.type == pygame.KEYDOWN:
                if pause == True:
                    pygame.mixer_music.unpause()
                    pause = False
            if event.type == pygame.MOUSEBUTTONDOWN and not pause:
                if event.button ==1:
                    click.play()
                    for i in range(len(board_list)):
                        button = board_list[i]
                        if button.collidepoint(event.pos) and not first_guess:
                            first_guess = True
                            first_guess_num = i
                        if button.collidepoint(event.pos) and not second_guess and first_guess and i != first_guess_num:
                            second_guess = True
                            second_guess_num = i
                    if restart_button.collidepoint(event.pos):
                        options_list = []
                        used = []
                        space = []
                        first_guess = False
                        second_guess = False
                        first_guess_num = 0
                        second_guess_num = 0
                        score = 20
                        match = 0
                        correct = [[0,0,0,0,0,0],
                                   [0,0,0,0,0,0],
                                   [0,0,0,0,0,0],
                                   [0,0,0,0,0,0],
                                   [0,0,0,0,0,0]]
                        current_seconds = 150
                    if mainmenu_button.collidepoint(event.pos):
                        main_menu()
        #Chiến thắng
        if match == rows * cols //2:
            #Màn hình xuất hiện khi chiến thắng
            SCREEN.fill("white")
            Winner_TEXT = get_font(45).render(f"You win with: {score}", True, "Black")
            Winner_RECT = Winner_TEXT.get_rect(center=(640, 260))
            SCREEN.blit(Winner_TEXT, Winner_RECT)
            PLAY_AGAIN = Button(image=None, pos=(640, 460), 
                    text_input="PLAY AGAIN", font=get_font(40), base_color="Black", hovering_color="Green")
            PLAY_AGAIN.changeColor(OPTIONS_MOUSE_POS)
            PLAY_AGAIN.update(SCREEN)

            #Reset lại game
            options_list = []
            used = []
            space = []
            first_guess = False
            second_guess = False
            first_guess_num = 0
            second_guess_num = 0
            score = 20
            match = 0
            correct = [[0,0,0,0,0,0],
                       [0,0,0,0,0,0],
                       [0,0,0,0,0,0],
                       [0,0,0,0,0,0],
                       [0,0,0,0,0,0]]
            current_seconds = 150  
            pygame.mixer_music.pause()
            Winner()     
        
        if first_guess:
            image_index = space[first_guess_num]
            hinh = image[image_index]
            location = (first_guess_num // rows *130 + 280, (first_guess_num -(first_guess_num // rows * rows))*120 + 220)
            SCREEN.blit(hinh, (location))

        if second_guess:
            image_index = space[second_guess_num]
            hinh = image[image_index]
            location = (second_guess_num // rows *130 + 280, (second_guess_num -(second_guess_num // rows * rows))*120 + 220)
            SCREEN.blit(hinh, (location))
        
        #Đếm ngược và thua cuộc              
        Count_down(current_seconds,score)
        #Dừng lại
        Pause()

        pygame.display.update()
#Chế độ khó
def hard():
    pygame.display.set_caption("Hard")

    global options_list, space, used, first_guess, second_guess, first_guess_num, second_guess_num, match, correct, error, countdown, click, pause, volume_check
    score = 30
    #Gán các icon
    image = [scaled_image1, scaled_image2, scaled_image3, scaled_image4, scaled_image5, scaled_image6, scaled_image7, scaled_image8, scaled_image9, scaled_image10, scaled_image11, scaled_image12, scaled_image13, scaled_image14, scaled_image15, scaled_image16, scaled_image17, scaled_image18, scaled_image19, scaled_image20,scaled_image21]

    #Nhạc nền chế độ chơi
    if volume_check:
        pygame.mixer_music.load('Sound Effect/funny-bgm-240795.mp3')
        pygame.mixer_music.set_volume(0.2)
        pygame.mixer_music.play(-1)

    #Tạo 1 bảng với 4 cột, 4 dòng
    rows = 6
    cols = 7

    #1 mảng correct sẽ thay đổi khi chọn đúng 1 cặp
    correct = [[0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0]]
    
    #Thời gian trò chơi
    current_seconds = 300
    pygame.time.set_timer(pygame.USEREVENT, 1000)

    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(HBG,(0,0))

         #Phân danh sách thành cặp
        for item in range(rows*cols//2):
            options_list.append(item)

        #Thêm 2 lần danh sách -> 1 cặp theo thứ tự ngẫu nhiên vào mảng rỗng
        for item in range(rows*cols):
            piece = options_list[random.randint(0, len(options_list)-1)]
            space.append(piece)
            #Sau khi thêm lần 2 sẽ kiểm tra nếu xuất hiện giá trị piece đã có trong mảng used thì sẽ lập tức xóa giá trị đó trong mảng cặp option_list
            if piece in used:
                used.remove(piece)
                options_list.remove(piece)
            else:
                used.append(piece)

        #Countdown
        if current_seconds >=0:
            seconds = current_seconds % 60
            minute = int(current_seconds/60)

        #Vẽ khung trò chơi
        top_menu = pygame.draw.rect(SCREEN, BLACK, [0,0,Width,110], 4, 15)
        title_button = pygame.draw.rect(SCREEN, GRAY, [570,10,140,40],0,15)
        restart_button = pygame.draw.rect(SCREEN, GRAY, [30,5,230,40],0,15)
        mainmenu_button = pygame.draw.rect(SCREEN, GRAY, [30,55,300,40],0,15)
        score_button = pygame.draw.rect(SCREEN, GRAY, [1010,10,260,40],0,15)
        time_button = pygame.draw.rect(SCREEN, GRAY, [970,60,300,40],0,15)
        pause_button = pygame.draw.rect(SCREEN, GRAY, [620,55,50,40],0,15)
        play_rect = pygame.draw.rect(SCREEN, BLACK, [180,130,860,740],4,5)
        timer_text = get_font(25).render(f'Time: {minute:02}:{seconds:02}', True, BLACK)
        title_text = get_font(25).render('Hard',True,BLACK)
        restart_text = get_font(30).render('Restart', True, BLACK)
        mainmenu_text = get_font(30).render('Main Menu', True, BLACK)
        score_text = get_font(25).render(f'Life:  {score}', True, BLACK)
        pause_text = get_font(15).render('||', True, BLACK)
        SCREEN.blit(title_text, (590,20))
        SCREEN.blit(score_text, (1025,20))
        SCREEN.blit(restart_text, (45,10))
        SCREEN.blit(timer_text, (980,70))
        SCREEN.blit(mainmenu_text, (45,60))
        SCREEN.blit(pause_text, (630,70))

        #Vẽ hình
        board_list = []

        #Vẽ các hình theo tỉ lệ cho trước
        for i in range(cols):
            for j in range (rows):
                piece = pygame.draw.rect(SCREEN, WHITE, (i*120 + 200, j*120 + 150, 100,100),0,10)
                board_list.append(piece)
        #Khi chọn đúng 1 cặp đúng sẽ vẽ viền xanh lá xung quanh 2 hình
        for r in range(rows):
            for c in range(cols):
                if correct[r][c] == 1:
                    image_index = space[c * rows + r]
                    hinh = image[image_index]
                    SCREEN.blit(hinh, (c*120 + 215, r*120 + 165))
                    pygame.draw.rect(SCREEN, GREEN, [c*120 +197, r*120 + 150, 105,105],5,12)

        #Kiểm tra cặp khi 2 hình được nhấn                   
        if first_guess and second_guess:
            if(space[first_guess_num] == space[second_guess_num]):
                col1 = first_guess_num // rows
                col2 = second_guess_num // rows
                row1 = first_guess_num - (first_guess_num // rows * rows)
                row2 = second_guess_num - (second_guess_num // rows * rows)
                if(correct[row1][col1] == 0 and correct[row2][col2]==0):
                    correct[row1][col1] = 1
                    correct[row2][col2] = 1
                    match +=1
                    couple.play()  
            else:
                score -=1
                error.play()
            pygame.time.delay(150)
            first_guess = False
            second_guess = False 
            
        #Xử lí sự kiện (Đếm ngược, thoát, click chuột)
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT and not pause:
                current_seconds-=1
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if pause_button.collidepoint(event.pos):
                        if not pause:
                            pygame.mixer_music.pause()
                            pause = True
            if event.type == pygame.KEYDOWN:
                if pause == True:
                    pygame.mixer_music.unpause()
                    pause = False
            if event.type == pygame.MOUSEBUTTONDOWN and not pause:
                if event.button ==1:
                    click.play()
                    for i in range(len(board_list)):
                        button = board_list[i]
                        if button.collidepoint(event.pos) and not first_guess:
                            first_guess = True
                            first_guess_num = i
                        if button.collidepoint(event.pos) and not second_guess and first_guess and i != first_guess_num:
                            second_guess = True
                            second_guess_num = i
                    if restart_button.collidepoint(event.pos):
                        options_list = []
                        used = []
                        space = []
                        first_guess = False
                        second_guess = False
                        first_guess_num = 0
                        second_guess_num = 0
                        score = 30
                        match = 0
                        correct = [[0,0,0,0,0,0,0],
                                   [0,0,0,0,0,0,0],
                                   [0,0,0,0,0,0,0],
                                   [0,0,0,0,0,0,0],
                                   [0,0,0,0,0,0,0],
                                   [0,0,0,0,0,0,0]]
                        current_seconds = 300
                    if mainmenu_button.collidepoint(event.pos):
                        main_menu()
        #Chiến thắng
        if match == rows * cols //2:
            #Màn hình xuất hiện khi chiến thắng
            SCREEN.fill("white")
            Winner_TEXT = get_font(45).render(f"You win with: {score}", True, "Black")
            Winner_RECT = Winner_TEXT.get_rect(center=(640, 260))
            SCREEN.blit(Winner_TEXT, Winner_RECT)
            PLAY_AGAIN = Button(image=None, pos=(640, 460), 
                    text_input="PLAY AGAIN", font=get_font(40), base_color="Black", hovering_color="Green")
            PLAY_AGAIN.changeColor(OPTIONS_MOUSE_POS)
            PLAY_AGAIN.update(SCREEN)

            #Reset lại game
            options_list = []
            used = []
            space = []
            first_guess = False
            second_guess = False
            first_guess_num = 0
            second_guess_num = 0
            score = 30
            match = 0
            correct = [[0,0,0,0,0,0],
                       [0,0,0,0,0,0],
                       [0,0,0,0,0,0],
                       [0,0,0,0,0,0],
                       [0,0,0,0,0,0]]
            current_seconds = 300 
            pygame.mixer_music.pause()
            Winner()     
        
        if first_guess:
            image_index = space[first_guess_num]
            hinh = image[image_index]
            location = (first_guess_num // rows *120 + 215, (first_guess_num -(first_guess_num // rows * rows))*120 + 162)
            SCREEN.blit(hinh, (location))

        if second_guess:
            image_index = space[second_guess_num]
            hinh = image[image_index]
            location = (second_guess_num // rows *120 + 215, (second_guess_num -(second_guess_num // rows * rows))*120 + 162)
            SCREEN.blit(hinh, (location))
        
        #Đếm ngược và thua cuộc              
        Count_down(current_seconds,score)
        #Dừng lại
        Pause()

        pygame.display.update()
#Chọn chế độ chơi
def play(): 
    while True:
        SCREEN.blit(BG, (0, 0))

        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        EASY_BUTTON = Button(image=pygame.image.load("Image/Play Rect.png"), pos=(640, 300), 
                            text_input="EASY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        MEDIUM_BUTTON = Button(image=pygame.image.load("Image/Options Rect.png"), pos=(640, 450), 
                            text_input="MEDIUM", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        HARD_BUTTON = Button(image=pygame.image.load("Image/Play Rect.png"), pos=(640, 600), 
                            text_input="HARD", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        EASY_BUTTON.changeColor(PLAY_MOUSE_POS)
        EASY_BUTTON.update(SCREEN)
        MEDIUM_BUTTON.changeColor(PLAY_MOUSE_POS)
        MEDIUM_BUTTON.update(SCREEN)
        HARD_BUTTON.changeColor(PLAY_MOUSE_POS)
        HARD_BUTTON.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    click.play()
                    if EASY_BUTTON.checkForInput(PLAY_MOUSE_POS):
                        easy()
                    if MEDIUM_BUTTON.checkForInput(PLAY_MOUSE_POS):
                        medium()
                    if HARD_BUTTON.checkForInput(PLAY_MOUSE_POS):
                        hard()

        pygame.display.update()
#Cài đặt âm thanh game  
def options():
    global volume_check, scaled_check, scaled_error, sfx_check, click, couple, win, lose, error, countdown
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        VOLUME_TEXT = get_font(45).render("Change volume", True, "Black")
        VOLUME_RECT = VOLUME_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(VOLUME_TEXT, VOLUME_RECT)

        SOUND_TEXT = get_font(45).render("Music", True, "Black")
        SOUND_RECT = SOUND_TEXT.get_rect(center=(250, 220))
        SCREEN.blit(SOUND_TEXT, SOUND_RECT)

        SFX_TEXT = get_font(45).render("SFX", True, "Black")
        SFX_RECT = SFX_TEXT.get_rect(center=(900, 220))
        SCREEN.blit(SFX_TEXT, SFX_RECT)

        pygame.draw.rect(SCREEN, GRAY, [380,185,75,75])
        pygame.draw.rect(SCREEN, GRAY, [995,185,75,75])
        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")
        VOLUME_BACK = Button(image=scaled_check, pos=(420, 220), 
                            text_input='', font=get_font(10), base_color="Black", hovering_color="Green")
        SFX_BACK = Button(image=scaled_check, pos=(1035, 220), 
                            text_input="", font=get_font(40), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)
        VOLUME_BACK.update(SCREEN)
        SFX_BACK.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click.play()
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        main_menu()
                    if VOLUME_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        volume_check = not volume_check
                        if volume_check:
                            pygame.mixer_music.play(-1)  # Bật lại nhạc
                        else:
                            pygame.mixer_music.stop()  # Tắt nhạc
                    if SFX_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        sfx_check = not sfx_check
                        if sfx_check:
                            click.set_volume(1)
                            couple.set_volume(1)
                            error.set_volume(1)
                            win.set_volume(1)
                            lose.set_volume(1)
                            countdown.set_volume(1)
                        else:
                            click.set_volume(0)
                            couple.set_volume(0)
                            error.set_volume(0)
                            win.set_volume(0)
                            lose.set_volume(0)
                            countdown.set_volume(0)
          
        pygame.display.update()
       
#Menu  
def main_menu():
    global volume_check
    if volume_check:
        pygame.mixer_music.load('Sound Effect/quirky-documentary-199161.mp3')
        pygame.mixer_music.set_volume(0.2)
        pygame.mixer_music.play(-1)
    while True:

        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("Image/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("Image/Options Rect.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Image/Play Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    click.play()
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        play()
                    if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        options()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()
        
        pygame.display.update()

main_menu()
pygame.display.flip()