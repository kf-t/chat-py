import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainLogin import Ui_MainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()  # 这是类函数的名称
    ui.setupUi(MainWindow)  # 运行类函数里的setupUi
    MainWindow.show()  # 显示窗口
    sys.exit(app.exec())
