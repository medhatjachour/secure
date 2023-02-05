# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'V0UCSrYB.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu
from Custom_Widgets.Widgets import QCustomStackedWidget

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1834, 966)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"*{\n"
"border:none;\n"
"background-color:transparent;\n"
"\n"
"padding:0;\n"
"margin:0;\n"
"color:#fff;\n"
"}\n"
"\n"
"#screencountCombobox{\n"
"\n"
"background-color:black;\n"
"border-radius: 10px;\n"
"\n"
"padding:5;\n"
"margin:2;\n"
"color:#fff;\n"
"}\n"
"\n"
"#centralwidget{\n"
"background-color: #1f232a;\n"
"}\n"
"#leftMenuSubContainer{\n"
"background-color: #16191d;\n"
"}\n"
"\n"
"#leftMenuSubContainer QPushButton{\n"
"text-align:left;\n"
"padding:5px 10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"#centerMenuSubContainer, #rightMenuSubContainer{\n"
" background-color: #2c313c;\n"
"}\n"
"\n"
"#frame, #frame_7,#popUpNotificationSubContainer{\n"
"background-color: #16191d;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"#headerContainer, #footerContainer{\n"
"background-color: #2c313c;\n"
"}")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.leftMenuContainer.setMaximumSize(QSize(200, 16777215))
        self.leftMenuContainer.setStyleSheet(u"background-color: #16191d;\n"
"")
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        self.leftMenuSubContainer.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_1 = QFrame(self.leftMenuSubContainer)
        self.frame_1.setObjectName(u"frame_1")
        self.frame_1.setStyleSheet(u"background-color: #16191d")
        self.frame_1.setFrameShape(QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_1)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menuButton = QPushButton(self.frame_1)
        self.menuButton.setObjectName(u"menuButton")
        self.menuButton.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/Icons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuButton.setIcon(icon)
        self.menuButton.setIconSize(QSize(24, 24))
        self.menuButton.setFlat(False)

        self.verticalLayout_3.addWidget(self.menuButton)


        self.verticalLayout_2.addWidget(self.frame_1, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.leftMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.homeBtn = QPushButton(self.frame_2)
        self.homeBtn.setObjectName(u"homeBtn")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.homeBtn.setFont(font)
        self.homeBtn.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/Icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon1)
        self.homeBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.homeBtn)

        self.recordsBtn = QPushButton(self.frame_2)
        self.recordsBtn.setObjectName(u"recordsBtn")
        self.recordsBtn.setFont(font)
        self.recordsBtn.setStyleSheet(u"")
        icon2 = QIcon()
        iconThemeName = u"white"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u":/icons/Icons/database.svg", QSize(), QIcon.Normal, QIcon.Off)
        
        self.recordsBtn.setIcon(icon2)
        self.recordsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.recordsBtn)

        self.analyticsBtn = QPushButton(self.frame_2)
        self.analyticsBtn.setObjectName(u"analyticsBtn")
        self.analyticsBtn.setFont(font)
        self.analyticsBtn.setAutoFillBackground(False)
        self.analyticsBtn.setStyleSheet(u"")
        icon3 = QIcon()
        iconThemeName = u"#fff"
        if QIcon.hasThemeIcon(iconThemeName):
            icon3 = QIcon.fromTheme(iconThemeName)
        else:
            icon3.addFile(u":/icons/Icons/activity.svg", QSize(), QIcon.Normal, QIcon.Off)
        
        self.analyticsBtn.setIcon(icon3)
        self.analyticsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.analyticsBtn)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.leftMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.settingsBtn = QPushButton(self.frame_3)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setFont(font)
        self.settingsBtn.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/Icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBtn.setIcon(icon4)
        self.settingsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_6.addWidget(self.settingsBtn)

        self.infoBtn = QPushButton(self.frame_3)
        self.infoBtn.setObjectName(u"infoBtn")
        self.infoBtn.setFont(font)
        self.infoBtn.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/Icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.infoBtn.setIcon(icon5)
        self.infoBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_6.addWidget(self.infoBtn)

        self.helpBtn = QPushButton(self.frame_3)
        self.helpBtn.setObjectName(u"helpBtn")
        self.helpBtn.setFont(font)
        self.helpBtn.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/Icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.helpBtn.setIcon(icon6)
        self.helpBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_6.addWidget(self.helpBtn)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.leftMenuSubContainer, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.leftMenuContainer, 0, Qt.AlignLeft)

        self.centerMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.centerMenuContainer.setObjectName(u"centerMenuContainer")
        self.centerMenuContainer.setMinimumSize(QSize(200, 0))
        self.centerMenuContainer.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.centerMenuSubContainer = QWidget(self.centerMenuContainer)
        self.centerMenuSubContainer.setObjectName(u"centerMenuSubContainer")
        self.centerMenuSubContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_7 = QVBoxLayout(self.centerMenuSubContainer)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centerMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.closeCenterMenuButton = QPushButton(self.frame)
        self.closeCenterMenuButton.setObjectName(u"closeCenterMenuButton")
        icon7 = QIcon()
        icon7.addFile(u":/icons/Icons/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeCenterMenuButton.setIcon(icon7)
        self.closeCenterMenuButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.closeCenterMenuButton, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.frame, 0, Qt.AlignTop)

        self.centerMenuPages = QCustomStackedWidget(self.centerMenuSubContainer)
        self.centerMenuPages.setObjectName(u"centerMenuPages")
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.verticalLayout_8 = QVBoxLayout(self.settingsPage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_2 = QLabel(self.settingsPage)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_2)

        self.centerMenuPages.addWidget(self.settingsPage)
        self.informationPage = QWidget()
        self.informationPage.setObjectName(u"informationPage")
        self.verticalLayout_9 = QVBoxLayout(self.informationPage)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_3 = QLabel(self.informationPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_3)

        self.centerMenuPages.addWidget(self.informationPage)
        self.helpPage = QWidget()
        self.helpPage.setObjectName(u"helpPage")
        self.verticalLayout_10 = QVBoxLayout(self.helpPage)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_4 = QLabel(self.helpPage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_4)

        self.centerMenuPages.addWidget(self.helpPage)

        self.verticalLayout_7.addWidget(self.centerMenuPages)


        self.verticalLayout_5.addWidget(self.centerMenuSubContainer, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.centerMenuContainer)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy1)
        self.mainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_11 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        self.horizontalLayout_4 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.frame_4 = QFrame(self.headerContainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.headerContainer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setSpacing(7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.notificationBtn = QPushButton(self.frame_5)
        self.notificationBtn.setObjectName(u"notificationBtn")
        icon8 = QIcon()
        icon8.addFile(u":/icons/Icons/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notificationBtn.setIcon(icon8)

        self.horizontalLayout_5.addWidget(self.notificationBtn)

        self.rightMenuBtn = QPushButton(self.frame_5)
        self.rightMenuBtn.setObjectName(u"rightMenuBtn")
        icon9 = QIcon()
        icon9.addFile(u":/icons/Icons/more-horizontal.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.rightMenuBtn.setIcon(icon9)
        self.rightMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.rightMenuBtn)

        self.rightMenuProfileBtn = QPushButton(self.frame_5)
        self.rightMenuProfileBtn.setObjectName(u"rightMenuProfileBtn")
        icon10 = QIcon()
        icon10.addFile(u":/icons/Icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.rightMenuProfileBtn.setIcon(icon10)
        self.rightMenuProfileBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.rightMenuProfileBtn)


        self.horizontalLayout_4.addWidget(self.frame_5, 0, Qt.AlignHCenter)

        self.frame_6 = QFrame(self.headerContainer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.minimizeBtn = QPushButton(self.frame_6)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        icon11 = QIcon()
        icon11.addFile(u":/icons/Icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon11)
        self.minimizeBtn.setIconSize(QSize(24, 20))

        self.horizontalLayout_3.addWidget(self.minimizeBtn)

        self.restoreBtn = QPushButton(self.frame_6)
        self.restoreBtn.setObjectName(u"restoreBtn")
        icon12 = QIcon()
        icon12.addFile(u":/icons/Icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreBtn.setIcon(icon12)

        self.horizontalLayout_3.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.frame_6)
        self.closeBtn.setObjectName(u"closeBtn")
        icon13 = QIcon()
        icon13.addFile(u":/icons/Icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon13)

        self.horizontalLayout_3.addWidget(self.closeBtn)


        self.horizontalLayout_4.addWidget(self.frame_6, 0, Qt.AlignRight)


        self.verticalLayout_11.addWidget(self.headerContainer)

        self.mainBodyContent = QWidget(self.mainBodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy)
        self.mainBodyContent.setMinimumSize(QSize(1459, 806))
        self.horizontalLayout_6 = QHBoxLayout(self.mainBodyContent)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.mainContentContainer = QWidget(self.mainBodyContent)
        self.mainContentContainer.setObjectName(u"mainContentContainer")
        self.horizontalLayout_13 = QHBoxLayout(self.mainContentContainer)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.mainPages = QCustomStackedWidget(self.mainContentContainer)
        self.mainPages.setObjectName(u"mainPages")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.horizontalLayout_12 = QHBoxLayout(self.homePage)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, -1)
        self.webcamWidget = QWidget(self.homePage)
        self.webcamWidget.setObjectName(u"webcamWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.webcamWidget.sizePolicy().hasHeightForWidth())
        self.webcamWidget.setSizePolicy(sizePolicy2)

        self.horizontalLayout_12.addWidget(self.webcamWidget)

        self.expandCamSettings = QPushButton(self.homePage)
        self.expandCamSettings.setObjectName(u"expandCamSettings")
        icon14 = QIcon()
        icon14.addFile(u":/icons/Icons/chevrons-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.expandCamSettings.setIcon(icon14)
        self.expandCamSettings.setIconSize(QSize(24, 30))

        self.horizontalLayout_12.addWidget(self.expandCamSettings, 0, Qt.AlignRight)

        self.rightMenuContainer = QCustomSlideMenu(self.homePage)
        self.rightMenuContainer.setObjectName(u"rightMenuContainer")
        self.rightMenuContainer.setMinimumSize(QSize(300, 0))
        self.rightMenuContainer.setMaximumSize(QSize(300, 806))
        self.horizontalLayout_7 = QHBoxLayout(self.rightMenuContainer)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.rightMenuSubContainer = QWidget(self.rightMenuContainer)
        self.rightMenuSubContainer.setObjectName(u"rightMenuSubContainer")
        self.verticalLayout_12 = QVBoxLayout(self.rightMenuSubContainer)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.rightMenuSubContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, -1, -1, -1)
        self.detectionSettingsBtn = QPushButton(self.frame_7)
        self.detectionSettingsBtn.setObjectName(u"detectionSettingsBtn")
        icon15 = QIcon()
        icon15.addFile(u":/icons/Icons/eye.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.detectionSettingsBtn.setIcon(icon15)
        self.detectionSettingsBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.detectionSettingsBtn)

        self.line = QFrame(self.frame_7)
        self.line.setObjectName(u"line")
        font2 = QFont()
        font2.setBold(True)
        font2.setWeight(75)
        self.line.setFont(font2)
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.line)

        self.cameraSettingsButton = QPushButton(self.frame_7)
        self.cameraSettingsButton.setObjectName(u"cameraSettingsButton")
        icon16 = QIcon()
        icon16.addFile(u":/icons/Icons/camera.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cameraSettingsButton.setIcon(icon16)

        self.horizontalLayout_8.addWidget(self.cameraSettingsButton)

        self.closeRightMenuBtn = QPushButton(self.frame_7)
        self.closeRightMenuBtn.setObjectName(u"closeRightMenuBtn")
        self.closeRightMenuBtn.setIcon(icon7)

        self.horizontalLayout_8.addWidget(self.closeRightMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_12.addWidget(self.frame_7)

        self.rightMenuPages = QCustomStackedWidget(self.rightMenuSubContainer)
        self.rightMenuPages.setObjectName(u"rightMenuPages")
        self.cameraSettingPage = QWidget()
        self.cameraSettingPage.setObjectName(u"cameraSettingPage")
        self.verticalLayout_15 = QVBoxLayout(self.cameraSettingPage)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.screencountCombobox = QComboBox(self.cameraSettingPage)
        icon17 = QIcon()
        icon17.addFile(u":/icons/Icons/monitor.svg", QSize(), QIcon.Normal, QIcon.On)
        self.screencountCombobox.addItem(icon17, "")
        self.screencountCombobox.addItem("")
        self.screencountCombobox.addItem("")
        self.screencountCombobox.addItem("")
        self.screencountCombobox.addItem("")
        self.screencountCombobox.addItem("")
        self.screencountCombobox.addItem("")
        self.screencountCombobox.addItem("")
        self.screencountCombobox.addItem("")
        self.screencountCombobox.addItem("")
        self.screencountCombobox.addItem("")
        self.screencountCombobox.setObjectName(u"screencountCombobox")
        self.screencountCombobox.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.screencountCombobox.sizePolicy().hasHeightForWidth())
        self.screencountCombobox.setSizePolicy(sizePolicy3)
        self.screencountCombobox.setCursor(QCursor(Qt.PointingHandCursor))
        self.screencountCombobox.setMouseTracking(False)
        self.screencountCombobox.setAutoFillBackground(False)

        self.verticalLayout_15.addWidget(self.screencountCombobox, 0, Qt.AlignTop)

        self.rightMenuPages.addWidget(self.cameraSettingPage)
        self.objdetectSettingPage = QWidget()
        self.objdetectSettingPage.setObjectName(u"objdetectSettingPage")
        self.verticalLayout_13 = QVBoxLayout(self.objdetectSettingPage)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_10 = QFrame(self.objdetectSettingPage)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_10)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.pushButton_2 = QPushButton(self.frame_10)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setIcon(icon15)
        self.pushButton_2.setIconSize(QSize(24, 24))

        self.verticalLayout_14.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.frame_10)
        self.pushButton.setObjectName(u"pushButton")
        icon18 = QIcon()
        icon18.addFile(u":/icons/Icons/record.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon18)
        self.pushButton.setIconSize(QSize(24, 24))

        self.verticalLayout_14.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.frame_10)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon19 = QIcon()
        icon19.addFile(u":/icons/Icons/category.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon19)
        self.pushButton_3.setIconSize(QSize(24, 24))

        self.verticalLayout_14.addWidget(self.pushButton_3)

        self.horizontalSlider = QSlider(self.frame_10)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_14.addWidget(self.horizontalSlider)


        self.verticalLayout_13.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.objdetectSettingPage)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)

        self.verticalLayout_13.addWidget(self.frame_11)

        self.rightMenuPages.addWidget(self.objdetectSettingPage)

        self.verticalLayout_12.addWidget(self.rightMenuPages)


        self.horizontalLayout_7.addWidget(self.rightMenuSubContainer)


        self.horizontalLayout_12.addWidget(self.rightMenuContainer)

        self.mainPages.addWidget(self.homePage)
        self.savedRecordsPage = QWidget()
        self.savedRecordsPage.setObjectName(u"savedRecordsPage")
        self.verticalLayout_17 = QVBoxLayout(self.savedRecordsPage)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_10 = QLabel(self.savedRecordsPage)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_10)

        self.mainPages.addWidget(self.savedRecordsPage)
        self.analyticsPage = QWidget()
        self.analyticsPage.setObjectName(u"analyticsPage")
        self.verticalLayout_16 = QVBoxLayout(self.analyticsPage)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_9 = QLabel(self.analyticsPage)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_9)

        self.mainPages.addWidget(self.analyticsPage)

        self.horizontalLayout_13.addWidget(self.mainPages)


        self.horizontalLayout_6.addWidget(self.mainContentContainer)


        self.verticalLayout_11.addWidget(self.mainBodyContent)

        self.popUpNotificationContainer = QCustomSlideMenu(self.mainBodyContainer)
        self.popUpNotificationContainer.setObjectName(u"popUpNotificationContainer")
        self.verticalLayout_18 = QVBoxLayout(self.popUpNotificationContainer)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, -1, -1)
        self.popUpNotificationSubContainer = QWidget(self.popUpNotificationContainer)
        self.popUpNotificationSubContainer.setObjectName(u"popUpNotificationSubContainer")
        self.verticalLayout_19 = QVBoxLayout(self.popUpNotificationSubContainer)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_12 = QLabel(self.popUpNotificationSubContainer)
        self.label_12.setObjectName(u"label_12")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setUnderline(False)
        font3.setWeight(75)
        self.label_12.setFont(font3)

        self.verticalLayout_19.addWidget(self.label_12)

        self.frame_8 = QFrame(self.popUpNotificationSubContainer)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_11 = QLabel(self.frame_8)
        self.label_11.setObjectName(u"label_11")
        sizePolicy1.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy1)
        font4 = QFont()
        font4.setPointSize(10)
        self.label_11.setFont(font4)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_11)

        self.closeNotificationBtn = QPushButton(self.frame_8)
        self.closeNotificationBtn.setObjectName(u"closeNotificationBtn")
        self.closeNotificationBtn.setIcon(icon7)
        self.closeNotificationBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.closeNotificationBtn, 0, Qt.AlignRight)


        self.verticalLayout_19.addWidget(self.frame_8)


        self.verticalLayout_18.addWidget(self.popUpNotificationSubContainer)


        self.verticalLayout_11.addWidget(self.popUpNotificationContainer)

        self.footerContainer = QWidget(self.mainBodyContainer)
        self.footerContainer.setObjectName(u"footerContainer")
        self.horizontalLayout_11 = QHBoxLayout(self.footerContainer)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.footerContainer)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font4)

        self.horizontalLayout_11.addWidget(self.label_13)

        self.frame_9 = QFrame(self.footerContainer)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_11.addWidget(self.frame_9)

        self.sizeGrip = QFrame(self.footerContainer)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(20, 20))
        self.sizeGrip.setMaximumSize(QSize(20, 20))
        self.sizeGrip.setFrameShape(QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_11.addWidget(self.sizeGrip)


        self.verticalLayout_11.addWidget(self.footerContainer)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainPages.setCurrentIndex(0)
        self.rightMenuPages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuButton.setToolTip(QCoreApplication.translate("MainWindow", u"Open Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuButton.setText("")
#if QT_CONFIG(tooltip)
        self.homeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Go to Home", None))
#endif // QT_CONFIG(tooltip)
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
#if QT_CONFIG(tooltip)
        self.recordsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"View Saved Records", None))
#endif // QT_CONFIG(tooltip)
        self.recordsBtn.setText(QCoreApplication.translate("MainWindow", u"Saved Records", None))
#if QT_CONFIG(tooltip)
        self.analyticsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"View Analytics", None))
