import random
import time
from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def run_event():
    global running
    global x, y

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running == False

        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running == False
    pass

def run_dir(now, after):

    now_x = now
    after_x = after

    if now_x <= after_x:
        return 1
    else:
        return 0

def random_location():
    ran_x = random.randrange(0, KPU_WIDTH + 1)
    ran_y = random.randrange(0, KPU_HEIGHT + 1)


    return ran_x, ran_y

def following_line():
    global running
    global before_location
    global run_location
    global frame

    dir = (run_dir(before_location, run_location))

    for i in range(0, 100 + 1, 2):
        clear_canvas()
        t = i / 100
        x = (1 - t) * before_location[0] + t * run_location[0]
        y = (1 - t) * before_location[1] + t * run_location[1]

        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        hand_arrow.draw(run_location[0], run_location[1])
        character.clip_draw(frame * 100, 100 * dir, 100, 100, x, y)

        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)

        run_event()


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2 , KPU_HEIGHT // 2
frame = 0

run_location = (0, 0)
before_location = (0, 0)

while running:
    before_location = run_location
    run_location = random_location()
    following_line()

    run_event()


close_canvas()

