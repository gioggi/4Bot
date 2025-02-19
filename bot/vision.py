import pyautogui
import cv2
import numpy as np
from config import ATTACK_TEMPLATE_PATH, LIFE_TEMPLATE_PATH


def screenshot():
    """Capture the screen."""
    return pyautogui.screenshot()


def find_enemy(threshold=0.8):
    """
    Check if the skill is active or not, if is active we have an enemy
    on target.

    threshold: threshold of similarity (0.8 = 80%).
    """
    # All the screen
    screenshot_img = screenshot()
    screenshot_np = np.array(screenshot_img)

    # Convert to grayscale
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)

    # Cut the skill zone
    # the skill zone is a rectangle of 1/4 of the screen in center for the width
    # and 1/4 of the screen in the bottom for the height
    x = screenshot_gray.shape[1] // 4
    y = screenshot_gray.shape[0] // 2
    w = screenshot_gray.shape[1] // 2
    h = screenshot_gray.shape[0] // 4
    skill_zone = screenshot_gray[y:y + h, x:x + w]

    # Load the template
    template = cv2.imread(ATTACK_TEMPLATE_PATH, cv2.IMREAD_GRAYSCALE)

    # Match the template
    result = cv2.matchTemplate(skill_zone, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    return max_val < threshold  # True se non c'è il nemico

def life_check(threshold=0.8):
    """
    Check if the life is low or not, if is low we need to heal.

    threshold: threshold of similarity (0.8 = 80%).
    """
    # All the screen
    screenshot_img = screenshot()
    screenshot_np = np.array(screenshot_img)

    # Convert to grayscale
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)

    # Cut the life zone
    # the life zone is a rectangle of 1/4 of the screen in center for the width
    # and 1/4 of the screen in the top for the height
    x = screenshot_gray.shape[1] // 4
    y = 0
    w = screenshot_gray.shape[1] // 2
    h = screenshot_gray.shape[0] // 4
    life_zone = screenshot_gray[y:y + h, x:x + w]


    # Load the template
    template = cv2.imread(LIFE_TEMPLATE_PATH, cv2.IMREAD_GRAYSCALE)

    # Match the template
    result = cv2.matchTemplate(life_zone, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    return max_val < threshold  # True if life is low