# 本代码作者：林家华
# 班级：20大数据技术与应用1班
# 学号：205801138

import pygame  # 游戏插件
import random  # 随机数插件
import math  # 数学模块

# 初始化界面
pygame.init()
screen = pygame.display.set_mode((900, 600))   # 设置窗口的大小
pygame.display.set_caption('进击的飞机')   # 设置窗口的标题
icon = pygame.image.load('UFO.png')
pygame.display.set_icon(icon)   # 添加图标
context = pygame.image.load('context.png')   # 定义背景图像
plane = pygame.image.load('plane1.png')   # 定义飞机图像

# 设置飞机初始位置
planex = 400  # 飞机的X坐标
planey = 480  # 飞机的Y坐标
planet = 0  # 飞机移动速度

# 设置飞机移动及设置移动边界
def move_plaene():
    global planex  # 使之前设置的变量可以改动
    planex += planet  # 使飞机移动
    # 设置飞机移动边界
    if planex > 795:
        planex = 795
    if planex < 0:
        planex = 0

# 添加多个敌人
number_of_ufos = 6  # 敌人数量
class Ufo():  # 敌人类
    def __init__(self):
        self.img = pygame.image.load('UFO.png')  # 定义敌人图像
        self.x = random.randint(200, 600)  # 设置敌人出现的范围
        self.y = random.randint(0, 200)   # 设置敌人出现的范围
        self.step = random.randint(1, 2)  # 设置敌人出现的速度
    def reset(self):  # 当被击中时重置位置
        self.x = random.randint(200, 600)  # 设置敌人出现的范围
        self.y = random.randint(0, 200)  # 设置敌人出现的范围
        self.step = random.randint(1, 3)  # 设置敌人出现的速度
ufos = []  # 保存所以敌人
for x in range(number_of_ufos):
    ufos.append(Ufo())

# 显示敌人并使敌人进行移动
def show_ufo():
    global is_over  # 使之前设置的变量可以改动
    for u in ufos:
        screen.blit(u.img, (u.x, u.y))
        u.x += u.step  # 使敌人移动
        # 设置敌人移动边界
        if(u.x > 795 or u.x <0):
            u.step *= -1
            u.y += 50
            if u.y >450:  # 判定游戏结束的条件
                is_over = True
                print("游戏结束")
                ufos.clear()

# 添加子弹
class Ball():  # 子弹类
    def __init__(self):
        self.img = pygame.image.load('ball.png')  # 定义子弹图像
        self.x = planex+25  # 子弹出现的位置
        self.y = planey+10  # 子弹出现的位置
        self.step = 8  # 子弹移动的速度
    def hit(self):  # 判断是否击中敌人
        global score  # 使之前设置的变量可以改动
        for u in ufos:
            if(distance(self.x, self.y, u.x, u.y) < 30):
                balls.remove(self)
                u.reset()  # 重置敌人位置
                score += 1  # 击中敌人后分数加1

balls = []  #保存现有的子弹

# 显示子弹并移除离开界面的子弹
def show_balls():
    for b in balls:
        screen.blit(b.img, (b.x, b.y))
        b.hit()  # 查看是否击中敌人
        b.y -=b.step  # 使子弹移动
        if b.y < 0:  # 判断子弹是否离开界面
            balls.remove(b)  # 移除离开界面的子弹

# 子弹与敌人的距离
def distance(bx,by,ux,uy):
    a = bx - ux
    b = by - uy
    return math.sqrt(a*a + b*b) #开更号

# 分数
score = 0
font1 = pygame.font.Font('freesansbold.ttf', 32)  # 定义字体及字号
def show_score():  # 显示分数
    text = f"score:{score}"
    score_render = font1.render(text, True, (123,234,181))   # 输出文字及定义字体颜色
    screen.blit(score_render, (10, 10))  # 调整文本位置

# 游戏结束
is_over = False
font2 = pygame.font.Font('freesansbold.ttf', 72)  # 定义字体及字号
def check_is_over():  # 提醒游戏已结束
    if is_over:
        text = f"GAME OVER"
        reander = font2.render(text, True, (123,234,181))  # 输出文字及定义字体颜色
        screen.blit(reander, (250, 250))  # 调整文本位置

# 游戏主循环
while True:
    screen.blit(context, (0, 0))   # 添加背景图
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # 添加停止方式
            running == False
        # 通过键盘控制飞机移动
        if event.type == pygame.KEYDOWN:  # 按下方向键使飞机移动
            if event.key == pygame.K_RIGHT:  # 按下右键右移
                planet = 3
            elif event.key == pygame.K_LEFT:  # 按下左键左移
                planet = -3
            elif event.key == pygame.K_SPACE:  # 按下空格键发射子弹
                balls.append(Ball())
        if event.type == pygame.KEYUP:   # 停止按下方向键使飞机原地不动
            planet = 0

    screen.blit(plane, (planex, planey))   # 调用飞机图像
    move_plaene()   # 调用showmove_plaene这个方法
    show_ufo()   # 调用show_ufo这个方法
    show_balls()  #调用show_balls这个方法
    show_score()  #调用show_score这个方法
    check_is_over()   #调用check_is_over这个方法
    pygame.display.update()  # 界面更新，必须放在主循环末尾