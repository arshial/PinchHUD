# Gesture Grid HUD — Hand Tracking Drawing System

A real-time computer vision project that turns your webcam into a **gesture-controlled hidden grid HUD** using **MediaPipe Hands** and **OpenCV**.

You draw and erase invisible grid cells in full screen using **pinch gestures**:
- ✋ Right hand pinch → draw / fill a cell
- 🤚 Left hand pinch → erase a cell

The result feels like painting on an invisible digital surface floating in front of the camera.

---

## How It Works
- The screen is divided into a virtual grid (no visible grid lines)
- Each grid cell can be filled with a low-opacity dark overlay
- MediaPipe tracks hand landmarks in real time
- Distance between thumb tip and index tip detects a pinch
- Pinching with:
  - Right hand → adds a filled cell
  - Left hand → removes a filled cell
- Filled cells persist until erased

---

## Features
- Full-screen hidden grid system
- Two-hand interaction (draw / erase)
- Low-opacity black HUD style overlay
- Stable pinch detection with debounce
- Real-time performance
- No mouse, no keyboard interaction required

---

## Requirements
- Python 3.9+
- Webcam
- macOS / Linux / Windows

### Python Dependencies
```
opencv-python
mediapipe
numpy
```

---

## Installation

### 1) Clone the repository
```bash
git clone https://github.com/<YOUR_USERNAME>/gesture-grid-hud.git
cd gesture-grid-hud
```

### 2) (Recommended) Create virtual environment
```bash
python -m venv .venv
source .venv/bin/activate     # macOS / Linux
# .venv\Scripts\activate    # Windows
```

### 3) Install dependencies
```bash
pip install opencv-python mediapipe numpy
```

---

## Run
```bash
python app.py
```

Press **Q** to quit.

---

## Controls
| Gesture | Action |
|------|------|
| Right hand pinch | Fill / draw cell |
| Left hand pinch | Erase cell |
| Q key | Exit |

---

## Key Parameters (Tuning)

Inside `app.py`:

```python
CELL = 120
PINCH_THRESH = 0.045
```

### CELL
Controls grid resolution:
- Larger value → fewer, bigger cells
- Smaller value → more, smaller cells

### PINCH_THRESH
Pinch sensitivity:
- Lower → harder to trigger
- Higher → easier to trigger

---

## Webcam Troubleshooting
If the camera doesn’t open, try:
```python
cap = cv2.VideoCapture(1)
```
instead of `0`.

---

## Known Limitations
- Lighting conditions affect accuracy
- Very fast hand motion can reduce tracking quality
- Grid resolution is fixed at runtime

---

## Possible Improvements
- Dynamic grid scaling with screen size
- Gesture to clear all cells
- Visual hint for active cell
- Save/load grid state
- Multi-color drawing modes

---

## License
MIT License

Copyright (c) 2026 Arshia

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.
