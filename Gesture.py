import cv2
import mediapipe as mp
import pyautogui
import math
import time

# Safety
pyautogui.FAILSAFE = True

# Setup
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)
screen_w, screen_h = pyautogui.size()

click_cooldown = 0
CLICK_DELAY = 0.5  # seconds

with mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
) as hands:

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)

        if result.multi_hand_landmarks:
            hand = result.multi_hand_landmarks[0]
            mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)
            lm = hand.landmark

            # Index finger tip → cursor
            ix, iy = int(lm[8].x * screen_w), int(lm[8].y * screen_h)
            pyautogui.moveTo(ix, iy, duration=0.01)

            # Thumb + index distance
            tx, ty = int(lm[4].x * screen_w), int(lm[4].y * screen_h)
            distance = math.hypot(ix - tx, iy - ty)

            # Click condition
            current_time = time.time()
            if distance < 40 and (current_time - click_cooldown) > CLICK_DELAY:
                pyautogui.click()
                click_cooldown = current_time
                print("CLICK")

        cv2.imshow("Gesture Control", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
