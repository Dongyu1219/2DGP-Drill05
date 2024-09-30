from pico2d import *
from pygame.display import update
from pygame.event import clear

open_canvas()
grass = load_image('TUK_GROUND.png')
character = load_image('drill_05_charcter_running_image.png')


def handle_events():
    global running ,dir
    # fill here
    global x
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
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1

running = True
x = 800 // 2
frame = 0
dir = 0         # 방향 변수 추가. 오른쪽 키 쭈욱 누르면 계속 가게
# fill here
while running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame*100, 100, 100,100, x, 90)
    update_canvas()
    handle_events()
    frame = (frame + 1) %8
    x += dir * 5                #방향 변수에 따라 x가 계속 변한다
    delay(0.05)

close_canvas()

