import cv2
import numpy as np
import os

def detect_objects_yolo(image, model_cfg, model_weights, conf_threshold=0.5, nms_threshold=0.4):
    """
    YOLO object detection using OpenCV's dnn module.

    Args:
        image (np.ndarray): Input image as a NumPy array (BGR format).
        model_cfg (str): Path to the YOLO config file.
        model_weights (str): Path to the YOLO weights file.
        conf_threshold (float): Minimum confidence to keep detections.
        nms_threshold (float): Non-maximum suppression threshold.

    Returns:
        list: Final bounding boxes after filtering with confidence and NMS.
              Each bounding box is a list: [x, y, width, height, confidence, class_id]

    Example:
        detections = detect_objects_yolo(img, 'yolov3.cfg', 'yolov3.weights')
    """
    net = cv2.dnn.readNetFromDarknet(model_cfg, model_weights)
    
    # Get output layer names
    output_layers = get_output_layers(net)

    # Prepare image for YOLO
    blob = cv2.dnn.blobFromImage(image, 1/255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)

    # Perform forward pass
    outputs = net.forward(output_layers)

    # Extract bounding boxes, confidences, and class IDs
    boxes = []
    confidences = []
    class_ids = []
    height, width = image.shape[:2]

    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > conf_threshold:
                # Scale box coordinates back to original image size
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # Apply Non-Maximum Suppression
    indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)

    final_boxes = []
    if len(indices) > 0:
        for i in indices.flatten():
            x, y, w, h = boxes[i]
            confidence = confidences[i]
            class_id = class_ids[i]
            final_boxes.append([x, y, w, h, confidence, class_id])

    return final_boxes

def get_output_layers(net):
    """
    Get the names of the output layers of the YOLO network.

    Args:
        net (cv2.dnn_Net): The loaded YOLO network.

    Returns:
        list: A list of output layer names.
    """
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    return output_layers

if __name__ == '__main__':
    # Example Usage (replace with your actual paths and image)
    image_path = 'path/to/your/image.jpg'  # Replace with a valid image path
    model_cfg = 'path/to/your/yolov3.cfg'  # Replace with your YOLO config file
    model_weights = 'path/to/your/yolov3.weights'  # Replace with your YOLO weights file

    # Check if files exist
    if not os.path.exists(image_path):
        print(f"Error: Image file not found at {image_path}")
    if not os.path.exists(model_cfg):
        print(f"Error: YOLO config file not found at {model_cfg}")
    if not os.path.exists(model_weights):
        print(f"Error: YOLO weights file not found at {model_weights}")

    # Load image and perform detection
    if os.path.exists(image_path) and os.path.exists(model_cfg) and os.path.exists(model_weights):
        img = cv2.imread(image_path)
        detections = detect_objects_yolo(img, model_cfg, model_weights)

        # Print the detections
        print("Detections:")
        for box in detections:
            x, y, w, h, confidence, class_id = box
            print(f"  Box: {x}, {y}, {w}, {h}, Confidence: {confidence}, Class ID: {class_id}")

        # Visualize the detections (optional)
        for box in detections:
            x, y, w, h, confidence, class_id = box
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green box

        cv2.imshow("YOLO Detections", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()