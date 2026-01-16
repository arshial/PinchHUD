import cv2
import numpy as np
import mediapipe as mp
import math

CELL = 120
PINCH_THRESH = 0.045

filled = set()
last_draw = None
last_del = None

def dist2d(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

def finger_to_cell(px, py):
    return int(py // CELL), int(px // CELL)

def draw_filled_cells(frame):
    overlay = frame.copy()

    for (r, c) in filled:
        x1 = c * CELL
        y1 = r * CELL
        x2 = x1 + CELL
        y2 = y1 + CELL

        cv2.rectangle(overlay, (x1, y1), (x2, y2), (10, 10, 10), -1)
        cv2.rectangle(overlay, (x1, y1), (x2, y2), (40, 40, 40), 2)

    frame[:] = cv2.addWeighted(overlay, 0.85, frame, 0.15, 0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    model_complexity=1,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
)

cap = cv2.VideoCapture(0)

while True:
    ok, frame = cap.read()
    if not ok:
        break

    frame = cv2.flip(frame, 1)
    H, W = frame.shape[:2]

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    res = hands.process(rgb)

    right_lm = None
    left_lm = None

    if res.multi_hand_landmarks and res.multi_handedness:
        for hand_landmarks, handedness in zip(res.multi_hand_landmarks, res.multi_handedness):
            label = handedness.classification[0].label
            lm = hand_landmarks.landmark
            if label == "Right":
                right_lm = lm
            elif label == "Left":
                left_lm = lm

    draw_filled_cells(frame)

    if right_lm is not None:
        idx = (right_lm[8].x, right_lm[8].y)
        thb = (right_lm[4].x, right_lm[4].y)

        pinch = dist2d(idx, thb) < PINCH_THRESH
        fx, fy = int(idx[0] * W), int(idx[1] * H)
        cell = finger_to_cell(fx, fy)

        cv2.circle(frame, (fx, fy), 6, (0, 0, 0), -1)

        if pinch:
            if cell != last_draw:
                filled.add(cell)
                last_draw = cell
        else:
            last_draw = None

    if left_lm is not None:
        idx = (left_lm[8].x, left_lm[8].y)
        thb = (left_lm[4].x, left_lm[4].y)

        pinch = dist2d(idx, thb) < PINCH_THRESH
        fx, fy = int(idx[0] * W), int(idx[1] * H)
        cell = finger_to_cell(fx, fy)

        if pinch:
            if cell != last_del:
                filled.discard(cell)
                last_del = cell
        else:
            last_del = None

    cv2.imshow("Full-Screen Hidden Grid — Low Opacity Black HUD", frame)

    if (cv2.waitKey(1) & 0xFF) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
hands.close()