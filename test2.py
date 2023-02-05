from ui_mainwindow import Ui_MainWindow
import sys
from Custom_Widgets.Widgets import *
import cv2
import numpy as np
from PyQt5.QtCore import pyqtSignal, QObject, QThread
from PySide6.QtMultimedia import (QCamera, QImageCapture,
                                  QCameraDevice, QMediaCaptureSession,
                                  QMediaDevices)


from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from ui_mainwindow import Ui_MainWindow



class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        self.show()
        #self.camera_info = None
        #available_cameras = QMediaDevices.videoInputs()
        #self.camera_info = available_cameras[0]
        

        #Expand Center Menu Widget
        self.ui.settingsBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.infoBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.helpBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())

        #Close Center Menu Widget
        self.ui.closeCenterMenuButton.clicked.connect(lambda: self.ui.centerMenuContainer.collapseMenu())

        #Close Notification Menu Widget
        self.ui.closeNotificationBtn.clicked.connect(lambda: self.ui.popUpNotificationContainer.collapseMenu())

        self.gridLayoutWebcamWidget = QtWidgets.QGridLayout(self.ui.webcamWidget)
        self.gridLayoutWebcamWidget.setObjectName("gridLayoutWebcamWidget")

        self.ui.screencountCombobox.activated.connect(self.loopCamFeed)

        



        



	
    def ImageUpdateSlot(self, Image):
        self.ui.label_5.setPixmap(QPixmap.fromImage(Image))

    def CancelFeed(self):
        self.worker1.stop()
    
    def startVideo(self):
        self.worker1 = Worker1()
        self.worker1.start()
        self.worker1.ImageUpdate.connect(self.ImageUpdateSlot)
    
    def loopCamFeed(self):
        n = int(self.ui.screencountCombobox.currentIndex())
        #If any childer in parent then delete 
        if self.gridLayoutWebcamWidget.count() > 0 :
            children = []
            for i in range(self.gridLayoutWebcamWidget.count()):
                child = self.gridLayoutWebcamWidget.itemAt(i).widget()
                if child:
                    children.append(child)
            for child in children:
                child.deleteLater()
        #Loop and apply monitors
        w = 0
        if n > 0:             
            for i in range(int(n)):
                if (i%2) == 0:
                    w +=1                
                #print(int(w / 2), (i%2))
                #ADD MONITORS
                self.label = QtWidgets.QLabel()
                self.label.setText("Screen " +str(i+1))
                self.label.setStyleSheet("background-color: black5;")
                self.label.setAlignment(QtCore.Qt.AlignCenter)
                self.label.setObjectName(u"label")
                self.gridLayoutWebcamWidget.addWidget(self.label, (i%2) ,int(w) )

                #ADD COMBOBOX
                self.comboBox = QComboBox(self.ui.cameraSettingPage)
                self.comboBox.setObjectName(u"comboBox")
                self.ui.verticalLayout_15.addWidget(self.comboBox, 0, Qt.AlignTop)
                #print(self.camera_info)

            


class Worker1(QThread):
    ImageUpdate = pyqtSignal(QImage)
    def __init__(self):
        super().__init__()

    def run(self):
        self.ThreadActive = True
        Capture = cv2.VideoCapture(0)
        while self.ThreadActive:
            ret, frame = Capture.read()
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Image, 1)
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(1200, 900, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)

    def stop(self):
        self.ThreadActive = False
        self.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())