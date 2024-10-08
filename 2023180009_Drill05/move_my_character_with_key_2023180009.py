from pico2d import *
from pygame.display import update
from pygame.event import clear

open_canvas()
grass = load_image('TUK_GROUND.png')
character = load_image('drill_05_png.png')


def handle_events():
    global running ,dir, dir2
    # fill here
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        # fill here
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_UP:
                dir2 += 1
            elif event.key == SDLK_DOWN:
                dir2 -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
            elif event.key == SDLK_UP:
                dir2 -= 1
            elif event.key == SDLK_DOWN:
                dir2 += 1
running = True
x = 800 // 2
y= 600 //2
frame = 0
dir = 0         # 방향 변수 추가. 오른쪽 키 쭈욱 누르면 계속 가게
dir2 = 0
# fill here
while running:
    clear_canvas()
    grass.draw(800 // 2, 600 // 2, 800, 600)
    if dir < 0 and dir2 == 0 :
        character.clip_composite_draw(frame * 130, 140, 130, 140, 0, 'h',  x, y, 132, 140)
    elif dir >=0 and dir2==0:
        character.clip_draw(frame*130, 140, 130,140, x, y)
    if dir2 > 0 and dir ==0:
        character.clip_composite_draw(frame * 130, 140, 130, 140, 1, 'v', x, y, 132, 140)
    elif dir2 < 0 and dir ==0:
        character.clip_composite_draw(frame * 130, 140, 130, 140, 4, 'v', x, y, 132, 140)
    update_canvas()
    handle_events()
    frame = (frame + 1) %5
    x += dir * 5                #방향 변수에 따라 x가 계속 변한다
    y += dir2 * 5
    if x< 50:
        x = 50
    if x>750:
        x = 750
    if y< 50:
        y=50
    if y>550:
        y=550
    delay(0.08)

close_canvas()

