from classes import *

clock = time.Clock()

font.init()
font1 = font.SysFont()

plate = Player(plr, 48, 175, 2)
plate2 = Player(plr, window.get_width()-70, 180, 2)
soccer = Ball(ball, window.get_width()/2, window.get_height()/2, 2, 2)

while counter.run:

    for e in event.get():
        if e.type == QUIT:
            counter.run = False

    if sprite.collide_rect(plate, soccer):
        soccer.speedx *= -1

    if sprite.collide_rect(plate2, soccer):
        soccer.speedx *= -1
    
    window.blit(feild, (0,0))

    soccer.move()
    soccer.show()

    plate.move()
    plate.show()

    plate2.move2()
    plate2.show()

    count1 = font1.render(f'Счёт игрока 1: {counter.plr1Scored}')
    count2 = font1.render(f'Счёт игрока 2: {counter.plr2Scored}')
    window.blit(count1)
    window.blit(count2)

    display.update()
    clock.tick(60)