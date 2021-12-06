import random
import time
from typing import List

while True:
    day = int(input("请输入您要测试的章节：（目前仅仅支持9～23）"))
    if 8 < day < 24:
        break
    else:
        print("你在乱搞吗？请重新输入！")

file_path = "word_list" + str(day)


def file_open(filename):
    raw_file = open(filename, mode="r", encoding='utf-8')
    section = raw_file.readline().strip('word_list_\n')
    test = int(raw_file.readline().strip('共个单词\n'))
    totals = total = random.randint(5, test - 4)
    return raw_file,  section, test, totals, total


def menu():
    while True:
        print("1.看英文选中文\n2.看中文选英文\n3.看中文默英文(提示前五个字母)\n4.看中文默英文(提示前三个字母)\n5.看中文默英文(提示首字母)\n6.随机难度+全部测试")
        test = int(input("您想测试的难度为："))                    # 选择难度
        if test > 6:
            print("难度错误，请重新输入")
        else:
            break
    return test


def question_1():
    already: List[int] = yet[:]                                 # 列表切片
    use_num = test_num                                          # 测试数量重置
    temp = random.randint(0, 3)                                 # 从0，1，2，3中随机取一个数字作为选项
    if temp == 0:                                               # 假如a为正确答案
        print("a." + answer[a])
    else:
        y = random.randint(0, use_num - 1)
        used = already.pop(y)
        print("a." + answer[used])
    if temp == 1:                                               # 假如b为正确答案
        print("b." + answer[a])
    else:
        y = random.randint(0, use_num - 2)
        used = already.pop(y)
        print("b." + answer[used])
    if temp == 2:                                               # 假如c为正确答案
        print("c." + answer[a])
    else:
        y = random.randint(0, use_num - 3)
        used = already.pop(y)
        print("c." + answer[used])
    if temp == 3:                                               # 假如d为正确答案
        print("d." + answer[a])
    else:
        y = random.randint(0, use_num - 4)
        used = already.pop(y)
        print("d." + answer[used])
    consequence = sheet[temp]                                   # 将数字转换为字母
    return consequence                                          # 将正确答案输出


def question_2():
    already: List[int] = yet[:]                                 # 列表切片
    use_num = test_num                                          # 测试数量重置
    temp = random.randint(0, 3)                                 # 从0，1，2，3中随机取一个数字作为选项
    if temp == 0:                                               # 假如a为正确答案
        print("a." + grammar[a])
    else:
        y = random.randint(0, use_num - 1)
        used = already.pop(y)
        print("a." + grammar[used])
    if temp == 1:                                               # 假如b为正确答案
        print("b." + grammar[a])
    else:
        y = random.randint(0, use_num - 2)
        used = already.pop(y)
        print("b." + grammar[used])
    if temp == 2:                                               # 假如c为正确答案
        print("c." + grammar[a])
    else:
        y = random.randint(0, use_num - 3)
        used = already.pop(y)
        print("c." + grammar[used])
    if temp == 3:                                               # 假如d为正确答案
        print("d." + grammar[a])
    else:
        y = random.randint(0, use_num - 4)
        used = already.pop(y)
        print("d." + grammar[used])
    consequence = sheet[temp]                                   # 将数字转换为字母
    return consequence


grammar = []                                                    # 语法条目列表
answer = []                                                     # 答案列表
sheet = ["a", "b", "c", "d"]
score = 0
file, unit, test_num, num, k = file_open(file_path)             # 打开测试对象文件
print("您本次测试的个数为：" + str(k))
difficult = menu()
for x in range(test_num * 2):                                   # 将文件内的语法与答案放入列表
    if x % 2 == 0:
        grammar.append(file.readline().strip('1234567890.\n'))
    else:
        answer.append(file.readline().strip('\n'))              # 题目数（用于计分）
yet = [value for value in range(test_num)]                      # 统计题目个数，保证题目不重复
print("现在开始第" + unit + "天的单词测试")                        # 标题
time.sleep(1)
if difficult == 6:
    num = k = test_num - 4
    difficult = random.randint(1, 5)
    print("您选择了随机难度+全部测试\n您的测试难度为：" + str(difficult) + "\n您的测试个数为:" + str(test_num - 4))
