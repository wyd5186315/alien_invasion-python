#导入pygame模块
import pygame
#导入设置类
from settings import Settings
#导入飞船类
from ship import Ship
#导入监听键盘鼠标事件模块并取名为gf
import game_functions as gf
#导入精灵编组
from pygame.sprite import Group

#游戏开始
def run_pygame():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    #实例一个设置类
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    #给屏幕对象取个标题
    pygame.display.set_caption("Alien Invasion")
    #设置屏幕的背景颜色
    bg_color=(ai_settings.bg_color)

    #创建一艘飞船
    ship=Ship(ai_settings,screen)

    #创建用于存储子弹的编组
    bullets=Group()

    #开始游戏的主循环
    while True:

        #调用game_functions模块check_events方法 监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,ship,bullets)
        #飞船移动
        ship.update()
        #子弹向上移动
        bullets.update()

        #调用gf模块update_screen方法 更新屏幕
        gf.update_screen(ai_settings,screen,ship,bullets)





#运行游戏开始方法
run_pygame()