class Settings():
    """存储《外星人入侵》的所有设置类"""
    def __init__(self):
        """初始化游戏设置"""
        #屏幕设置
        self.screen_width=1200
        self.screen_height=600
        #背景颜色
        self.bg_color=(87,250,255)

        #飞船速度
        self.ship_speed_factor=1.5
