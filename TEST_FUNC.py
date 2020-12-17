# -*- coding: utf-8 -*-
import os
from PyQt5.QtWidgets import QFileDialog
import time
from TEST import Ui_MainWindow

# 提示信息
def show_log(window, some_msg):
    def print_(func):
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
                window.statusbar.clearMessage()
            except:
                if not window.statusbar.currentMessage():
                    window.statusbar.showMessage(some_msg)
            else:
                return True
        return wrapper
    return print_


class TESTCustW(Ui_MainWindow):
    def __init__(self, window):
        super(TESTCustW, self).__init__()
        self.setupUi(window)
        self._custom_setup()

    def _custom_setup(self):
        self.change_extension = show_log(self, "请输入正确的后缀格式")(self.change_extension)
        self.filter_extension_file = show_log(self, "请检查文件夹是否存在或具有权限")(self.filter_extension_file)
        self.fix = ""
        self.pushButton.clicked.connect(lambda: self.select_folder())
        self.lineEdit_2.textChanged.connect(self.change_extension)

    # 选择文件夹
    def select_folder(self):
        dir_ = QFileDialog.getExistingDirectory()
        if dir_:
            self.lineEdit.setText(dir_)
            self.change_extension(self.lineEdit_2.text())

    # 文件格式输入
    def change_extension(self, ext: str):
        _ = ext.replace(" ", "")
        assert len(_)
        preExt = _.split(".")
        if len(preExt) == 1:
            pass
        elif len(preExt) == 2:
            assert len(preExt[0]) == 0 and len(preExt[1]) > 0
        else:
            raise ValueError
        self.fix = "." + preExt[-1]
        self.listWidget.clear()
        assert self.filter_extension_file()

    # 输出符合条件的文件信息
    def filter_extension_file(self, dir_=None):
        if dir_ is None:
            dir_ = self.lineEdit.text()
        assert dir_
        if os.path.exists(dir_):
            for file in os.listdir(dir_):
                absolute_path = os.path.join(dir_, file)
                filetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getctime(absolute_path)))
                complete_msg = "文件生成时间：%s \t" % filetime + absolute_path
                if os.path.isdir(absolute_path):
                    self.filter_extension_file(absolute_path)
                elif os.path.splitext(os.path.basename(file))[-1] == self.fix:
                    self.listWidget.addItem(complete_msg)


