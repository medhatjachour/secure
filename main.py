# lip 
import sys
import math
import cv2
from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve,QThread,Signal
from PySide6.QtGui import QIcon, QPixmap, QImage
# widgets
from mainWindow import Ui_MainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()        
        self.labels = []
        

        # threads = 
        self.threadIsActive = False
        
        self.doneQuiting = False

        
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
  
    # update Images 
    def imageUpdateSlot(self, image): 
        self.threadIsActive = True
        for i in self.labels:
            i.setPixmap(QPixmap.fromImage(image))
    def cancelImage(self):
        self.worker.stop()
        self.doneQuiting == True
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
        
        if self.threadIsActive:
            self.cancelImage()
        
        if self.doneQuiting:
            self.clear_tab(self.ui.gridLayout)
        else:
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

        self.worker = cameraWorker()
        self.worker.imageUpdate.connect(self.imageUpdateSlot)
        self.worker.start()
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

class cameraWorker(QThread):
    imageUpdate = Signal(QImage)
    def run(self):
        self.activate = True
        capturedVid = cv2.VideoCapture(0)
        while self.activate:
            returned, aFrame =  capturedVid.read()
            if returned:
                Image = cv2.cvtColor(aFrame, cv2.COLOR_BGR2RGB)
                flippedImage = cv2.flip(Image, 1)
                convertToQtFormat = QImage(flippedImage.data, flippedImage.shape[1], flippedImage.shape[0], QImage.Format_RGB888)
                pic = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.imageUpdate.emit(pic)
    def stop(self):
        self.activate = False
        self.quit()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())