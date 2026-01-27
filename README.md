# Gesture Control Python Script

This project enables **full desktop control using hand gestures** via a webcam. It allows you to move the cursor, click, open files, close programs, and select text lines with intuitive gestures.

## Features

- **Cursor Control:** Move your mouse using your index fingertip.
- **Single Click:** Pinch thumb and index finger.
- **Double Click / Open File:** Pinch distance variation.
- **Drag / Select:** Pinch and hold.
- **Close Window:** Pinch thumb and middle finger.
- **Select Line in Text Editor:** Pinch variation for line selection.

## Requirements

- Python 3.11 or higher
- Libraries:
  - OpenCV (`cv2`)
  - MediaPipe (`mediapipe==0.10.9`)
  - PyAutoGUI (`pyautogui`)

```bash
python -m pip install opencv-python mediapipe==0.10.9 pyautogui
```

## Usage

1. Connect your webcam.
2. Run the script:

```bash
python Gesture.py
```

3. Move your index finger to control the cursor.
4. Use gestures to perform actions:
   - **Pinch thumb + index** → Click
   - **Pinch distance variation** → Double click / drag
   - **Thumb + middle** → Close window
   - **Pinch long** → Select line

5. Press `ESC` to exit the program.

## Notes

- Ensure your Python environment is **Python 3.11**, not Python 3.14 or others.
- Gesture thresholds may require **tuning depending on camera distance and screen resolution**.
- For desktop file control, predefine coordinates or use `pyautogui.locateOnScreen('file.png')` for dynamic selection.
- The script has a built-in **cooldown** to prevent accidental repeated clicks.

## Safety

- `pyautogui.FAILSAFE` is enabled. Move your mouse to the top-left corner to immediately stop the program if something goes wrong.
- Be cautious when using gestures that **close windows** or perform destructive actions.

---

This setup provides a foundation for **OS control with hand gestures**, allowing further customization for applications like opening specific files, controlling slides in presen