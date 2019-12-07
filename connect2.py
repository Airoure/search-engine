import pygame,sys,random
from pygame.locals import *
#定义颜色变量  目标方块的颜色
yellowColor = pygame.Color(255,255,0)
#贪吃蛇的颜色
greenColor = pygame.Color(0,250,154)
#背景颜色
blackColor = pygame.Color(255,255,255)
def gameOver():
    pygame.quit()
    sys.exit()

def main():
    # 初始化pygame
    pygame.init()
    # 控制游戏速度
    fpsColck = pygame.time.Clock()
    # 创建pygame显示层
    playSurface = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('贪吃的陈文杰')
    #初始化贪吃蛇的起始坐标
    snakePosition = [0, 0]
    # 初始化贪吃蛇的长度
    snakeBody = [[100,0],[80,0],[60,0]]
    # 初始化目标方块的坐标
    targetPosition = [400, 400]
    # 初始化一个目标方块的标记  目的：用来判断是否吃掉这个目标方块
    targerflag = 1
    # 初始化方向
    direction = 'right'
    # 定义一个方向变量
    changeDirection = direction

    while True:
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    changeDirection = 'right'
                if event.key == K_LEFT:
                    changeDirection = 'left'
                if event.key == K_UP:
                    changeDirection = 'up'
                if event.key == K_DOWN:
                    changeDirection = 'down'
                    # 对应键盘Esc键
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))
        # 避免贪吃蛇穿过身体
        if changeDirection == 'left' and not direction == 'right':
            direction = changeDirection
        # 避免贪吃蛇穿过身体
        if changeDirection == 'right' and not direction == 'left':
            direction = changeDirection
        # 避免贪吃蛇穿过身体
        if changeDirection == 'up' and not direction == 'down':
            direction = changeDirection
        # 避免贪吃蛇穿过身体
        if changeDirection == 'down' and not direction == 'up':
            direction = changeDirection

        if direction == 'down':
            snakePosition[1] += 20
        # 增加蛇的长度
        snakeBody.insert(0, list(snakePosition))
        # 判断目标方块是否被吃掉
        if snakePosition[0] == targetPosition[0] and snakePosition[1] == targetPosition[1]:
            targerflag = 0
        else:
            snakeBody.pop()
        if targerflag == 0:
            x = random.randrange(1, 40)
            y = random.randrange(1, 40)
            targetPosition = [int(x * 20), int(y * 20)]
            targerflag = 1
        # 绘制pygame的显示层
        playSurface.fill(blackColor)


        for Position in snakeBody:
            pygame.draw.rect(playSurface, greenColor, Rect(Position[0], Position[1], 15, 15))
            pygame.draw.rect(playSurface, yellowColor, Rect(targetPosition[0], targetPosition[1], 20, 20))

        for num in range(0, len(snakeBody)):
            tail = 0
            if(snakeBody[0]==snakeBody[num] and num>1):
                tail = 1
                break
        if(tail==1):
            break

        pygame.display.flip()
        if snakePosition[0]> 800 or snakePosition[0] < 0:
            if snakePosition[0]>= 800:
                snakePosition = [0, snakePosition[1]]
            else:
                snakePosition = [800, snakePosition[1]]
        elif snakePosition[1] > 800 or snakePosition[1] < 0:
            if snakePosition[1] >= 800:
                snakePosition = [snakePosition[0], 0]
            else:
                snakePosition = [snakePosition[0], 800]
        fpsColck.tick(10)
if __name__ == '__main__':
    main()


