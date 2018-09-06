class Settings():
    """存储设置相关"""

    def __init__(self):
        """初始化设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_speed_factor = 5
        self.ship_limit = 1

        # 子弹设置
        self.bullet_speed_factor = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3

        # 外星人设置
        self.alien_speed_factor = 10
        self.fleet_drop_speed = 10
        # 1表示右移， -1表示左移
        self.fleet_direction = 1
