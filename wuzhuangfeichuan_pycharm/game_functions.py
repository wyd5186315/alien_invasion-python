import sys
import pygame
from bullet import Bullet
def check_keydown_events(event,ai_settings,screen,ship,bullets):
    '''按下左或者右键盘时'''
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 向左移动
        ship.moving_left = True
    elif event.key==pygame.K_SPACE:
        #创建一颗子弹，并将其加入到编组bullets中
        new_bullet=Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)
def check_keyup_events(event,ship):
    '''当松开左或者右键时'''
    if event.key == pygame.K_RIGHT:
        # 飞船停止向右移动
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # 向停止左移动
        ship.moving_left = False

def check_events(ai_settings,screen,ship,bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type==pygame.KEYUP:
            check_keyup_events(event,ship)

def update_screen(ai_settings,screen,ship,bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    #每次循环时都重绘屏幕
    #填充背景颜色
    screen.fill(ai_settings.bg_color)

    #在飞船和外星人后面重新绘制所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    #绘制飞机
    ship.blitme()

    #让最近绘制的屏幕可见
    pygame.display.flip()