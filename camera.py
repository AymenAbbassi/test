import cv2 as cv
import logger

class CameraConfig:

    def __init__(self, fps=None, height=None, width=None, brightness=None, contrast=None, saturation=None, exposure=None) -> None:
        self.configs = []
        self.user_configs = [
        [cv.CAP_PROP_FPS, fps],
        [cv.CAP_PROP_FRAME_HEIGHT, height],
        [cv.CAP_PROP_FRAME_WIDTH, width],
        [cv.CAP_PROP_BRIGHTNESS, brightness],
        [cv.CAP_PROP_CONTRAST, contrast],
        [cv.CAP_PROP_SATURATION, saturation],
        [cv.CAP_PROP_EXPOSURE, exposure],
        ]
        for i in range(len(self.user_configs)):
            if self.user_configs[i][1] is not None:
                self.configs.append(self.user_configs[i])
        
camera1_configs = CameraConfig(fps=20, brightness=50)
for prod_id, value in camera1_configs.configs:
    print(prod_id, value)

class Camera:

    def __init__(self, configs: CameraConfig, name: str, index: int, attemp_threshold: int) -> None:
        self.capture = cv.VideoCapture(index)
        self.apply_configs(configs)
        self.name = name
        self.attempts = 0
        self.attempts_threshold = attemp_threshold
    
    def __str__(self) -> str:
        return self.name
        
    def apply_configs(self, camera_configs: CameraConfig) -> None:
        for prod_id, value in camera_configs.configs:
            self.capture.set(prod_id, value)

    def get_frame(self) -> cv.Mat | None:
        success, frame = self.capture.read()
        if not success:
            self.attempts += 1
            logger.log(f"Could not read frame from {self.name}", "err")
            return None
        if self.attempts >= self.attempts_threshold:
            logger.log(f"Camera {self.name} has exceeded the maximum number of attempts. Check camera connection", "fatal")
            return None
        
        return frame
    
    def close(self) -> None:
        self.capture.release()

    def isOpened(self) -> bool:
        return self.capture.isOpened()