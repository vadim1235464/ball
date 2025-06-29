from pygame import *
from random import randint
window = display.set_mode((700,500))
display.set_caption('доганялки')
klock = time.Clock()

font.init()

win = font.SysFont(None,70).render('YOU WIN',True,(255,0,0))
lose = font.SysFont(None,70).render('YOU lose',True,(255,0,0))

class Game_sprite(sprite.Sprite):
    def __init__(self,background,x,y,speed,widht,hight):
        super().__init__()
        self.speed = speed
        self.image = transform.scale(image.load(background),(widht,hight))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(Game_sprite):
    def updateL(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y <= 400:
            self.rect.y += self.speed
    def updateR(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y <= 400:
            self.rect.y += self.speed

racket = Player('racket.png',35,300,10,40,100)
racket2 = Player('racket.png',625,300,10,40,100)
ball = Game_sprite('tenis_ball.png',350,300,5,40,40)
speedX = 5
speedY = 5
finish = False
game = True

while game:
    if not finish:
        window.fill((0,232,83))
        racket.reset()
        racket2.reset()
        ball.reset()
        racket.updateL()
        racket2.updateR()
        ball.rect.x += speedX
        ball.rect.y += speedY
        if ball.rect.y <= 0 or ball.rect.y >= 460:
            speedY *= -1
        if sprite.collide_rect(racket,ball) or sprite.collide_rect(racket2,ball):
            speedX *= -1
        if ball.rect.x <= 0:
            finish = True
            window.blit(lose,(200,200))
        if ball.rect.x >= 700:
            finish = True
            window.blit(lose,(200,200))
    for i in event.get():
        if i.type == QUIT:
            game = False

    display.update()
    klock.tick(60)

    
