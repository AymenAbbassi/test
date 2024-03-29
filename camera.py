import cv2 as cv
from threading import Thread
import logger

class CameraConfig:

    def __init__(self, fps=None, height=None, width=None, brightness=None, contrast=None, saturation=None, exposure=None) -> None:
        self.configs = []
        self.user_configs = [
        #This depends on the camera capabilites and the backend.
        [cv.CAP_PROP_FPS, fps],
        [cv.CAP_PROP_FRAME_HEIGHT, height],
        [cv.CAP_PROP_FRAME_WIDTH, width],
        [cv.CAP_PROP_BRIGHTNESS, brightness],
        [cv.CAP_PROP_CONTRAST, contrast],
        [cv.CAP_PROP_SATURATION, saturation],
        [cv.CAP_PROP_EXPOSURE, exposure],
        ]

        self.configs = [self.user_configs[i] for i in range(len(self.user_configs)) if self.user_configs[i][1] is not None]
        
class Camera:

    def __init__(self, configs: CameraConfig, name: str, index: int, attemp_threshold: int) -> None:
        self.capture = cv.VideoCapture(index)
        self.apply_configs(configs)
        self.name = name
        self.attempts = 0
        self.attempts_threshold = attemp_threshold
        self.frame: cv.Mat | None = None

        self.camera_process = Thread(target=self.monitor_mats, daemon=True)
        self.camera_process.start()
    
    def __str__(self) -> str:
        return self.name
        
    def apply_configs(self, camera_configs: CameraConfig) -> None:
        for prod_id, value in camera_configs.configs:
            self.capture.set(prod_id, value)

    def monitor_mats(self) -> None:
        while self.isOpened():
            success, frame = self.capture.read()
            if not success:
                self.attempts += 1
                logger.log(f"Could not read frame from {self.name}", "err")
                self.frame = None
            if self.attempts >= self.attempts_threshold:
                logger.log(f"Camera {self.name} has exceeded the maximum number of attempts. Check camera connection", "fatal")
                self.frame = None
            
            self.frame = frame
    
    def get_frame(self) -> cv.Mat | None:
        return self.frame
    
    def close(self) -> None:
        self.capture.release()

    def isOpened(self) -> bool:
        return self.capture.isOpened()
    
if __name__ == "__main__":
    camera1_configs = CameraConfig(contrast=20, width=600, height=800)
    camera1 = Camera(camera1_configs, "camera1", 0, 100)
    while True:
        if (frame := camera1.get_frame()) is not None:
            cv.imshow("video1", frame)
            if cv.waitKey(1) & 0xFF == ord("q"):
                break

    cv.destroyAllWindows()
    camera1.close()