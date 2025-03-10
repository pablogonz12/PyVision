# PyVision

PyVision is a collection of Python implementations of various computer vision algorithms. This repository serves as a resource for understanding and experimenting with fundamental computer vision techniques. It includes implementations in both pure Python (for educational purposes) and OpenCV (for optimized performance).

This project is intended to provide clear and concise examples of common computer vision algorithms, making it easier to learn and adapt them for your own projects.


## Features

- **Feature Detection**: BRISK, FAST, Harris Corner, Shi-Tomasi, SIFT, SUSAN, MSER
- **Edge Detection**: Canny, Sobel, Prewitt
- **Image Filtering**: Gaussian Blur, Bilateral Filter, Median Filter
- **Transformations**: Affine Transform, Perspective Transform, Histogram Equalization
- **Object Detection**: YOLO implementation

## Project Structure

```
PyVision/
├── src/
│   ├── pure_python/           # Pure Python implementations
│   │   ├── feature_detection/
│   │   ├── edge_detection/
│   │   ├── image_filtering/
│   │   ├── transformations/
│   │   └── object_detection/
│   ├── opencv/               # OpenCV implementations
│   │   ├── feature_detection/
│   │   ├── edge_detection/
│   │   ├── image_filtering/
│   │   ├── transformations/
│   │   └── object_detection/
│   └── filters/              # Additional implementations
├── README.md
├── requirements.txt
└── LICENSE
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/PyVision.git
   ```
2. Navigate to the project directory:
   ```
   cd PyVision
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Pure Python Examples

```python
from src.pure_python.feature_detection.BRISK import Brisk
import cv2
import numpy as np

# Load image
image = cv2.imread('image.jpg', 0)  # Load as grayscale

# Create BRISK detector
detector = Brisk(threshold=30, octaves=4)

# Detect keypoints
keypoints, descriptors = detector.compute(image)

# Print number of keypoints detected
print(f"Detected {len(keypoints)} keypoints")
```

### OpenCV Examples

```python
from src.opencv.feature_detection.brisk_cv2 import run_brisk

# Run BRISK detection on an image
keypoints, descriptors = run_brisk('image.jpg', threshold=30, octaves=3)
```

## Compare Implementations

One of the key benefits of PyVision is the ability to compare pure Python implementations with optimized OpenCV versions:

```python
import cv2
import time
from src.pure_python.edge_detection.canny import canny_edge_detection as canny_pure
from src.opencv.edge_detection.canny_cv2 import canny_edge_detection as canny_cv

# Load image
image = cv2.imread('image.jpg', 0)  # Load as grayscale

# Time pure Python implementation
start = time.time()
edges_pure = canny_pure(image)
pure_time = time.time() - start

# Time OpenCV implementation
start = time.time()
edges_cv = canny_cv(image)
cv_time = time.time() - start

print(f"Pure Python: {pure_time:.4f}s, OpenCV: {cv_time:.4f}s")
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.