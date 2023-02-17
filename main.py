# lip 
import sys
import math
from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QSpacerItem, QSizePolicy
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QThread, Signal, Slot
from PySide6.QtGui import QIcon, QPixmap, QImage
from PySide6.QtMultimedia import QMediaDevices
# widgets
from mainWindow import Ui_MainWindow
import cv2


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()        
        self.cameraViewlabels = {}
        self.availableCameras =[]
        self.combBoxes = {}
        self.theLabel = []
        self.threads = {}
        # # Thread in charge of updating the image
        # self.th = Thread(self)
        # self.th.finished.connect(self.close)
        # self.th.updateFrame.connect(self.setImage)

        # self.setWindowFlag(Qt.FramelessWindowHint)
        # window functions 
        self.ui.verticalLayout_11.removeWidget(self.ui.popUpNotificationContainer)
        self.setWindowFlag(Qt.FramelessWindowHint)
        # window functions 
        self.ui.closeBtn.clicked.connect(self.closeFun)

        self.ui.notificationBtn.clicked.connect(self.notificationFun)
        self.ui.closeNotificationBtn.clicked.connect(self.closeNotificationFun)
        # left
        icon12 = QIcon()
        icon12.addPixmap(QPixmap(":/icons/Icons/chevrons-right.svg"), QIcon.Mode.Normal, QIcon.State.Off)
        self.ui.expandCamSettings.setIcon(icon12)
        self.ui.homeBtn.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.ui.popUpNotificationContainer.setVisible(False)
        # self.expandRightMenuFun(False)
        self.ui.leftMenuContainer.setMaximumWidth(60)
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

        #Window state
        self.ui.minimizeBtn.clicked.connect(self.showMinimized)
        self.ui.restoreBtn.clicked.connect(self.toggleFullScreen)

    # main Functions 
    # ///////////////////////////////////////////////// Window State
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

    def getAvailableCameras(self):
        cameras = QMediaDevices.videoInputs()
        self.availableCameras.append("select camera")
        for cameraDevice in cameras:
            self.availableCameras.append(cameraDevice.description())
        
    # ///////////////////////////////////////////////// clearing taps
    def clear_tab(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
    def clear_tab_except_first(self, layout):
        for i in range(layout.count() - 1):
            child = layout.takeAt(1)
            if child.widget():
                child.widget().deleteLater()


    def notificationFun(self):
        
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
        self.clear_tab_except_first(self.ui.verticalLayout_20)
        self.cameraViewlabels.clear()
        self.availableCameras.clear()
        num = self.ui.screencountCombobox.currentIndex()
        self.getAvailableCameras()
        n = num
        w = 0
        x = math.pow(n, 1/2)
        if n > 0:
            for i in range(int(n)):
                if (i%int(x)) == 0:
                    w +=1                
                self.cameraViewLabel = QLabel()
                self.cameraViewLabel.setText(str(i))
                self.cameraViewLabel.setObjectName(u"label")
                self.cameraViewLabel.setStyleSheet(u"background-color: black;")
                self.cameraViewlabels[i] = self.cameraViewLabel
                self.cameraViewLabel.setAlignment(Qt.AlignCenter)
                if (i + 1) == n and (i%int(x)) == 0:
                    self.ui.gridLayout.addWidget(self.cameraViewLabel, int(w), (i%int(x)) , 1, int(x))
                else:
                    self.ui.gridLayout.addWidget(self.cameraViewLabel, int(w), (i%int(x)),1,1)
                self.cameraOptionscomboBox = QComboBox(self.ui.cameraComboboxListFrame)
                self.cameraOptionscomboBox.id_number = i
                self.cameraOptionscomboBox.setObjectName(u"cameraOptionscomboBox"+str(i))
                self.ui.verticalLayout_20.addWidget(self.cameraOptionscomboBox, 0, Qt.AlignTop)
                self.cameraOptionscomboBox.addItems(self.availableCameras)
                self.combBoxes[i] = self.cameraOptionscomboBox 
                self.cameraOptionscomboBox.currentIndexChanged.connect(self.runWebCam)
                
                
                # self.th.updateFrame.connect(self.setImage)

        self.verticalSpacer_2 = QSpacerItem(20, 104, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.ui.verticalLayout_20.addItem(self.verticalSpacer_2)

    # @Slot(QImage)
    def runWebCam(self, idx):
        combo = self.sender()
        print("combo.id_number")
        print(combo.id_number)
        if combo.id_number >= 0 :
            if idx > 0 :
                print(f"idx ==  {idx}")
                self.theLabel.append(combo.id_number)
                self.threads[combo.id_number] = Thread(idx - 1)
                self.threads[combo.id_number].updateFrame.connect(self.setImage)
            elif idx == 0:
                self.threads[combo.id_number].stop()

        elif (combo.id_number == 0):
            # self.threads[combo.id_number].stop()
            pass
            
        else:
            self.theLabel.remove(combo.id_number) 
        print(f"Selected the variable {idx} from combo {combo.id_number}")
        self.threads[combo.id_number].start()

    @Slot(QImage)
    def setImage(self, image):
        for i in self.cameraViewlabels:
            if i in self.theLabel:
                self.cameraViewlabels[i].setPixmap(QPixmap.fromImage(image))
            else:
                pass
                # self.cameraViewlabels[i].setPixmap(None)
        # self.cameraViewLabel.setPixmap(QPixmap.fromImage(image))

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





class Thread(QThread):
    updateFrame = Signal(QImage)
   
    def __init__(self, index) -> None:
        super(Thread, self).__init__()
       
        self.index = index
        self.__thread_active = True

    def run(self):
        if  self.index >= 0:
            self.cap = cv2.VideoCapture(self.index)
        while self.__thread_active and self.index >= 0:
            ret, frame = self.cap.read()
            if not ret:
                continue
            h, w, ch = frame.shape
            img = QImage(frame.data, w, h, ch * w, QImage.Format_RGB888)
            scaled_img = img.scaled(640, 480, Qt.KeepAspectRatio)
            # Emit signal
            self.updateFrame.emit(scaled_img)
            if self.__thread_active == False:
                break
        # sys.exit(-1)
    def stop(self):
        self.__thread_active = False
        self.quit()






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())