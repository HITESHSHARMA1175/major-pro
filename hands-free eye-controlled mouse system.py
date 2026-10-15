import cv2
import mediapipe
import pyautogui
import time
from pathlib import Path

model_path = Path(__file__).with_name("face_landmarker.task")
base_options = mediapipe.tasks.BaseOptions(model_asset_path=str(model_path))
landmarker_options = mediapipe.tasks.vision.FaceLandmarkerOptions(
    base_options=base_options,
    running_mode=mediapipe.tasks.vision.RunningMode.IMAGE,
    num_faces=1,
)
face_landmarker = mediapipe.tasks.vision.FaceLandmarker.create_from_options(
    landmarker_options
)
cam = cv2.VideoCapture(0)
screen_w, screen_h = pyautogui.size()

# Cooldowns
last_click_time = 0
last_scroll_time = 0
click_cooldown = 1  # sec
scroll_cooldown = 1  # sec

while True:
    success, image = cam.read()
    if not success:
        print("Unable to read from the webcam")
        break

    image = cv2.flip(image, 1)
    window_h, window_w, _ = image.shape
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    mp_image = mediapipe.Image(
        image_format=mediapipe.ImageFormat.SRGB, data=rgb_image
    )

    output = face_landmarker.detect(mp_image)
    landmarks_set = output.face_landmarks

    if landmarks_set:
        landmarks = landmarks_set[0]

        # === Cursor Movement with Right Eye Iris ===
        for id, lm in enumerate(landmarks[474:478]):
            x = int(lm.x * window_w)
            y = int(lm.y * window_h)
            if id == 1:
                screen_x = int(screen_w / window_w * x)
                screen_y = int(screen_h / window_h * y)
                pyautogui.moveTo(screen_x, screen_y)
            cv2.circle(image, (x, y), 3, (0, 0, 255), -1)

        # === Left Eye Blink for Click ===
        left_eye = [landmarks[145], landmarks[159]]
        if abs(left_eye[0].y - left_eye[1].y) < 0.01:
            current_time = time.time()
            if current_time - last_click_time > click_cooldown:
                pyautogui.click()
                last_click_time = current_time
                print("Mouse clicked")

        for lm in left_eye:
            x = int(lm.x * window_w)
            y = int(lm.y * window_h)
            cv2.circle(image, (x, y), 3, (0, 255, 255), -1)

        # === Right Eye Blink for Scroll ===
        right_eye = [landmarks[374], landmarks[386]]
        iris_center = landmarks[475]  # Iris center Y for eye direction

        for lm in right_eye:
            x = int(lm.x * window_w)
            y = int(lm.y * window_h)
            cv2.circle(image, (x, y), 3, (255, 255, 0), -1)

        if abs(right_eye[0].y - right_eye[1].y) < 0.01:
            current_time = time.time()
            if current_time - last_scroll_time > scroll_cooldown:
                iris_y = iris_center.y
                if iris_y < 0.45:
                    pyautogui.scroll(100)  # Scroll up
                    print("Scrolled UP")
                elif iris_y > 0.55:
                    pyautogui.scroll(-100)  # Scroll down
                    print("Scrolled DOWN")
                else:
                    print("Blink detected, but looking straight")
                last_scroll_time = current_time

    # Show camera feed
    cv2.imshow("Eye Controlled Mouse + Click + Scroll", image)
    if cv2.waitKey(1) == 27:  # ESC key to exit
        break

cam.release()
face_landmarker.close()
cv2.destroyAllWindows()


#hello 