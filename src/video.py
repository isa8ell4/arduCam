import time
import cv2  
class Video: 
    def __init__(self, index):
        self.index = index

    def open_camera(self, retries=10, delay=10):
        for i in range(retries):
            capture = cv2.VideoCapture(self.index, cv2.CAP_DSHOW)
            if capture.isOpened():
                ret, frame = capture.read()
                if ret and frame is not None and frame.any():
                    print(f"Camera opened on index {self.index} (try {i + 1})")
                    return capture
            print(f"Retry {i + 1}/{retries}...")
            capture.release()
            time.sleep(delay)
        return None
    
    def displayRaw(self, cap, resolution=3, displayScale=0.5):

        frameCount = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if frameCount % resolution == 0:

                if frameCount == 0:
                    h, w = frame.shape[:2]
                    # print(h, w)
                    h = int(h * displayScale)
                    w = int(w * displayScale)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            
                cv2.namedWindow('video feed', cv2.WINDOW_NORMAL)
                cv2.resizeWindow('video feed', w, h)
                cv2.imshow('video feed', frame)
            frameCount += 1
        cap.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    vid = Video(index=1)
    cap = vid.open_camera()
    vid.displayRaw(cap)
    # cap = cv2.VideoCapture(self.cap, cv2.CAP_DSHOW)
