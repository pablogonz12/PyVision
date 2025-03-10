import numpy as np
import cv2

def histogram_equalization(image: np.ndarray) -> np.ndarray:
    """
    Perform histogram equalization for contrast enhancement.

    Args:
        image (np.ndarray): Grayscale image.

    Returns:
        np.ndarray: Image after histogram equalization.

    Example:
        result = histogram_equalization(gray_img)
    """
    return cv2.equalizeHist(image)