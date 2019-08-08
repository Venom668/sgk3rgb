from PyQt5 import QtWidgets, QtGui
try:
    from app import Ui_MainWindow
except ImportError:
    from .app import Ui_MainWindow
import sys

def HTMLtoRGB(color):
    color = color.lstrip('#')
    rgb = list((int(color[i:i+2] ,base = 16) for i in (0, 2, 4)))
    return rgb

class MainWindow(QtWidgets.QMainWindow):
    def colorDialog(self):
        color = QtWidgets.QColorDialog.getColor()
        if color.isValid():
            global selectedColor
            selectedColor = HTMLtoRGB(color.name())
            self.ui.colorButton.setStyleSheet("background-color: rgb(" + str(selectedColor[0]) + "," + str(selectedColor[1]) + "," + str(selectedColor[2]) + ");")

    def buttonClick(self, button):
        exec("self.ui." + button + '_led.setStyleSheet("background-color: rgb(' + str(selectedColor[0]) + "," + str(selectedColor[1]) + "," + str(selectedColor[2]) + ');")')
        ctl.change_light(button.split('_')[1], selectedColor)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.label.setPixmap(QtGui.QPixmap("gui/layout.png"))
        self.ui.colorButton.clicked.connect(self.colorDialog)

        self.ui.button_1.clicked.connect(lambda: self.buttonClick('button_1'))
        self.ui.button_a.clicked.connect(lambda: self.buttonClick('button_a'))


def main():
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    sys.exit(app.exec_())

main()