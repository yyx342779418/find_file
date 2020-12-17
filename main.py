# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from TEST_FUNC  import TESTCustW

if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = QMainWindow()
    # 控件功能连接
    TESTCustW(test)
    test.show()
    sys.exit(app.exec_())

