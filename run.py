import sys
import Ui_dl
import Ui_news
import Ui_offer
from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainW = QMainWindow()# 登录界面
    ui = Ui_dl.Ui_MainWindow()
    ui.setupUi(mainW)

    mainW.show()

    maine = QMainWindow()# 企业信息界面
    ui_new = Ui_news.Ui_MainWindow()
    ui_new.setupUi(maine)

    maino = QMainWindow()# 岗位信息界面
    ui_off = Ui_offer.Ui_MainWindow()
    ui_off.setupUi(maino)
    ui.pushButton.clicked.connect(lambda: {mainW.close(),maine.show()})
    ui_new.pushButton_3.clicked.connect(lambda: {maine.close(),maino.show()})
    ui_off.pushButton_3.clicked.connect(lambda: {maino.close(),maine.show()})
    sys.exit(app.exec_())
