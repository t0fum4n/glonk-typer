import pyautogui
import time
import keyboard

# Flag to control the typing loop
typing_enabled = False

def on_press_t(event):
    global typing_enabled
    typing_enabled = True

def on_press_k(event):
    global typing_enabled
    typing_enabled = False

# Listen for 't' key press to start typing
keyboard.on_press_key("t", on_press_t)

# Listen for 'k' key press to stop typing
keyboard.on_press_key("k", on_press_k)

print("Press 't' to start typing ',roll', press 'k' to stop.")

while True:
    if typing_enabled:
        pyautogui.typewrite(',roll')
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(4)
    time.sleep(0.1)  # A short delay to prevent high CPU usage
