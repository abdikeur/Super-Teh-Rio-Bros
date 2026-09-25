from object import Platform, Goal, Coin, Spike, Saw


class Level:
    def __init__(self, level_number):
        self.platforms = []
        self.coins = []
        self.spikes = []
        self.saws = []
        self.goal = None

        self.load_level(level_number)

    def load_level(self, level_number):
        
        if level_number == 1:
            self.platforms = [
                Platform(0, 680, 280, 40, color_row=1),
                Platform(515, 580, 250, 40, color_row=1),
                Platform(1030, 680, 280, 40, color_row=1),
            ]
            
            self.coins = [
                Coin(624, 380)
            ]
            
            self.spikes = [
                Spike(616, 532)
            ]
            
            self.goal = Goal(1100, 588, 128, 92)

        elif level_number == 2:
            self.platforms = [
                Platform(0, 680, 250, 40, color_row=2),
                Platform(515, 680, 250, 40, color_row=2),
                Platform(1030, 680, 250, 40, color_row=2),
                Platform(0, 500, 250, 40, color_row=2),
                Platform(0, 320, 250, 40, color_row=2)
            ]
            
            self.coins = [
                Coin(130, 560),
                Coin(1150, 560),
                Coin(624, 560)
            ]
            
            self.spikes = [
                Spike(555, 632),
                Spike(677, 632)
            ]

            self.goal = Goal(61, 228, 128, 92)

        elif level_number == 3:
            self.platforms = [
                Platform(0, 680, 200, 40, color_row=2),
                Platform(350, 580, 200, 40, color_row=2),
                Platform(700, 480, 200, 40, color_row=2),
                Platform(1050, 380, 200, 40, color_row=2),
                Platform(700, 280, 200, 40, color_row=2),
                Platform(350, 180, 200, 40, color_row=2)
            ]
            
            self.coins = [
                Coin(84, 560),
                Coin(609, 380),
                Coin(84, 160),
                Coin(84, 260),
                Coin(84, 360),
                Coin(84, 460),
            ]
            
            self.spikes = [
                Spike(712, 232),
                Spike(840, 232),
                Spike(776, 432),
                Spike(426, 132)
            ]
            
            self.goal = Goal(1086, 288, 128, 92)
            
        elif level_number == 4:
            self.platforms = [
                Platform(0, 680, 250, 40, color_row=3),
                Platform(250, 680, 250, 40, color_row=3),
                Platform(500, 680, 250, 40, color_row=3),
                Platform(1030, 680, 250, 40, color_row=3),
                Platform(1030, 480, 250, 40, color_row=3),
                Platform(1030, 280, 250, 40, color_row=3),
                Platform(0, 280, 250, 40, color_row=3),
                Platform(250, 280, 250, 40, color_row=3),
                Platform(500, 280, 250, 40, color_row=3),
            ]
            
            self.coins = [
                Coin(359, 460),
                Coin(1139, 560),
                Coin(1139, 360),
                Coin(1139, 160),
                Coin(359, 60),
            ]
            
            self.spikes = [
                Spike(263, 632),
                Spike(307, 632),
                Spike(351, 632),
                Spike(395, 632),
                Spike(439, 632),
                Spike(263, 232),
                Spike(307, 232),
                Spike(351, 232),
                Spike(395, 232),
                Spike(439, 232)
            ]
            
            self.saws = [
                Saw(1030, 432),
                Saw(1232, 432),
                Saw(1030, 382),
                Saw(1232, 382),
                Saw(1030, 332),
                Saw(1232, 332),
                Saw(750, 280),
                Saw(798, 280),
                Saw(846, 280),
                Saw(894, 280),
                Saw(942, 280),
                Saw(990, 280),
            ]
            
            self.goal = Goal(50, 190, 128, 92)