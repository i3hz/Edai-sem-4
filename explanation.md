This script is a **Drowsiness Detection System** using **computer vision and facial landmarks**. It continuously monitors a person's face using a webcam and alerts them if signs of drowsiness or distraction are detected.  

---

## **Key Features of the Script**
1. **Real-Time Face & Feature Detection:**  
   - Uses **Dlib’s pre-trained facial landmark detector** to identify facial features.
   - Detects **eyes and mouth** to analyze drowsiness levels.

2. **Drowsiness Detection:**  
   - Computes **Eye Aspect Ratio (EAR)** to check if eyes are closing.
   - Computes **Mouth Aspect Ratio (MAR)** to detect yawning.
   - If eyes remain closed or yawning persists, an **alarm sound is played**.

3. **Distraction Detection:**  
   - If no face is detected for a certain period, it assumes **distraction** and triggers an alert.

4. **Audio Alerts using Pygame Mixer:**  
   - Plays an alarm sound if **drowsiness or distraction** is detected.

---

## **Code Breakdown**
### 1. **Importing Required Libraries**
The script uses:
- `cv2` (OpenCV) → For video capture and image processing.  
- `dlib` → For face detection and facial landmark extraction.  
- `scipy.spatial.distance` → To compute eye and mouth aspect ratios.  
- `pygame.mixer` → To play alarm sounds.  

### 2. **Supporting Functions**
- `get_max_area_rect(rects)`: Finds the largest detected face.  
- `get_eye_aspect_ratio(eye)`: Computes the **eye aspect ratio (EAR)** to detect eye closure.  
- `get_mouth_aspect_ratio(mouth)`: Computes the **mouth aspect ratio (MAR)** to detect yawning.  

### 3. **Facial Processing Function**
- Initializes **Dlib’s face detector** and **shape predictor**.  
- Captures live video using OpenCV.  
- Detects **face, eyes, and mouth** in the frame.  
- Computes EAR and MAR values.  

### 4. **Alert System**
- **If EAR drops below a threshold** for a set time → **Plays an alert (sleepiness detected)**.  
- **If MAR rises above a threshold** for a set time → **Plays an alert (yawning detected)**.  
- **If no face is detected for a set time** → **Plays an alert (distraction detected)**.  

### 5. **FPS Calculation**
- Measures FPS and displays it on the screen.  

### 6. **Loop & Exit Mechanism**
- Runs continuously until the user presses **‘q’** to quit.  

---

## **How It Works (Demo Steps)**
1. **Run the script.**  
2. The webcam starts and detects your face.  
3. If you **close your eyes for too long**, the system **triggers an alert**.  
4. If you **yawn**, the system **warns you**.  
5. If you **look away from the camera**, the system **alerts for distraction**.  

---

## **Use Cases**
- **Driver Monitoring System**  
  Prevents accidents caused by drowsy driving.  
- **Workplace Monitoring**  
  Alerts users in critical jobs (e.g., machine operators, pilots).  
- **Health Monitoring**  
  Helps track sleepiness patterns for medical research.  

---

This script effectively combines **AI, Computer Vision, and Audio Alerts** to ensure **safety and alertness** in real time. 🚀