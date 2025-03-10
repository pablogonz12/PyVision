import numpy as np
import cv2

def bilateral_filter(image: np.ndarray, d=9, sigma_color=75, sigma_space=75) -> np.ndarray:
    """
    Apply bilateral filtering for edge-preserving smoothing.

    Args:
        image (np.ndarray): Input image.
        d (int): Diameter of each pixel neighborhood.
        sigma_color (float): Filter sigma in the color space.
        sigma_space (float): Filter sigma in the coordinate space.

    Returns:
        np.ndarray: Filtered image.

    Example:
        output = bilateral_filter(img, d=5, sigma_color=50, sigma_space=50)
    """
    return cv2.bilateralFilter(image, d, sigma_color, sigma_space)