import pyautogui as pag
import time


START_X = 0
START_Y = 204
BOX_WIDTH = 1895
BOX_HEIGHT = 802

SCAN_REGION = (START_X, START_Y, BOX_WIDTH, BOX_HEIGHT)
TARGET_COLOR = (149, 195, 232)

time.sleep(3)

start_time = time.time()


while True:

    if time.time() - start_time >= 7:
        break

    screenshot = pag.screenshot(region=SCAN_REGION)
    width, height = screenshot.size

    color_found_this_frame = False

    for x in range(0, width, 5):
        for y in range(0, height, 5):
            curr_pix = screenshot.getpixel((x, y))[:3]

            if curr_pix == TARGET_COLOR:
                
                actual_screen_x = START_X + x
                actual_screen_y = START_Y + y
                
                pag.click(actual_screen_x, actual_screen_y)

                color_found_this_frame = True
                break
        if color_found_this_frame:
                    break

    time.sleep(0.01)