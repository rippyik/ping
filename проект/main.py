from pygame import *

x1 = (100)
x2 = (500)
y1 = (100)
y2 = (100)

window = display.set_mode((700,500))
lock = time.Clock()
FPS = 60

display.set_caption("картинка")
background = transform.scale(image.load("cir.jpg"),(700,500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(wight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

win_height = 500
win_wight = 700

racket1 = Player("racketka.png", 30, 200, 4, 150, 150)
racket2 = Player("racketka.png", 520, 200, 4, 150, 150)
ball = GameSprite("ball.png", 200, 200, 4, 125, 125)

speed_x = 10
speed_y = 10

game = True
while game:
    ball.rect.x += speed_x
    ball.rect.y += speed_y

    if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
        speed_x *= -1
        speed_y *= 1


    window.blit(background,(0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    racket1.reset()
    racket2.reset()
    racket1.update_l()
    racket2.update_r()
    ball.reset()
    display.update()

































































