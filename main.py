# lip 
import sys
import cv2
import math
from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QThread, pyqtSignal
from PySide6.QtGui import QIcon, QPixmap, QImage
# widgets
from mainWindow import Ui_MainWindow



class CaptureIpCameraFramesWorker(QThread):
    # Signal emitted when a new image or a new frame is ready.
    ImageUpdated = pyqtSignal(QImage)

    def __init__(self, url) -> None:
        super(CaptureIpCameraFramesWorker, self).__init__()
        # Declare and initialize instance variables.
        self.url = url
        self.__thread_active = True
        self.fps = 0
        self.__thread_pause = False

    def run(self) -> None:
        # Capture video from a network stream.
        cap = cv2.VideoCapture(self.url, cv2.CAP_FFMPEG)
        # Get default video FPS.
        self.fps = cap.get(cv2.CAP_PROP_FPS)
        print(self.fps)
        # If video capturing has been initialized already.q
        if cap.isOpened():
            # While the thread is active.
            while self.__thread_active:
                #
                if not self.__thread_pause:
                    # Grabs, decodes and returns the next video frame.
                    ret, frame = cap.read()
                    # If frame is read correctly.
                    if ret:
                        # Get the frame height, width and channels.
                        height, width, channels = frame.shape
                        # Calculate the number of bytes per line.
                        bytes_per_line = width * channels
                        # Convert image from BGR (cv2 default color format) to RGB (Qt default color format).
                        cv_rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        # Convert the image to Qt format.
                        qt_rgb_image = QImage(cv_rgb_image.data, width, height, bytes_per_line, QImage.Format_RGB888)
                        # Scale the image.
                        # NOTE: consider removing the flag Qt.KeepAspectRatio as it will crash Python on older Windows machines
                        # If this is the case, call instead: qt_rgb_image.scaled(1280, 720) 
                        qt_rgb_image_scaled = qt_rgb_image.scaled(1280, 720, Qt.KeepAspectRatio)  # 720p
                        # qt_rgb_image_scaled = qt_rgb_image.scaled(1920, 1080, Qt.KeepAspectRatio)
                        # Emit this signal to notify that a new image or frame is available.
                        self.ImageUpdated.emit(qt_rgb_image_scaled)
                    else:
                        break
        # When everything done, release the video capture object.
        cap.release()
        # Tells the thread's event loop to exit with return code 0 (success).
        self.quit()

    def stop(self) -> None:
        self.__thread_active = False

    def pause(self) -> None:
        self.__thread_pause = True

    def unpause(self) -> None:
        self.__thread_pause = False


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()        
        self.labels = []
        
        # self.setWindowFlag(Qt.FramelessWindowHint)
        # window functions 
        self.ui.verticalLayout_11.removeWidget(self.ui.popUpNotificationContainer)
        self.setWindowFlag(Qt.FramelessWindowHint)
        # window functions 
        self.ui.closeBtn.clicked.connect(self.closeFun)

        self.ui.notificationBtn.clicked.connect(self.notificationFun)
        self.ui.closeNotificationBtn.clicked.connect(self.closeNotificationFun)
        self.ui.verticalLayout_11.removeWidget(self.ui.popUpNotificationContainer)
        # left
        icon12 = QIcon()
        icon12.addPixmap(QPixmap(":/icons/Icons/chevrons-right.svg"), QIcon.Mode.Normal, QIcon.State.Off)
        self.ui.expandCamSettings.setIcon(icon12)
        self.ui.homeBtn.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.ui.popUpNotificationContainer.setVisible(False)
        # self.expandRightMenuFun(False)
        self.ui.leftMenuContainer.setMaximumWidth(65)
        self.ui.centerMenuContainer.setMinimumWidth(0)
        self.ui.centerMenuContainer.setMaximumWidth(0)
        # self.expandLeftMenuFun(False)

        self.ui.expandCamSettings.clicked.connect(partial( self.expandRightMenuFun, True))
        self.ui.closeRightMenuBtn.clicked.connect(partial( self.expandRightMenuFun, False))
        self.ui.cameraSettingsButton.clicked.connect(self.cameraSettingsButtonFun)
        self.ui.detectionSettingsBtn.clicked.connect(self.detectionSettingsBtnfun)
     
        self.ui.screencountCombobox.currentIndexChanged.connect(self.addScreens)

        # right
        self.ui.menuButton.clicked.connect(self.menuButtonFun)
        self.ui.homeBtn.clicked.connect(self.homeBtnfun)
        self.ui.recordsBtn.clicked.connect(self.recordsBtnfun)
        self.ui.analyticsBtn.clicked.connect(self.analyticsBtnfun)

        self.ui.closeCenterMenuButton.clicked.connect(partial( self.expandLeftMenuFun, False))
        self.ui.settingsBtn.clicked.connect(self.settingsBtnfun)
        self.ui.infoBtn.clicked.connect(self.infoBtnfun)
        self.ui.helpBtn.clicked.connect(self.helpBtnfun)
        self.ui.headerContainer.mouseMoveEvent = self.moveWindow

        self.ui.minimizeBtn.clicked.connect(self.showMinimized)
        
        self.ui.restoreBtn.clicked.connect(self.toggleFullScreen)
  
    def showMinimized(self) -> None:
        return super().showMinimized()
    def toggleFullScreen(self):  
        isullScreen = bool(self.windowState() == Qt.WindowFullScreen)
        if isullScreen:
            self.showNormal()
        else:
            self.showFullScreen()    
    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()
    def moveWindow(self,event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos )
        self.dragPos = event.globalPosition().toPoint()
        event.accept()
    def closeFun(self):
        self.close()
        
    # main Functions 
    # ///////////////////////////////////////////////// clearing taps
    def clear_tab(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def notificationFun(self):
        print(self.width())
        self.ui.popUpNotificationContainer.setMaximumSize(420,100)
        self.ui.popUpNotificationContainer.setMinimumSize(420,100)
        self.ui.popUpNotificationContainer.move(self.width()/3 , self.height()/2.4)
        self.ui.popUpNotificationContainer.setVisible(True)
    def closeNotificationFun(self):
        self.ui.popUpNotificationContainer.setVisible(False)
    # window functions

    #left
    def expandRightMenuFun(self, toggled):
        minwidth = 0
        maxwidth = 300
        widthExtended = 0
        self.ui.rightMenuContainer.setMinimumWidth(0)
        self.ui.rightMenuContainer.setMaximumWidth(1654541)
        width = self.ui.rightMenuContainer.width()
        if toggled:
            if width == minwidth:
                widthExtended = 300
                icon12 = QIcon()
                icon12.addPixmap(QPixmap(":/icons/Icons/chevrons-right.svg"), QIcon.Mode.Normal, QIcon.State.Off)
                self.ui.expandCamSettings.setIcon(icon12)
            if width == maxwidth or width == 300:
                widthExtended = minwidth
                icon12 = QIcon()
                icon12.addPixmap(QPixmap(":/icons/Icons/chevrons-left.svg"), QIcon.Mode.Normal, QIcon.State.Off)
                self.ui.expandCamSettings.setIcon(icon12)
        else:
            widthExtended = 0
            icon12 = QIcon()
            icon12.addPixmap(QPixmap(":/icons/Icons/chevrons-left.svg"), QIcon.Mode.Normal, QIcon.State.Off)
            self.ui.expandCamSettings.setIcon(icon12)
        self.animation = QPropertyAnimation(self.ui.rightMenuContainer, b"maximumWidth")
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.setDuration(450)
        self.animation.setStartValue(width)
        self.animation.setEndValue(widthExtended)
        self.animation.start()
    def cameraSettingsButtonFun(self):
        self.ui.rightMenuPages.setCurrentIndex(0)
    def detectionSettingsBtnfun(self):
        self.ui.rightMenuPages.setCurrentIndex(1)

    def addScreens(self):
        self.clear_tab(self.ui.gridLayout)
        num = self.ui.screencountCombobox.currentIndex()
        print(int(num))
        n = num
        w = 0
        x = math.pow(n, 1/2)
        if n > 0:
            for i in range(int(n)):
                if (i%int(x)) == 0:
                    w +=1                
                print(int(w / 2), (i%int(x)))
                self.label = QLabel()
                self.label.setText(str(i))
                self.label.setObjectName(u"label")
                self.labels.append(self.label)
                self.label.setAlignment(Qt.AlignCenter)
                if (i + 1) == n and (i%int(x)) == 0:
                    self.ui.gridLayout.addWidget(self.label, int(w), (i%int(x)) , 1, int(x))
                else:
                    self.ui.gridLayout.addWidget(self.label, int(w), (i%int(x)),1,1)

    #right
    def homeBtnfun(self):
        self.ui.homeBtn.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.ui.recordsBtn.setStyleSheet(u"background-color:transparent;")
        self.ui.analyticsBtn.setStyleSheet(u"background-color:transparent;")

        self.ui.mainPages.setCurrentIndex(0) 
    def recordsBtnfun(self):
        self.ui.recordsBtn.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.ui.homeBtn.setStyleSheet(u"background-color:transparent;")
        self.ui.analyticsBtn.setStyleSheet(u"background-color:transparent;")
        self.ui.mainPages.setCurrentIndex(1) 
    def analyticsBtnfun(self):
        self.ui.analyticsBtn.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.ui.recordsBtn.setStyleSheet(u"background-color:transparent;")
        self.ui.homeBtn.setStyleSheet(u"background-color:transparent;")
        self.ui.mainPages.setCurrentIndex(2) 

    def menuButtonFun(self):
        minwidth = 60
        maxwidth = 153
        widthExtended = 0
        self.ui.leftMenuContainer.setMinimumWidth(minwidth)
        self.ui.leftMenuContainer.setMaximumWidth(1654541)
        width = self.ui.leftMenuContainer.width()
        if width == minwidth:
            widthExtended = 153
            icon12 = QIcon()
            icon12.addPixmap(QPixmap(":/icons/Icons/align-justify.svg"), QIcon.Mode.Normal, QIcon.State.Off)
            self.ui.menuButton.setIcon(icon12)
     
        if width == maxwidth or width == 153:
            widthExtended = minwidth
            icon12 = QIcon()
            icon12.addPixmap(QPixmap(":/icons/Icons/chevrons-left.svg"), QIcon.Mode.Normal, QIcon.State.Off)
            self.ui.menuButton.setIcon(icon12)
      

        self.animation = QPropertyAnimation(self.ui.leftMenuContainer, b"maximumWidth")
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.setDuration(650)
        self.animation.setStartValue(width)
        self.animation.setEndValue(widthExtended)
        self.animation.start()
    def expandLeftMenuFun(self, toggled):
        minwidth = 0
        widthExtended = 0
        self.ui.centerMenuContainer.setMinimumWidth(0)
        self.ui.centerMenuContainer.setMaximumWidth(1654541)
        width = self.ui.centerMenuContainer.width()
        if toggled:
            widthExtended = 200
        else:
            widthExtended = 0
            self.ui.settingsBtn.setStyleSheet(u"background-color: transparent;")
            self.ui.infoBtn.setStyleSheet(u"background-color:transparent;")
            self.ui.helpBtn.setStyleSheet(u"background-color:transparent;")
        self.animation = QPropertyAnimation(self.ui.centerMenuContainer, b"maximumWidth")
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.setDuration(450)
        self.animation.setStartValue(width)
        self.animation.setEndValue(widthExtended)
        self.animation.start()
    def settingsBtnfun(self):
        self.ui.settingsBtn.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.ui.infoBtn.setStyleSheet(u"background-color:transparent;")
        self.ui.helpBtn.setStyleSheet(u"background-color:transparent;")
        self.expandLeftMenuFun( True)
        self.ui.centerMenuPages.setCurrentIndex(0) 
    def infoBtnfun(self):
        self.ui.infoBtn.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.ui.settingsBtn.setStyleSheet(u"background-color:transparent;")
        self.ui.helpBtn.setStyleSheet(u"background-color:transparent;")
        self.expandLeftMenuFun( True)
        self.ui.centerMenuPages.setCurrentIndex(1) 
    def helpBtnfun(self):
        self.ui.helpBtn.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.ui.infoBtn.setStyleSheet(u"background-color:transparent;")
        self.ui.settingsBtn.setStyleSheet(u"background-color:transparent;")
        self.expandLeftMenuFun( True)
        self.ui.centerMenuPages.setCurrentIndex(2) 



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())