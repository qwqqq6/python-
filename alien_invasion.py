import sys
import pygame

def run_game():
    # 初始化
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    #设置背景色
    bg_color = (230,230,230)

    # 开始游戏主循环
    while True:

        # 监视键盘和鼠标
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #重绘屏幕
        screen.fill(bg_color)

        # 最近绘制屏幕可见
        pygame.display.flip()


if __name__ == "__main__":
    run_game()