import random
import sys
import pygame
import time

pygame.init()  # 初始化
bg_size = width, height = 390, 650  # 设置界面大小
screen = pygame.display.set_mode(bg_size)  # 设置界面
pygame.display.set_caption("井字棋")  # 设置游戏标题
title = 1    # 加载logo
menu = single = double = result_1 = result_2 = result_3 = 0   # 不加载其余页面


class Button():
    def __init__(self, screen, pos_y, msg, button_color, text_color):
        """ 初始化参数 """
        self.screen = screen
        self.pos_y = pos_y
        self.msg = msg
        self.button_color = button_color
        self.text_color = text_color

        """ 设置固定参数 """
        self.pos_x = 100
        self.width, self.height = 200, 100
        self.font = pygame.font.SysFont('calibri', 60)

        """ 设置边框与文本信息 """
        self.rect = pygame.draw.rect(screen, self.button_color, ((self.pos_x, self.pos_y), (self.width, self.height)), 0)
        self.prep_msg(msg)

    def prep_msg(self, msg):    # 设置文本信息
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):  # 设置按钮
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


yao_button = Button(screen, 200, "Yao", (0, 0, 0), (255, 0, 0))
game_button = Button(screen, 400, "Game", (0, 0, 0), (255, 255, 255))
single_button = Button(screen, 100, "SINGLE", (255, 255, 255), (0, 0, 0))
double_button = Button(screen, 300, "DOUBLE", (255, 255, 255), (0, 0, 0))
quit_button = Button(screen, 500, "QUIT", (255, 255, 255), (0, 0, 0))
return_button = Button(screen, 0, "RETURN", (255, 255, 255), (0, 0, 0))
now_1_button = Button(screen, 550, "Now is X", (0, 0, 0), (0, 255, 0))
now_0_button = Button(screen, 550, "Now is 0", (0, 0, 0), (0, 0, 255))
result_1_button = Button(screen, 300, "X Win!", (255, 255, 255), (255, 0, 0))
result_2_button = Button(screen, 300, "O Win!", (255, 255, 255), (255, 0, 0))
result_3_button = Button(screen, 300, "draw", (255, 255, 255), (255, 0, 0))


def draw_line(start=(100, 100), end=(200, 200)):
    line_color = (255, 255, 255)
    line_width = 10
    pygame.draw.line(screen, line_color, start, end, line_width)


def draw_circle(position=(100, 100)):
    line_color = (255, 255, 255)
    radius = 45
    line_width = 10
    pygame.draw.circle(screen, line_color, position, radius, line_width)


def draw_x(position=0):
    x = position % 3
    y = int(position / 3) + 1
    draw_line(start=(130*x+20, 130*y+20), end=(130*x+110, 130*y+110))
    draw_line(start=(130*x+110, 130*y+20), end=(130*x+20, 130*y+110))


def draw_o(position=0):
    x = position % 3
    y = int(position / 3) + 1
    draw_circle(position=(130*x+65, 130*y+65))


def draw_result(array):
    for index in range(len(array)):
        if array[index] == 0:
            draw_o(index)
        elif array[index] == 1:
            draw_x(index)


def judge(array):
    answer = 2
    for index in range(3):
        if array[index] == array[index + 3] == array[index + 6] != 2:
            answer = array[index]
            break
        elif array[3 * index] == array[3 * index + 1] == array[3 * index + 2] != 2:
            answer = array[3 * index]
            break
        elif array[0] == array[4] == array[8] or array[2] == array[4] == array[6] != 2:
            answer = array[4]
    return answer


def auto(array, step=0):
    another = (step + 1) % 2
    flag = 1
    if array[4] == 2:
        array[4] = step
        flag = 0
    else:
        for index in range(3):
            if array[index] == array[index + 3] == step and array[index + 6] == 2:
                array[index + 6] = step
                flag = 0
                break
            elif array[index] == array[index + 6] == step and array[index + 3] == 2:
                array[index + 3] = step
                flag = 0
                break
            elif array[index + 3] == array[index + 6] == step and array[index] == 2:
                array[index] = step
                flag = 0
                break
            elif array[3 * index] == array[3 * index + 1] == step and array[3 * index + 2] == 2:
                array[3 * index + 2] = step
                flag = 0
                break
            elif array[3 * index] == array[3 * index + 2] == step and array[3 * index + 1] == 2:
                array[3 * index + 1] = step
                flag = 0
                break
            elif array[3 * index + 1] == array[3 * index + 2] == step and array[3 * index] == 2:
                array[3 * index] = step
                flag = 0
                break
            elif array[0] == array[4] == step and array[8] == 2:
                array[8] = step
                flag = 0
                break
            elif array[4] == array[8] == step and array[0] == 2:
                array[0] = step
                flag = 0
                break
            elif array[2] == array[4] == step and array[6] == 2:
                array[6] = step
                flag = 0
                break
            elif array[4] == array[6] == step and array[2] == 2:
                array[2] = step
                flag = 0
                break
    if flag == 1:
        for index in range(3):
            if array[index] == array[index + 3] == another and array[index + 6] == 2:
                array[index + 6] = step
                flag = 0
                break
            elif array[index] == array[index + 6] == another and array[index + 3] == 2:
                array[index + 3] = step
                flag = 0
                break
            elif array[index + 3] == array[index + 6] == another and array[index] == 2:
                array[index] = step
                flag = 0
                break
            elif array[3 * index] == array[3 * index + 1] == another and array[3 * index + 2] == 2:
                array[3 * index + 2] = step
                flag = 0
                break
            elif array[3 * index] == array[3 * index + 2] == another and array[3 * index + 1] == 2:
                array[3 * index + 1] = step
                flag = 0
                break
            elif array[3 * index + 1] == array[3 * index + 2] == another and array[3 * index] == 2:
                array[3 * index] = step
                flag = 0
                break
            elif array[0] == array[4] == another and array[8] == 2:
                array[8] = step
                flag = 0
                break
            elif array[4] == array[8] == another and array[0] == 2:
                array[0] = step
                flag = 0
                break
            elif array[2] == array[4] == another and array[6] == 2:
                array[6] = step
                flag = 0
                break
            elif array[4] == array[6] == another and array[2] == 2:
                array[2] = step
                flag = 0
                break
    while flag:
        r = random.randint(0, 8)
        if array[r] == 2:
            array[r] = 0
            flag = 0
            break
    return array


