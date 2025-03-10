import numpy as np
import cv2

def affine_transform(image: np.ndarray, src_points: np.ndarray, dst_points: np.ndarray) -> np.ndarray:
    """
    Apply an affine transformation.

    Args:
        image (np.ndarray): Input image.
        src_points (np.ndarray): Coordinates in the source image.
        dst_points (np.ndarray): Desired coordinates in the output image.

    Returns:
        np.ndarray: Transformed image.

    Example:
        transformed = affine_transform(img, np.float32([[0,0],[1,0],[0,1]]),
                                           np.float32([[10,10],[20,10],[10,20]]))
    """
    matrix = cv2.getAffineTransform(src_points, dst_points)
    rows, cols = image.shape[:2]
    return cv2.warpAffine(image, matrix, (cols, rows))