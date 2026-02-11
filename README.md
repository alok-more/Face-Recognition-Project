# 🎯 Face Recognition System using OpenCV & SQLite

A real-time **Face Recognition System** built using **Python**, **OpenCV (LBPH algorithm)**, and **SQLite**.  
The system captures face images, trains a model, stores user data in a database, and recognizes faces using a webcam.

---

## 📌 Features

- 📸 Capture face images using webcam
- 🧠 Train model using **LBPH Face Recognizer**
- 🗄️ Store user details (ID, Name, Age) in **SQLite**
- 🔍 Real-time face detection & recognition
- 🧑 Display recognized person's name and age
- ❌ Shows **Unknown** for unrecognized faces

---

## 🛠️ Technologies Used

- Python 3.13
- OpenCV (opencv-contrib-python)
- NumPy
- Pillow (PIL)
- SQLite
- Haar Cascade Classifier

---

## 📥 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/alok-more/Face-Recognition-Project.git
cd face-recognition-system
```

### 2. Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install opencv-contrib-python numpy pillow
```

**Note**: Use `opencv-contrib-python` instead of `opencv-python` to get the face recognition module.

### 4. Create Required Directories

```bash
mkdir dataSet
mkdir recognizer
```

### 5. Set Up Database

```bash
python setup_database.py
```
---