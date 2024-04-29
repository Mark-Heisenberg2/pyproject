from classes import *

clock = time.Clock()

font.init()
font1 = font.SysFont(['Agency FB', 'Heletic', 'Arial'], 30)

plate = Player(plr, 48, 175, 2)
plate2 = Player(plr, window.get_width()-73, 180, 2)
soccer = Ball(ball, window.get_width()/2, window.get_height()/2, 2, 2)

def mode_select():
    counter.mode = 1

    soccer.rect.x = window.get_width() / 2
    soccer.rect.y = window.get_height() / 2

def quited():
    counter.run = False

play_btn = Button(play_button, 54, 148, mode_select)
quit_btn = Button(quit_button, 54, 250, quited)

while counter.run:

    for e in event.get():
        if e.type == QUIT:
            counter.run = False

        elif e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                counter.click = e.pos

        elif e.type == MOUSEBUTTONUP:
            if e.button == 1:
                counter.click = (-1,  -1)

    if counter.mode == 0:
        window.blit(feild, (0,0))

        soccer.move_back()
        soccer.show()
        
        quit_btn.click()
        quit_btn.show()

        play_btn.click()
        play_btn.show()

        window.blit(game_name, (376, 59))

    elif counter.mode == 1:
        if sprite.collide_rect(plate, soccer):
            if soccer.rect.left <= plate.rect.centerx:
                if soccer.rect.centery < plate.rect.centery:
                    soccer.speedy = -abs(soccer.speedy)

                elif soccer.rect.centery > plate.rect.centery:
                    soccer.speedy = abs(soccer.speedy)

            if counter.left_collid:

                counter.left_collid = False
                soccer.speedx *= -1
                counter.right_collid = True

        if sprite.collide_rect(plate2, soccer):
            if soccer.rect.right >= plate2.rect.centerx:
                if soccer.rect.centery > plate2.rect.centery:
                    soccer.speedy = abs(soccer.speedy)

                elif soccer.rect.centery < plate2.rect.centery:
                    soccer.speedy = -abs(soccer.speedy)

            if counter.right_collid:

                counter.right_collid = False
                soccer.speedx *= -1
                counter.left_collid = True


        
        window.blit(feild, (0,0))

        soccer.move()
        soccer.show()

        plate.move()
        plate.show()

        plate2.move2()
        plate2.show()

        count1 = font1.render(f'Player1 score: {counter.plr1Scored}', False, 'black')
        count2 = font1.render(f'Player2 score: {counter.plr2Scored}', False, 'black')
        window.blit(count1, (20, 20))
        window.blit(count2, (window.get_width()-count2.get_width()-20, 20))

    display.update()
    clock.tick(60)