import pygame
import sys
pygame.init()  # 初始化
bg_size = width, height = 908, 820  # 设置界面大小
screen = pygame.display.set_mode(bg_size)  # 设置界面
pygame.display.set_caption("五子棋")  # 设置标题
background_play = pygame.image.load(r"/Users/yaoyuhan/PycharmProjects/aaa/五子棋/background.jpg")  # 设置背景
# a = [[2] * 14 for decide in range(14)]
num = 14  # 棋盘大小，用于后续循环
a = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 0, 1, 1, 2, 2, 2, 2, 2, 2], [2, 2, 1, 2, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2], [2, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2], [2, 1, 0, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2], [2, 2, 1, 1, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2], [2, 2, 0, 0, 0, 1, 1, 0, 2, 2, 2, 2, 2, 2], [1, 1, 0, 1, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2], [0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2], [1, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 1, 0, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]


def draw_circle():
    global a
    for i in range(num):
        for j in range(num):
            if a[i][j] == 1:  # 画白棋
                pygame.draw.circle(screen, (255, 255, 255), (65 + 59 * j, 54 + 53 * i), 20, 0)
            if a[i][j] == 0:  # 画黑棋
                 pygame.draw.circle(screen, (0, 0, 0), (65 + 59 * j, 54 + 53 * i), 20, 0)


while True:
    screen.blit(background_play, (0, 0))  # 加载背景
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 退出整个游戏
            sys.exit()
    draw_circle()
    pygame.display.flip()
