# importing required library
import pygame

# constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 300
BACKGROUND_COLOR = (255,255,255) # RGB
LEFT_PRESSED = False
RIGHT_PRESSED = False

class Dino:
    def __init__(self, pos_x, pos_y, speed):
        img = pygame.image.load("../week8/dino.png")
        self.img = pygame.transform.scale(img, (100,100))
        # init position
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = speed

    def tint(self):
        # option: tint your image if you want
        self.img.fill((0, 0, 200, 100), special_flags=pygame.BLEND_ADD)
        pass

    def animate(self, left):
        if self.pos_x < SCREEN_WIDTH:
            if left == 1:
                self.pos_x -= self.speed
            else:
                self.pos_x += self.speed
        else:
           self.pos_x = 0

    def draw(self):
        screen.blit(self.img, (self.pos_x, self.pos_y))

class DinoKid(Dino):
    def __init__(self, pos_x, pos_y, speed):
        super().__init__(pos_x, pos_y, speed)
        self.img = pygame.transform.scale(self.img, (50, 50))

    def follow(self, parent:Dino):
        self.pos_x = parent.pos_x - 50

# activate the pygame library
pygame.init()

# create the display surface object
# of specific dimension.
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# set the pygame window name
pygame.display.set_caption('image')

# Create one dino object at a start location
dino = Dino(0, 100, 10)
baby = DinoKid(0, 150, 5)

# Init the clock
clock = pygame.time.Clock()

flag = True
while flag:
    # ticking the clock
    clock.tick(60)

    # update dino's position
    # dino.animate()
    if LEFT_PRESSED:
        dino.animate(1)
        # baby.follow(dino)
    elif RIGHT_PRESSED:
        dino.animate(0)
        # baby.follow(dino)

    baby.follow(dino)

    # paint the screen with background color
    screen.fill(BACKGROUND_COLOR)
    # Using blit to copy image to screen at a specific location
    dino.draw()
    baby.draw()
    # refresh the display
    pygame.display.flip()

    for event in pygame.event.get():
        # code you need to end pygame
        if event.type == pygame.QUIT:
            # print("quit")
            flag = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # print("left")
                # dino.animate(1, 0)
                LEFT_PRESSED = True
            if event.key == pygame.K_RIGHT:
                # print("right")
                # dino.animate(0, 1)
                RIGHT_PRESSED = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                LEFT_PRESSED = False
            if event.key == pygame.K_RIGHT:
                RIGHT_PRESSED = False



pygame.quit()
exit(0)