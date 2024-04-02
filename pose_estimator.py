import cv2 as cv
from topic import Subscriber
import numpy as np
from yaml import safe_load

class PoseEstimator:
    def __init__(self) -> None:
        with open("yaml_file") as file:
            data = safe_load(file)
        self.camMatrix, self.tvec, self.rvec, self.dist = [data[i] for i in ("camera_matrix", "tvec", "rvec", "dist")]
        markerlength = 2
        self.mat_sub = Subscriber("/image", "pose_estimator_sub")
        self.params = cv.aruco.DetectorParameters()
        self.dictionary = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_5X5_1000)
        self.detector = cv.aruco.ArucoDetector(self.dictionary, self.params)
        self.objpts = np.array([[-markerlength/2, markerlength/2, 0],
                                [markerlength/2, markerlength/2, 0],
                                [markerlength/2, -markerlength/2, 0],
                                [-markerlength/2, -markerlength/2, 0]])

    def detect(self, mat):
        self.corners, self.ids, self.rejected = self.detector.detectMarkers(mat)
    def estimate_pose(self):
        sucess, rvec, tvec = cv.solvePnP(self.objpts, self.corners, self.camMatrix, self.dist)
        if sucess:
            return (tvec, rvec)