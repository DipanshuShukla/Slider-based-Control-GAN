# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StyleGan.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StyleGan2(object):
    def setupUi(self, StyleGan2):
        StyleGan2.setObjectName("StyleGan2")
        StyleGan2.resize(720, 480)
        self.centralwidget = QtWidgets.QWidget(StyleGan2)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setEnabled(True)
        self.scrollArea.setGeometry(QtCore.QRect(20, 50, 180, 360))
        self.scrollArea.setMouseTracking(False)
        self.scrollArea.setTabletTracking(False)
        self.scrollArea.setAcceptDrops(True)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 178, 358))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.sliderBox = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.sliderBox.setGeometry(QtCore.QRect(10, 10, 160, 40))
        self.sliderBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.sliderBox.setObjectName("sliderBox")
        self.sliderTitle = QtWidgets.QLabel(self.sliderBox)
        self.sliderTitle.setGeometry(QtCore.QRect(10, 0, 40, 10))
        self.sliderTitle.setObjectName("sliderTitle")
        self.slider = QtWidgets.QSlider(self.sliderBox)
        self.slider.setGeometry(QtCore.QRect(0, 20, 150, 20))
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("slider")
        self.sliderBox_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.sliderBox_2.setGeometry(QtCore.QRect(10, 60, 160, 40))
        self.sliderBox_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.sliderBox_2.setObjectName("sliderBox_2")
        self.sliderTitle_7 = QtWidgets.QLabel(self.sliderBox_2)
        self.sliderTitle_7.setGeometry(QtCore.QRect(10, 0, 40, 10))
        self.sliderTitle_7.setObjectName("sliderTitle_7")
        self.slider_7 = QtWidgets.QSlider(self.sliderBox_2)
        self.slider_7.setGeometry(QtCore.QRect(0, 20, 150, 20))
        self.slider_7.setOrientation(QtCore.Qt.Horizontal)
        self.slider_7.setObjectName("slider_7")
        self.sliderBox_3 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.sliderBox_3.setGeometry(QtCore.QRect(10, 110, 160, 40))
        self.sliderBox_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.sliderBox_3.setObjectName("sliderBox_3")
        self.sliderTitle_8 = QtWidgets.QLabel(self.sliderBox_3)
        self.sliderTitle_8.setGeometry(QtCore.QRect(10, 0, 40, 10))
        self.sliderTitle_8.setObjectName("sliderTitle_8")
        self.slider_8 = QtWidgets.QSlider(self.sliderBox_3)
        self.slider_8.setGeometry(QtCore.QRect(0, 20, 150, 20))
        self.slider_8.setOrientation(QtCore.Qt.Horizontal)
        self.slider_8.setObjectName("slider_8")
        self.sliderBox_4 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.sliderBox_4.setGeometry(QtCore.QRect(10, 160, 160, 40))
        self.sliderBox_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.sliderBox_4.setObjectName("sliderBox_4")
        self.sliderTitle_9 = QtWidgets.QLabel(self.sliderBox_4)
        self.sliderTitle_9.setGeometry(QtCore.QRect(10, 0, 40, 10))
        self.sliderTitle_9.setObjectName("sliderTitle_9")
        self.slider_9 = QtWidgets.QSlider(self.sliderBox_4)
        self.slider_9.setGeometry(QtCore.QRect(0, 20, 150, 20))
        self.slider_9.setOrientation(QtCore.Qt.Horizontal)
        self.slider_9.setObjectName("slider_9")
        self.sliderBox_5 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.sliderBox_5.setGeometry(QtCore.QRect(10, 210, 160, 40))
        self.sliderBox_5.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.sliderBox_5.setObjectName("sliderBox_5")
        self.sliderTitle_10 = QtWidgets.QLabel(self.sliderBox_5)
        self.sliderTitle_10.setGeometry(QtCore.QRect(10, 0, 40, 10))
        self.sliderTitle_10.setObjectName("sliderTitle_10")
        self.slider_10 = QtWidgets.QSlider(self.sliderBox_5)
        self.slider_10.setGeometry(QtCore.QRect(0, 20, 150, 20))
        self.slider_10.setOrientation(QtCore.Qt.Horizontal)
        self.slider_10.setObjectName("slider_10")
        self.sliderBox_6 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.sliderBox_6.setGeometry(QtCore.QRect(10, 260, 160, 40))
        self.sliderBox_6.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.sliderBox_6.setObjectName("sliderBox_6")
        self.sliderTitle_11 = QtWidgets.QLabel(self.sliderBox_6)
        self.sliderTitle_11.setGeometry(QtCore.QRect(10, 0, 40, 10))
        self.sliderTitle_11.setObjectName("sliderTitle_11")
        self.slider_11 = QtWidgets.QSlider(self.sliderBox_6)
        self.slider_11.setGeometry(QtCore.QRect(0, 20, 150, 20))
        self.slider_11.setOrientation(QtCore.Qt.Horizontal)
        self.slider_11.setObjectName("slider_11")
        self.sliderBox_7 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.sliderBox_7.setGeometry(QtCore.QRect(10, 310, 160, 40))
        self.sliderBox_7.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.sliderBox_7.setObjectName("sliderBox_7")
        self.sliderTitle_12 = QtWidgets.QLabel(self.sliderBox_7)
        self.sliderTitle_12.setGeometry(QtCore.QRect(10, 0, 40, 10))
        self.sliderTitle_12.setObjectName("sliderTitle_12")
        self.slider_12 = QtWidgets.QSlider(self.sliderBox_7)
        self.slider_12.setGeometry(QtCore.QRect(0, 20, 150, 20))
        self.slider_12.setOrientation(QtCore.Qt.Horizontal)
        self.slider_12.setObjectName("slider_12")
        self.sliderBox_8 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.sliderBox_8.setGeometry(QtCore.QRect(10, 360, 160, 40))
        self.sliderBox_8.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.sliderBox_8.setObjectName("sliderBox_8")
        self.sliderTitle_13 = QtWidgets.QLabel(self.sliderBox_8)
        self.sliderTitle_13.setGeometry(QtCore.QRect(10, 0, 40, 10))
        self.sliderTitle_13.setObjectName("sliderTitle_13")
        self.slider_13 = QtWidgets.QSlider(self.sliderBox_8)
        self.slider_13.setGeometry(QtCore.QRect(0, 20, 150, 20))
        self.slider_13.setOrientation(QtCore.Qt.Horizontal)
        self.slider_13.setObjectName("slider_13")
        self.sliderBox_9 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.sliderBox_9.setGeometry(QtCore.QRect(10, 410, 160, 40))
        self.sliderBox_9.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.sliderBox_9.setObjectName("sliderBox_9")
        self.sliderTitle_15 = QtWidgets.QLabel(self.sliderBox_9)
        self.sliderTitle_15.setGeometry(QtCore.QRect(10, 0, 40, 10))
        self.sliderTitle_15.setObjectName("sliderTitle_15")
        self.slider_15 = QtWidgets.QSlider(self.sliderBox_9)
        self.slider_15.setGeometry(QtCore.QRect(0, 20, 150, 20))
        self.slider_15.setOrientation(QtCore.Qt.Horizontal)
        self.slider_15.setObjectName("slider_15")
        self.sliderBox_10 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.sliderBox_10.setGeometry(QtCore.QRect(10, 460, 160, 40))
        self.sliderBox_10.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.sliderBox_10.setObjectName("sliderBox_10")
        self.sliderTitle_16 = QtWidgets.QLabel(self.sliderBox_10)
        self.sliderTitle_16.setGeometry(QtCore.QRect(10, 0, 40, 10))
        self.sliderTitle_16.setObjectName("sliderTitle_16")
        self.slider_16 = QtWidgets.QSlider(self.sliderBox_10)
        self.slider_16.setGeometry(QtCore.QRect(0, 20, 150, 20))
        self.slider_16.setOrientation(QtCore.Qt.Horizontal)
        self.slider_16.setObjectName("slider_16")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 20, 180, 20))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 420, 100, 20))
        self.pushButton.setObjectName("pushButton")
        self.imageBox = QtWidgets.QLabel(self.centralwidget)
        self.imageBox.setGeometry(QtCore.QRect(230, 20, 470, 420))
        self.imageBox.setText("")
        self.imageBox.setPixmap(QtGui.QPixmap("../../GitHub/Slider-based-Control-GAN/avatar.jpeg"))
        self.imageBox.setScaledContents(True)
        self.imageBox.setObjectName("imageBox")
        StyleGan2.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(StyleGan2)
        self.statusbar.setObjectName("statusbar")
        StyleGan2.setStatusBar(self.statusbar)

        self.retranslateUi(StyleGan2)
        QtCore.QMetaObject.connectSlotsByName(StyleGan2)

    def retranslateUi(self, StyleGan2):
        _translate = QtCore.QCoreApplication.translate
        StyleGan2.setWindowTitle(_translate("StyleGan2", "MainWindow"))
        self.sliderTitle.setText(_translate("StyleGan2", "abc"))
        self.sliderTitle_7.setText(_translate("StyleGan2", "abc"))
        self.sliderTitle_8.setText(_translate("StyleGan2", "abc"))
        self.sliderTitle_9.setText(_translate("StyleGan2", "abc"))
        self.sliderTitle_10.setText(_translate("StyleGan2", "abc"))
        self.sliderTitle_11.setText(_translate("StyleGan2", "abc"))
        self.sliderTitle_12.setText(_translate("StyleGan2", "abc"))
        self.sliderTitle_13.setText(_translate("StyleGan2", "abc"))
        self.sliderTitle_15.setText(_translate("StyleGan2", "abc"))
        self.sliderTitle_16.setText(_translate("StyleGan2", "abc"))
        self.comboBox.setItemText(0, _translate("StyleGan2", "Faces"))
        self.comboBox.setItemText(1, _translate("StyleGan2", "Other"))
        self.comboBox.setItemText(2, _translate("StyleGan2", "Another"))
        self.pushButton.setText(_translate("StyleGan2", "Random"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StyleGan2 = QtWidgets.QMainWindow()
    ui = Ui_StyleGan2()
    ui.setupUi(StyleGan2)
    StyleGan2.show()
    sys.exit(app.exec_())
