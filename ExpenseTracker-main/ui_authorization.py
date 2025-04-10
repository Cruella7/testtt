# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'authorization.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import image_rc

class Ui_Authorization(object):
    def setupUi(self, Authorization):
        if not Authorization.objectName():
            Authorization.setObjectName(u"Authorization")
        Authorization.resize(993, 549)
        Authorization.setStyleSheet(u"QDialog{\n"
"	\n"
"	\n"
"	\n"
"	background-image: url(:/img/img/back.jpg);\n"
"}\n"
"\n"
"")
        self.groupBox = QGroupBox(Authorization)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(120, 40, 771, 461))
        self.groupBox.setStyleSheet(u"")
        self.pushButton_6 = QPushButton(self.groupBox)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(510, 290, 151, 51))
        self.pushButton_6.setStyleSheet(u"QPushButton {\n"
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
        self.pushButton_5 = QPushButton(self.groupBox)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(350, 290, 151, 51))
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
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
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(170, 110, 71, 61))
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(170, 190, 101, 61))
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(350, 80, 311, 201))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_5 = QLineEdit(self.layoutWidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.verticalLayout.addWidget(self.lineEdit_5)

        self.lineEdit_6 = QLineEdit(self.layoutWidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.verticalLayout.addWidget(self.lineEdit_6)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(350, 240, 311, 31))

        self.retranslateUi(Authorization)

        QMetaObject.connectSlotsByName(Authorization)
    # setupUi

    def retranslateUi(self, Authorization):
        Authorization.setWindowTitle(QCoreApplication.translate("Authorization", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("Authorization", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.pushButton_6.setText(QCoreApplication.translate("Authorization", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.pushButton_5.setText(QCoreApplication.translate("Authorization", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.label_8.setText(QCoreApplication.translate("Authorization", u"<html><head/><body><p><span style=\" font-size:12pt;\">\u041b\u043e\u0433\u0438\u043d</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Authorization", u"<html><head/><body><p><span style=\" font-size:12pt;\">\u041f\u0430\u0440\u043e\u043b\u044c</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Authorization", u"<html><head/><body><p><br/></p></body></html>", None))
    # retranslateUi

