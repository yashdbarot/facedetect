# Face Data Collection Tool

A Python-based tool for capturing facial images using a webcam, designed for building structured datasets for machine learning and computer vision projects. This script leverages OpenCV's Haar Cascade for accurate face detection and organizes images by individual.

---

## 📌 Features

- **Real-Time Face Detection**: Uses Haar Cascade to detect faces in a video stream.
- **Dataset Creation**: Automatically saves detected faces as images in a structured directory.
- **User-Friendly Operation**: Simple prompts for specifying individual names and easy-to-stop functionality.

---

## 🛠️ Requirements

- Python 3.7 or higher
- OpenCV library (`opencv-python`)
- Functional webcam

---

## 🚀 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yashdbarot/facedetect.git

2. Navigate to the project directory:
   ```bash
   cd face-data-collection-tool

3. Install the required dependencies:
   ```bash
   pip install opencv-python

## 📖 Usage Guide
1. Run the script:
   ```bash
   python facedata2.py

2. Input the person's name when prompted. This will create a folder under dataset/ with the entered name.

3. Capture faces:
  - The script detects and saves faces from the webcam feed.
  - Up to 100 images are saved for each person or until you manually stop the script.

4. Exit the script:
  Press `q` to quit anytime.

## 📂 Dataset Structure
The captured images are organized in the dataset directory as follows:
  ```bash
dataset/
└── [person_name]/
    ├── image1.jpg
    ├── image2.jpg
    └── ...
```

## 📝 Notes
- The Haar Cascade XML file is loaded from OpenCV's default location. Update the path if necessary for custom installations.
- Ensure sufficient lighting for better face detection accuracy.
- Modify the script parameters (`scaleFactor`, `minNeighbors`, etc.) to fine-tune detection for your use case.

## 🤝 Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests for improvements or additional features.

## 💡 Acknowledgments
 - OpenCV: For the powerful computer vision tools used in this project.
 - Community: For inspiration and support in building practical AI solutions.
