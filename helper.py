import pyautogui
import cv2
import numpy as np
import subprocess

def find_and_click_image(image_path):
    try:
        # Activate Google Chrome window using AppleScript
        script = '''
        tell application "Google Chrome"
            activate
        end tell
        '''
        subprocess.run(["osascript", "-e", script])

        screenshot = pyautogui.screenshot()
        screenshot.save("debug_screenshot.png")
        print("Saved screenshot for debugging. Check debug_screenshot.png")

        location = pyautogui.locateOnScreen(image_path, confidence=0.8)

        print("Image search completed.")

        if location:            
            print(location)
            scaling_factor = 1/2  # Adjust according to your setup
            x, y = location.left * scaling_factor, location.top * scaling_factor
            print(f"Moving to coordinates: {x}, {y}")
            pyautogui.sleep(1)
            pyautogui.moveTo(x + location.width / 4, y + location.height / 4, duration=0.5)
            pyautogui.click(button='left')
        else:
            print("Image not found on the screen.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the path to your image file
print("Detected screen size:", pyautogui.size())
image_path = "./start_button.png"  # Update with your image path
find_and_click_image(image_path)
print("Done!")
