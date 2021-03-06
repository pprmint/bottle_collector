import cv2

class VideoWorker():

    on_image = None
    on_end = None
    interval = 0.5
    started = False

    def __init__(self, camera_number: int = 0):
        self.webcam = cv2.VideoCapture(camera_number)
        return

    def start(self):
        print('Webcam start')
        self.started = True
        # default : 848x480 on MacBook

        while True:
            if self.webcam.isOpened():
                rc, frame = self.webcam.read()
                if not rc:
                    print('Camera image capture failed')
                    continue

                if self.on_image is not None:
                    self.on_image(frame)

                time.sleep(self.interval)
            else:
                print('No available camera')
                break

        self.end()

    def end(self):
        print('End webcam')

        if self.webcam is not None:
            self.webcam.release()
            cv2.destroyAllWindows()

        if self.on_end is not None:
            self.on_end()

vid_worker = VideoWorker()
