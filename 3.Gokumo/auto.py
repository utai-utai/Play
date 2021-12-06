import random
import sys

filename = 'bag001.txt'
with open(filename, 'w') as file_object:
    file_object.write("Add a words/n")
    file_object.write("Add two words/n")

num = 14
a = [[2] * num for i in range(num)]
now = 0
x = 2


def judge_win():
    global num, x
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
        print("player2 win")
        print(a)
        sys.exit()
    elif x == 0:
        print("player1 win")
        print(a)
        sys.exit()


def auto_one(coordinate_x, coordinate_y, which):
    count = 0
    global num, a
    b = [[0] * 3 for example in range(3)]
    b[1][1] = 9
    for i in range(3):
        for j in range(3):
            if coordinate_x == 0:
                b[0][j] = 9
            if coordinate_x == num - 1:
                b[2][j] = 9
            if coordinate_y == 0:
                b[i][0] = 9
            if coordinate_y == num - 1:
                b[i][2] = 9
    for i in range(3):
        for j in range(3):
            if b[i][j] == 0 and a[coordinate_x + i - 1][coordinate_y + j - 1] == 2:
                count += 1
                b[i][j] = count
    if count == 0:
        print("平局")
        print(a)
        sys.exit()
    else:
        ran_x = random.randint(1, count)
    print(b)
    print(ran_x)
    for i in range(3):
        for j in range(3):
            if b[i][j] == ran_x:
                print("i = " + str(i)+"  j = " + str(j))
                a[coordinate_x + i - 1][coordinate_y + j - 1] = which
                print("现在坐标 = " + str(coordinate_x + i - 1)+" ," + str(coordinate_y + j - 1))
                print("现在下的是" + str(which))
                return (coordinate_x + i - 1), (coordinate_y + j - 1)


m = 7
n = 7
a[m][n] = 0
while True:
    m, n = auto_one(m, n, now)
    now = (now + 1) % 2
    judge_win()
    print(a)