while True:
    while title:
        screen.fill((0, 0, 0))
        yao_button.draw_button()
        game_button.draw_button()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        time.sleep(3)
        title = 0
        menu = 1

    while menu:
        screen.fill((0, 0, 0))
        win = 2
        a = [2, 2, 2, 2, 2, 2, 2, 2, 2]
        k = 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 100 < mouse_x < 300:
                    if 100 < mouse_y < 200:
                        menu = 0
                        single = 1
                    elif 300 < mouse_y < 400:
                        menu = 0
                        double = 1
                    elif 500 < mouse_y < 600:
                        menu = 0
                        title = 1
        single_button.draw_button()
        double_button.draw_button()
        quit_button.draw_button()
        pygame.display.flip()

    while single:
        screen.fill((0, 0, 0))
        draw_result(a)
        if win != 2:
            single = 0
            if win == 1:
                result_1 = 1
            else:
                result_2 = 1
        elif win == 2 and a.count(2) == 0:
            single = 0
            result_3 = 1
        return_button.draw_button()
        draw_line(start=(0, 260), end=(390, 260))
        draw_line(start=(0, 390), end=(390, 390))
        draw_line(start=(130, 130), end=(130, 520))
        draw_line(start=(260, 130), end=(260, 520))
        if k == 0:
            now_0_button.draw_button()
        else:
            now_1_button.draw_button()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 0 < mouse_y < 100 and 100 < mouse_x < 300:
                    single = 0
                    menu = 1
                elif 130 < mouse_y < 520:
                    i = int(mouse_y / 130 - 1) * 3 + int(mouse_x / 130)
                    if a[i] == 2 and a.count(1) < 4:
                        a[i] = 1
                        win = judge(a)
                        if win == 2:
                            a = auto(a)
                        win = judge(a)
                    elif a.count(1) == 4:
                        for num in range(len(a)):
                            if a[num] == 2:
                                a[num] = 1
                                single = 0
                                result_3 = 1
        pygame.display.flip()

    while double:
        screen.fill((0, 0, 0))
        draw_result(a)
        if win != 2:
            double = 0
            if win == 1:
                result_1 = 1
            else:
                result_2 = 1
        elif win == 2 and a.count(2) == 0:
            double = 0
            result_3 = 1
        return_button.draw_button()
        draw_line(start=(0, 260), end=(390, 260))
        draw_line(start=(0, 390), end=(390, 390))
        draw_line(start=(130, 130), end=(130, 520))
        draw_line(start=(260, 130), end=(260, 520))
        if k == 0:
            now_0_button.draw_button()
        else:
            now_1_button.draw_button()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 0 < mouse_y < 100 and 100 < mouse_x < 300:
                    double = 0
                    menu = 1
                elif 130 < mouse_y < 520:
                    i = int(mouse_y / 130 - 1) * 3 + int(mouse_x / 130)
                    if a[i] == 2:
                        a[i] = k
                        k = (k + 1) % 2
                    win = judge(a)
        pygame.display.flip()

    while result_1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 0 < mouse_y < 100 and 100 < mouse_x < 300:
                    result_1 = 0
                    menu = 1
        return_button.draw_button()
        result_1_button.draw_button()
        pygame.display.flip()

    while result_2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 0 < mouse_y < 100 and 100 < mouse_x < 300:
                    result_2 = 0
                    menu = 1
        return_button.draw_button()
        result_2_button.draw_button()
        pygame.display.flip()

    while result_3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 0 < mouse_y < 100 and 100 < mouse_x < 300:
                    result_3 = 0
                    menu = 1
        return_button.draw_button()
        result_3_button.draw_button()
        pygame.display.flip()
