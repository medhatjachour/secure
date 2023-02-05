# lip 
import sys
import math
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt
# widgets
from mainWindow import Ui_MainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        
        self.labels = []

        self.ui.screencountCombobox.currentIndexChanged.connect(self.addScreens)

    # main Functions 
    # ///////////////////////////////////////////////// clearing taps
    def clear_tab(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

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



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())