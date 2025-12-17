from ultralytics import YOLO

class ObstacleDetector:
    """
    Detects obstacles in an image using YOLOv8.
    """

    def __init__(self, model_path="yolov8n.pt"):
        self.model = YOLO(model_path)

    def detect(self, image_path):
        """
        Runs object detection on an image and returns bounding boxes.
        """
        results = self.model(image_path)[0]
        obstacles = []

        for box in results.boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            obstacles.append({
                "bbox": (
                    int(x1),
                    int(y1),
                    int(x2),
                    int(y2)
                )
            })

        return obstacles

