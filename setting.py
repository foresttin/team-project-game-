# game options/settings
TITLE = "TEST"
WIDTH = 800
HEIGHT = 600
FPS = 60
FONT_NAME = 'arial'

# Player properties
PLAYER_ACC = 1.5
PLAYER_FRICTION = -0.2
PLAYER_GRAVITY = 0.8

# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40),
                 (WIDTH/2 - 50, HEIGHT*3/4, 100, 20),
                 (125, HEIGHT - 350, 100, 20),
                 (350, 200, 100, 20),
                 (175, 100, 50, 20)]


# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
SKYBLUE = (48, 200, 248)
BGCOLOR = SKYBLUE
PARANG=(108,108,255)


# Image file paths
PLAYER_IMG = 'player.png'
PLATFORM_IMGS = ['platform1.png', 'platform2.png', 'platform3.png', 'platform4.png']

