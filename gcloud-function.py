from google.cloud import vision
from google.cloud.vision import types
from python_imagesearch.imagesearch import region_grabber
import binascii
import cv2
import numpy as np
import pyautogui, time

region_dict = {
    "stat_dmg":  (258, 189, 359, 214),
    "crit_dmg":  (800, 463, 895, 485),
    "gold":  (258, 646, 350, 665)
}

resource_dict = {
    "gain": (615, 530, 703, 556),
    "coin": (612, 335, 720, 362),
    "gem": (615, 428, 667, 454),
    "weapon_box": (615, 463, 660, 488),
    "heroes": (615, 495, 670, 520),
    "key": (793, 428, 862, 454),
    "bone": (794, 463, 878, 488)  
}

rewind_pre_scroll = {
    "Max Day": (328,335,385,360),
    "Rewinds": (358,398,418,421),
    "elixir_mastery": (570, 260, 645, 280),
    "hidden_strength": (571, 353, 645, 373),
    "untapped_power": (571, 447, 645, 467)
}

rewind_post_scroll = {
    "explosive_strength": (571, 246, 645, 266),
    "beautiful_disaster": (571, 340, 645, 360),
    "inspire": (571, 433, 645, 454),
    "hard_labour": (571, 622, 645, 642)
}

img1 = cv2.imread('test123.png')
print(type(img1.shape[1]))

def scale_img(img1, img2):
    if img1.shape[1] > img2.shape[1]:
        scaled_img = vertical_concat_op(img2, img1)
        final_img = np.concatenate((img1, scaled_img), axis=0)
    elif img2.shape[1] > img1.shape[1]:
        scaled_img = vertical_concat_op(img1, img2)
        final_img = np.concatenate((img2, scaled_img), axis=0)
    else:
        final_img = np.concatenate((img2, img1), axis=0)
    return final_img

def vertical_concat_op(small_img, large_img):
    multiplier = large_img.shape[1] / small_img.shape[1]
    height = int(small_img.shape[0] * multiplier)
    width = int(small_img.shape[1] * multiplier)
    if large_img.shape[1] > width:
        width += 1
    elif large_img.shape[1] < width:
        width -= 1

    dim = (width, height)
    resized = cv2.resize(small_img, dim, interpolation = cv2.INTER_CUBIC)
    print(resized.shape)
    print(large_img.shape)
    return resized

border_bar = cv2.imread('buffer.png')
cv2.imwrite('temp.png', border_bar)
full_img = cv2.imread('temp.png')


for key in region_dict:
    stat_capture = np.array(region_grabber(region_dict[key]))
    stat_capture = cv2.cvtColor(stat_capture, cv2.COLOR_BGR2RGB)
    full_img = scale_img(stat_capture, full_img)
    full_img = scale_img(border_bar, full_img)
cv2.imwrite('temp.png', full_img)

time.sleep(1)
pyautogui.click(x=93, y=664)
time.sleep(1)
pyautogui.click(x=423, y=304)
time.sleep(1)

for key in resource_dict:
    stat_capture = np.array(region_grabber(resource_dict[key]))
    stat_capture = cv2.cvtColor(stat_capture, cv2.COLOR_BGR2RGB)
    full_img = scale_img(stat_capture, full_img)
    full_img = scale_img(border_bar, full_img)
cv2.imwrite('temp.png', full_img)

pyautogui.click(x=941, y=102)
time.sleep(1)

for key in rewind_pre_scroll:
    stat_capture = np.array(region_grabber(rewind_pre_scroll[key]))
    stat_capture = cv2.cvtColor(stat_capture, cv2.COLOR_BGR2RGB)
    full_img = scale_img(stat_capture, full_img)
    full_img = scale_img(border_bar, full_img)
cv2.imwrite('temp.png', full_img)

pyautogui.moveTo(1234,267)
pyautogui.dragTo(1234,365,0.5, button='left')
time.sleep(1)

for key in rewind_post_scroll:
    stat_capture = np.array(region_grabber(rewind_post_scroll[key]))
    stat_capture = cv2.cvtColor(stat_capture, cv2.COLOR_BGR2RGB)
    full_img = scale_img(stat_capture, full_img)
    full_img = scale_img(border_bar, full_img)
cv2.imwrite('temp.png', full_img)

pyautogui.moveTo(1234,365)
pyautogui.dragTo(1234,267,0.5, button='left')
time.sleep(1)