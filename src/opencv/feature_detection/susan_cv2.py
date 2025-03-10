import cv2
import numpy as np

def susan_detection(image: np.ndarray, threshold=25, radius=3):
    """
    Detects corners in an image using a SUSAN-like approach with OpenCV.
    Note: OpenCV does not have a direct SUSAN implementation. This uses a similar concept.

    Args:
        image: A NumPy array representing the grayscale image.
        threshold: Intensity difference threshold.
        radius: Radius of the circular mask.

    Returns:
        A list of (x, y) coordinates of detected corners.
    """

    # Apply a blurring filter to reduce noise
    blurred = cv2.GaussianBlur(image, (2*radius+1, 2*radius+1), 0)

    # Calculate the local variance
    local_variance = cv2.Laplacian(blurred, cv2.CV_64F)
    abs_variance = np.abs(local_variance)
    
    # Threshold the variance to find corners
    _, corner_map = cv2.threshold(abs_variance, threshold, 255, cv2.THRESH_BINARY)
    corner_map = corner_map.astype(np.uint8)

    # Find the coordinates of the corners
    corners = np.column_stack(np.where(corner_map > 0))
    return corners