#endif // QT_CONFIG(tooltip)
        self.analyticsBtn.setText(QCoreApplication.translate("MainWindow", u"Analytics", None))
#if QT_CONFIG(tooltip)
        self.settingsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Go to Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.infoBtn.setToolTip(QCoreApplication.translate("MainWindow", u"View Info", None))
#endif // QT_CONFIG(tooltip)
        self.infoBtn.setText(QCoreApplication.translate("MainWindow", u"Info", None))
#if QT_CONFIG(tooltip)
        self.helpBtn.setToolTip(QCoreApplication.translate("MainWindow", u"View Help", None))
#endif // QT_CONFIG(tooltip)
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"More Menu", None))
        self.closeCenterMenuButton.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.notificationBtn.setText("")
        self.rightMenuBtn.setText("")
        self.rightMenuProfileBtn.setText("")
        self.minimizeBtn.setText("")
        self.restoreBtn.setText("")
        self.closeBtn.setText("")
        self.detectionSettingsBtn.setText(QCoreApplication.translate("MainWindow", u"Detection", None))
        self.cameraSettingsButton.setText(QCoreApplication.translate("MainWindow", u"Camera settings", None))
        self.closeRightMenuBtn.setText("")
        self.screencountCombobox.setItemText(0, QCoreApplication.translate("MainWindow", u"Select Monitors", None))
        self.screencountCombobox.setItemText(1, QCoreApplication.translate("MainWindow", u"1 Screen", None))
        self.screencountCombobox.setItemText(2, QCoreApplication.translate("MainWindow", u"2 Screens", None))
        self.screencountCombobox.setItemText(3, QCoreApplication.translate("MainWindow", u"3 Screens", None))
        self.screencountCombobox.setItemText(4, QCoreApplication.translate("MainWindow", u"4 Screens", None))
        self.screencountCombobox.setItemText(5, QCoreApplication.translate("MainWindow", u"5 Screens", None))
        self.screencountCombobox.setItemText(6, QCoreApplication.translate("MainWindow", u"6 Screens", None))
        self.screencountCombobox.setItemText(7, QCoreApplication.translate("MainWindow", u"7 Screens", None))
        self.screencountCombobox.setItemText(8, QCoreApplication.translate("MainWindow", u"8 Screens", None))
        self.screencountCombobox.setItemText(9, QCoreApplication.translate("MainWindow", u"9 Screens", None))
        self.screencountCombobox.setItemText(10, QCoreApplication.translate("MainWindow", u"10 Screens", None))

        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Start Detection", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Record", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Select Object", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Saved Records", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Analytics", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Notification", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Notification Message", None))
        self.closeNotificationBtn.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"SecureVision", None))
    # retranslateUi