if difficult == 1:
    for i in range(k):
        time.sleep(1)
        x = random.randint(0, test_num-1)                           # 从0到（test_num-1）中取随机数
        a = yet.pop(x)                                              # 去除重复数字
        test_num -= 1                                               # 题目数减1
        print('\033[37;0m' + "第" + str(i+1) + "题：" + grammar[a])
        answers = question_1()                                        # 输出正确答案
        print('\033[37;0m' + "您的选项为")
        b = input()                                                 # 获得输入的字母
        if b == answers:                                            # 将输入信息与正确答案比对
            print('\033[32;0m' + "答对啦！")
            score += (100 / num)
        else:
            print('\033[31;0m' + "答错了！正确选项为：”" + answer[a] + "”")
    print('\033[32;0m' + "测验结束啦！")
elif difficult == 2:
    for i in range(k):
        time.sleep(1)
        x = random.randint(0, test_num-1)                           # 从0到（test_num-1）中取随机数
        a = yet.pop(x)                                              # 去除重复数字
        test_num -= 1                                               # 题目数减1
        print('\033[37;0m' + "第" + str(i+1) + "题：" + answer[a])
        answers = question_2()                                        # 输出正确答案
        print('\033[37;0m' + "您的选项为")
        b = input()                                                 # 获得输入的字母
        if b == answers:                                            # 将输入信息与正确答案比对
            print('\033[32;0m' + "答对啦！")
            score += (100 / num)
        else:
            print('\033[31;0m' + "答错了！正确选项为：”" + grammar[a] + "”")
    print('\033[32;0m' + "测验结束啦！")
elif difficult == 5:
    for i in range(k):
        time.sleep(1)
        x = random.randint(0, test_num-1)                           # 从0到（test_num-1）中取随机数
        a = yet.pop(x)                                              # 去除重复数字
        test_num -= 1                                               # 题目数减1
        print('\033[37;0m' + "第" + str(i+1) + "题：" + answer[a])
        answers = grammar[a]                                        # 输出正确答案
        print('\033[37;0m' + "它的英文应为（首字母为" + str(grammar[a][0]) + "）：")
        b = input()                                                 # 获得输入的字母
        if b == answers:                                            # 将输入信息与正确答案比对
            print('\033[32;0m' + "答对啦！")
            score += (100 / num)
        else:
            print('\033[31;0m' + "答错了！正确答案为：”" + grammar[a] + "”")
elif difficult == 4:
    for i in range(k):
        time.sleep(1)
        x = random.randint(0, test_num-1)                           # 从0到（test_num-1）中取随机数
        a = yet.pop(x)                                              # 去除重复数字
        test_num -= 1                                               # 题目数减1
        print('\033[37;0m' + "第" + str(i+1) + "题：" + answer[a])
        answers = grammar[a]                                        # 输出正确答案
        print('\033[37;0m' + "它的英文应为（前三个字母为" + str(grammar[a][:3]) + "）：")
        b = input()                                                 # 获得输入的字母
        if b == answers:                                            # 将输入信息与正确答案比对
            print('\033[32;0m' + "答对啦！")
            score += (100 / num)
        else:
            print('\033[31;0m' + "答错了！正确答案为：”" + grammar[a] + "”")
elif difficult == 3:
    for i in range(k):
        time.sleep(1)
        x = random.randint(0, test_num-1)                           # 从0到（test_num-1）中取随机数
        a = yet.pop(x)                                              # 去除重复数字
        test_num -= 1                                               # 题目数减1
        print('\033[37;0m' + "第" + str(i+1) + "题：" + answer[a])
        answers = grammar[a]                                        # 输出正确答案
        print('\033[37;0m' + "它的英文应为（前五个字母为" + str(grammar[a][:5]) + "）：")
        b = input()                                                 # 获得输入的字母
        if b == answers:                                            # 将输入信息与正确答案比对
            print('\033[32;0m' + "答对啦！")
            score += (100 / num)
        else:
            print('\033[31;0m' + "答错了！正确答案为：”" + grammar[a] + "”")
if score >= 60:                                                 # 统计最终成绩
    print('\033[36;0m' + "您的成绩为：" + str(int(score)) + "分/100分")
else:
    print('\033[31;0m' + "您的成绩为：" + str(int(score)) + "分/100分")
file.close()                                                    # 关闭测试对象文件
