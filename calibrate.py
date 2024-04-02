import cv2 as cv
import glob
import numpy as np

def calibrate():
    size = 1

    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    checkerboardsize = (6, 5)
    objp = np.zeros((np.multiply(checkerboardsize)), np.float32)
    objp[:, :2] = np.mgrid[0:checkerboardsize[0], 0:checkerboardsize[1]].T.reshape(-1, 2)
    objp *= size

    objpts = []
    imgpts = []

    images = glob.glob("*.jpg")
    for fname in images:
        img = cv.cvtColor(cv.imread(fname), cv.COLOR_BGR2GRAY)
        success, corners = cv.findChessboardCorners(img, checkerboardsize, None)
        if success:
            objpts.append(objp)
            new_corners = cv.cornerSubPix(img, corners, (11, 11), (-1, -1), criteria)
            imgpts.append(new_corners)

    sucess, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpts, imgpts, img.shape[::-1], None, None)

    if not sucess:
        print("Failed to calibrate camera")
    
    mean_error = 0
    for i in range(len(objpts)):
        imgpts2, _ = cv.projectPoints(objpts[i], rvecs[i], tvecs[i], mtx, dist)
        error = cv.norm(imgpts[i], imgpts2, cv.NORM_L2) / len(imgpts2)
        mean_error += error

    print(f"total error {mean_error}")


def find_pose(mat):
    pass