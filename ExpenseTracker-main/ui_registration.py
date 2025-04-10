# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'regist.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import registr_rc

class Ui_Regist(object):
    def setupUi(self, Regist):
        if not Regist.objectName():
            Regist.setObjectName(u"Regist")
        Regist.resize(854, 391)
        Regist.setMinimumSize(QSize(502, 219))
        Regist.setStyleSheet(u"QDialog{\n"
"	\n"
"	background-image: url(:/fon/img/regist.jpg);\n"
"}")
        self.label_4 = QLabel(Regist)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(370, 10, 181, 31))
        self.pushButton = QPushButton(Regist)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(540, 270, 201, 41))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #4CAF50; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    border: none; /* \u0423\u0431\u0440\u0430\u0442\u044c \u0433\u0440\u0430\u043d\u0438\u0446\u0443 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    color: white; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    padding: 10px 20px; /* \u041e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043e\u043a\u0440\u0443\u0433 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    text-align: center; /* \u0412\u044b\u0440\u0430\u0432\u043d\u0438\u0432\u0430\u043d\u0438\u0435 \u0442\u0435\u043a\u0441\u0442\u0430 \u043f\u043e \u0446\u0435\u043d\u0442\u0440\u0443 */\n"
"    text-decoration: none; /* \u0423\u0431\u0440\u0430\u0442\u044c \u043f\u043e\u0434\u0447\u0435\u0440\u043a\u0438\u0432\u0430\u043d\u0438\u0435 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    display: inline-block;\n"
"    font-size: 16px; /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438"
                        "\u0444\u0442\u0430 */\n"
"    margin: 4px 2px; /* \u0412\u043d\u0435\u0448\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    cursor: pointer; /* \u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u0444\u043e\u0440\u043c\u044b \u043a\u0443\u0440\u0441\u043e\u0440\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"    border-radius: 4px; /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #45a049; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 \u043a\u0443\u0440\u0441\u043e\u0440\u0430 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3e8e41; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0443 */\n"
"}")
        self.label_5 = QLabel(Regist)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(280, 270, 251, 41))
        self.label_5.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 0, 0);")
        self.label_2 = QLabel(Regist)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(190, 160, 51, 16))
        self.label = QLabel(Regist)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 100, 121, 16))
        self.label_3 = QLabel(Regist)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(190, 210, 125, 16))
        self.widget = QWidget(Regist)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(347, 70, 391, 191))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.lineEdit_3 = QLineEdit(self.widget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout.addWidget(self.lineEdit_3)


        self.retranslateUi(Regist)

        QMetaObject.connectSlotsByName(Regist)
    # setupUi

    def retranslateUi(self, Regist):
        Regist.setWindowTitle(QCoreApplication.translate("Regist", u"Dialog", None))
        self.label_4.setText(QCoreApplication.translate("Regist", u"<html><head/><body><p><span style=\" font-size:12pt;\">\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("Regist", u"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label_5.setText("")
        self.label_2.setText(QCoreApplication.translate("Regist", u"<html><head/><body><p><span style=\" font-size:9pt;\">\u043f\u0430\u0440\u043e\u043b\u044c</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Regist", u"<html><head/><body><p><span style=\" font-size:9pt;\">\u043b\u043e\u0433\u0438\u043d</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Regist", u"<html><head/><body><p><span style=\" font-size:9pt;\">\u043f\u043e\u0432\u0442\u043e\u0440\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c</span></p><p><span style=\" font-size:9pt;\"><br/></span></p></body></html>", None))
    # retranslateUi

