import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

def finger_extended(lm, tip, pip):
    return lm[tip].y < lm[pip].y

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    gesture = "NO HAND"

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            lm = hand_landmarks.landmark

            # Detect finger states
            thumb = lm[4].y < lm[3].y
            index = finger_extended(lm, 8, 6)
            middle = finger_extended(lm, 12, 10)
            ring = finger_extended(lm, 16, 14)
            pinky = finger_extended(lm, 20, 18)

            #Rule-based gesture
            if not index and not middle and not ring and not pinky:
                gesture = "FIST"
            elif index and middle and ring and pinky:
                gesture = "OPEN PALM"
            elif thumb and not index and not middle:
                gesture = "THUMB UP"
            elif index and middle and not ring and not pinky:
                gesture = "PEACE"
            else:
                gesture = "UNKNOWN"

            mp_draw.draw_landmarks(
                img,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

    cv2.putText(
        img,
        gesture,
        (30, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("Hand Tracking", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
