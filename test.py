import sys
from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QThread, Signal, Slot
from PySide6.QtGui import QImage
from PySide6.QtGui import QIcon, QPixmap, QImage
from PySide6.QtMultimedia import QMediaDevices
import cv2

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QGridLayout(self)
        self.lists = ["1", "2", "3"]
        self.availableCameras = []
        self.th = Thread(self)
        self.th.updateFrame.connect(self.setImage)

        for i in range(5):

            self.label = QtWidgets.QLabel(self)
            self.label.id_number = i
            self.label.setStyleSheet(u"background-color: black;")
            self.layout.addWidget(self.label, i, 0)
            
            self.combobox = QtWidgets.QComboBox(self)
            self.combobox.id_number = i
            self.getAvailableCameras()
            self.combobox.addItems(self.availableCameras)
            self.layout.addWidget(self.combobox, i, 1)
            self.combobox.currentIndexChanged.connect(self.runWebCam)


    #@Slot(QImage)
    def runWebCam(self, idx):
        combo = self.sender()
        print(f"Selected the variable {idx} from combo {combo.id_number}")
        self.th.start()

    #@Slot(QImage)
    def setImage(self, image):
        self.label.setPixmap(QPixmap.fromImage(image))
    
    def getAvailableCameras(self):
        cameras = QMediaDevices.videoInputs()
        for cameraDevice in cameras:
            self.availableCameras.append(cameraDevice.description())




class Thread(QThread):
    updateFrame = Signal(QImage)
    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.status = True
        self.cap = True

    def run(self):
        self.cap = cv2.VideoCapture(0)
        while self.status:
            ret, frame = self.cap.read()
            if not ret:
                continue
            h, w, ch = frame.shape
            img = QImage(frame.data, w, h, ch * w, QImage.Format_RGB888)
            scaled_img = img.scaled(640, 480, Qt.KeepAspectRatio)
            # Emit signal
            self.updateFrame.emit(scaled_img)
        sys.exit(-1)



if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())










































        

    

