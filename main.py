try :
    from PyQt6 import QtWidgets , uic
except:
    import pip
    pip.main(["install" , "PyQt6"])
    from PyQt6 import QtWidgets , uic

class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()

        uic.loadUi("ui.ui", self)

        self.pushButton.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        print("btn clicked")       

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()



    window.show()


    sys.exit(app.exec())