import pygame
import sys
import random

pygame.init()  # 初始化
bg_size = width, height = 1340, 1202  # 设置界面大小
screen = pygame.display.set_mode(bg_size)  # 设置界面
pygame.display.set_caption("五子棋")  # 设置标题
background_play = pygame.image.load(r"background.jpg")  # 设置背景
background_menu = pygame.image.load(r'title.png')
menu = 1
play_part1 = 0
play_part2 = 0
score = 0


def judge_win():
    global x, num, play_part1,  play_part2, score
    for i in range(num):  # 一列上有五个相同点
        for j in range(2, num - 2):
            if a[i][j - 1] == a[i][j] and a[i][j] == a[i][j + 1] and a[i][j - 2] == a[i][j] \
                    and a[i][j] == a[i][j + 2] and a[i][j] != 2:
                x = a[i][j]
    for i in range(2, num - 2):  # 一行中有五个相同点
        for j in range(num):
            if a[i - 1][j] == a[i][j] and a[i + 1][j] == a[i][j] and a[i - 2][j] == a[i][j] \
                    and a[i + 2][j] == a[i][j] and a[i][j] != 2:
                x = a[i][j]
    for i in range(2, num - 2):  # 斜线上有五个相同点
        for j in range(2, num - 2):
            if a[i][j] == a[i - 1][j - 1] and a[i][j] == a[i + 1][j + 1] and a[i][j] == a[i - 2][j - 2] \
                    and a[i][j] == a[i + 2][j + 2] and a[i][j] != 2:
                x = a[i][j]
            elif a[i][j] == a[i + 1][j - 1] and a[i][j] == a[i - 1][j + 1] and a[i][j] == a[i + 2][j - 2] \
                    and a[i][j] == a[i - 2][j + 2] and a[i][j] != 2:
                x = a[i][j]
    if x == 1:
        play_part1 = 0
        play_part2 = 0
        score = 1
        print("player2 win")
    elif x == 0:
        play_part1 = 0
        play_part2 = 0
        score = 1
        print("player1 win")


def draw_circle():
    global a
    for i in range(num):
        for j in range(num):
            if a[i][j] == 1:  # 画白棋
                pygame.draw.circle(screen, (255, 255, 255), (96 + 87 * j, 100 + 77 * i), 30, 0)
            if a[i][j] == 0:  # 画黑棋
                pygame.draw.circle(screen, (0, 0, 0), (96 + 87 * j, 100 + 77 * i), 30, 0)


def auto_one(coordinate_x, coordinate_y):
    count = 0
    global num, a
    b = [[0] * 3 for example in range(3)]
    b[1][1] = 9
    for i in range(3):
        for j in range(3):
            if coordinate_x == 0:
                b[0][j] = 9
            elif coordinate_x == num - 1:
                b[2][j] = 9
            if coordinate_y == 0:
                b[i][0] = 9
            elif coordinate_y == num - 1:
                b[i][2] = 9
    for i in range(3):
        for j in range(3):
            if b[i][j] == 0 and a[coordinate_x + i - 1][coordinate_y + j - 1] == 2:
                count += 1
                b[i][j] = count
    if count == 0:
        print("game over")
    else:
        ran_x = random.randint(1, count)
    print(b)
    print(ran_x)
    for i in range(3):
        for j in range(3):
            if b[i][j] == ran_x:
                print("i = " + str(i)+"  j = " + str(j))
                a[coordinate_x + i - 1][coordinate_y + j - 1] = 1
                print("现在坐标 = " + str(coordinate_x + i - 1)+" ," + str(coordinate_y + j - 1))


class Button():
    def __init__(self, screen, pos_y, msg,):
        """Initialize button attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.pos_y = pos_y

        # Set the dimensions and properties of the button.
        self.pos_x = 500
        self.width, self.height = 400, 150
        self.button_color = (210, 105, 30)  # 巧克力色：d2691e
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 60)

        # Build the button's rect object, and center it.
        self.rect = pygame.draw.rect(screen, (0, 0, 255), ((self.pos_x, self.pos_y), (self.width, self.height)), 0)

        # The button message only needs to be prepped once.
        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button, then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


single_button = Button(screen, 100, "single player")
double_button = Button(screen, 400, "double players")
quit_button = Button(screen, 700, "Quit")
player1_win = Button(screen, 400, "player1 win")
player2_win = Button(screen, 400, "player2 win")
bug = Button(screen, 400, "yyh win!")

while True:
    while menu:
        screen.blit(background_menu, (0, 0))
        x = 2  # 判断是否赢棋，0为黑胜，1为白胜
        a = [[2] * 14 for decide in range(14)]  # 创建矩阵作为棋盘
        num = 14  # 棋盘大小，用于后续循环
        now = 0  # 当前下棋方，0为黑色，1为白色
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 退出整个游戏
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:  # 获取鼠标坐标
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 500 <= mouse_x <= 900 and 100 <= mouse_y <= 250:
                    menu = 0
                    play_part1 = 1
                if 500 <= mouse_x <= 900 and 400 <= mouse_y <= 550:
                    menu = 0
                    play_part2 = 1
                if 500 <= mouse_x <= 900 and 700 <= mouse_y <= 850:
                    sys.exit()
        single_button.draw_button()
        double_button.draw_button()
        quit_button.draw_button()
        pygame.display.flip()
    while play_part1:
        screen.blit(background_play, (0, 0))  # 加载背景
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 退出整个游戏
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:  # 获取鼠标坐标
                mouse_x, mouse_y = pygame.mouse.get_pos()
                m = int((mouse_x - 66) / 87)  # 计算点格坐标
                n = int((mouse_y - 70) / 77)
                if a[n][m] == 2:  # 当该坐标为空时，将该坐标变为黑子
                    a[n][m] = 0
                    auto_one(n, m)
                    print(a)
        draw_circle()
        judge_win()
        pygame.display.flip()
    while play_part2:
        screen.blit(background_play, (0, 0))  # 加载背景
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 退出整个游戏
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:  # 获取鼠标坐标
                mouse_x, mouse_y = pygame.mouse.get_pos()
                m = int((mouse_x - 66) / 87)  # 计算点格坐标
                n = int((mouse_y - 70) / 77)
                if a[n][m] == 2:  # 当该坐标为空时，将该坐标变为黑子or白子
                    a[n][m] = now % 2
                    now += 1  # 更新当前棋子，保证下一次颜色不一样
                    print(a)
        draw_circle()
        judge_win()
        pygame.display.flip()
    while score:
        if x == 0:
            player1_win.draw_button()
        else:
            player2_win.draw_button()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 退出整个游戏
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:  # 获取鼠标坐标
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if mouse_x > 0:
                    score = 0
                    menu = 1
        pygame.display.flip()
