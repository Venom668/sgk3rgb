import sys
from PyQt5 import QtWidgets, QtGui
from functools import partial
from sgk3rgb.core import ctl
from sgk3rgb.gui.app import Ui_MainWindow


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
        try:
            exec("self.ui." + button + '_led.setStyleSheet("background-color: rgb(' + str(selectedColor[0]) + "," + str(selectedColor[1]) + "," + str(selectedColor[2]) + ');")')
            ctl.change_light(button.split('_')[1], selectedColor)
        except NameError:
            print("Select color first.")

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.label.setPixmap(QtGui.QPixmap("sgk3rgb/gui/layout.png"))
        self.ui.colorButton.clicked.connect(self.colorDialog)
        self.ui.reattach.clicked.connect(ctl.reattach_device)
        self.ui.attach.clicked.connect(ctl.detach_device)

        btns = ctl.keycodes.keys()
        for btn in btns:
            exec("self.ui.button_" + btn + ".clicked.connect(partial(self.buttonClick, 'button_" + btn + "'))")

def main():
    app = QtWidgets.QApplication([0])
    application = MainWindow()
    application.show()
    sys.exit(app.exec_())