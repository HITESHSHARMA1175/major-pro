# 👁️ AI-Powered Eye-Controlled Mouse (Python + OpenCV + MediaPipe)

A futuristic, hands-free mouse control system powered by **eye movements and blinks** using real-time webcam feed. Designed to enhance accessibility and enable innovative human-computer interaction.

---

## 🧠 Project Objective

The goal is to **control the mouse cursor**, **click**, and **scroll** using only eye gestures:

* Move mouse with **right eye iris**
* Click with **left eye blink**
* Scroll up/down with **right eye blink + gaze direction**

This project combines **Computer Vision** and **Automation** to create a smooth, hands-free experience.

---

## 🧰 Tech Stack

| Tool/Library | Purpose                                ------------------------------------- |
| Python       | Programming language                  |
| OpenCV       | Image & webcam processing             |
| MediaPipe    | Real-time face/eye landmark detection |
| PyAutoGUI    | Simulate mouse control & scrolling    |

---

## 🔍 Use Cases

| Use Case            | Description                                               |
| ------------------- | --------------------------------------------------------- |
| Accessibility       | Helps users with physical disabilities use a computer     |
| Multitasking        | Use eyes to control cursor while hands are busy           |
| Innovation in UI/UX | Explore next-gen HCI (Human-Computer Interaction)         |
| Research Projects   | Ideal for Computer Vision / AI-based BTech/MTech projects |

---

## ⚙️ Features

| Feature               | Description                                                            |
| --------------------- | ---------------------------------------------------------------------- |
| 👁️ Eye Tracking      | Tracks iris position in real time using webcam                         |
| 👡 Cursor Control     | Moves cursor using right eye iris position                             |
| 👨‍🧳 Blink Detection | Detects left and right eye blinks for click and scroll                 |
| ⬆️⬇️ Scroll Support   | Scroll up/down using blink + gaze direction (based on iris Y-axis)     |
| 🪄 Cooldown Logic     | Prevents multiple accidental clicks or scrolls with simple delay logic |

---

## 🔄 Eye Gesture Mapping

| Gesture                     | Action      |
| --------------------------- | ----------- |
| Right eye iris movement     | Move mouse  |
| Left eye blink              | Left click  |
| Right eye blink + look up   | Scroll up   |
| Right eye blink + look down | Scroll down |

---

## 💻 Architecture Diagram (Textual)

```
[ Webcam Feed ]
      ↓
[ OpenCV + MediaPipe ]
      ↓
[ Iris Detection + Blink Detection ]
      ↓
 ┌────────────────┐
 │ Cursor Move  │ ← (Right Eye Iris)
 ├────────────────├
 │ Click Event  │ ← (Left Eye Blink)
 ├────────────────├
 │ Scroll Event │ ← (Right Eye Blink + Direction)
 └────────────────┘
      ↓
[ PyAutoGUI → OS Mouse Control ]
```

## 📆 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/eye-controlled-mouse.git
cd eye-controlled-mouse
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install opencv-python mediapipe pyautogui
```

---

## ▶️ Run the Program

```bash
python eye_mouse.py
```

> Press `ESC` to exit.

---

## 🧾 Requirements

Save the following in a file called `requirements.txt`:

```
opencv-python
mediapipe
pyautogui
```

The program also requires the `face_landmarker.task` model file in the project
directory. It is included in this repository and is used by MediaPipe's Tasks
API.

---

## ⚠️ Notes & Calibration Tips

* Ensure **good lighting** and **direct face angle** to webcam.
* Blink thresholds can be customized for your face.
* Might not work accurately with glasses (glare issues).

---

## 💡 Future Enhancements

* GUI overlay for click feedback
* Scroll speed control
* Voice feedback integration
* Package as .exe / .app for easier use
* Calibration wizard for user-specific tuning

---

## 📜 License

This project is licensed under the **MIT License** — free to use, modify, and share.

---

## 🙌 Author

Made with ❤️ by **[HITESH SHARMA](https://github.com/HITESHSHARMA1175)**

If you like this project, 🌟 star the repo and share it!
