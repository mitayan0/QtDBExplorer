# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'connection_type_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
    QPushButton, QSizePolicy, QWidget)

class Ui_DialogTitle(object):
    def setupUi(self, DialogTitle):
        if not DialogTitle.objectName():
            DialogTitle.setObjectName(u"DialogTitle")
        DialogTitle.resize(452, 338)
        self.label_2 = QLabel(DialogTitle)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 30, 351, 20))
        self.label_3 = QLabel(DialogTitle)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 100, 49, 16))
        self.lineEdit = QLineEdit(DialogTitle)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(70, 100, 251, 21))
        self.label_4 = QLabel(DialogTitle)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 140, 49, 16))
        self.lineEdit_2 = QLineEdit(DialogTitle)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(70, 140, 251, 21))
        self.pushButton = QPushButton(DialogTitle)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(310, 270, 75, 24))
        self.pushButton_2 = QPushButton(DialogTitle)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(220, 270, 75, 24))
        self.label = QLabel(DialogTitle)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 0, 151, 20))

        self.retranslateUi(DialogTitle)

        QMetaObject.connectSlotsByName(DialogTitle)
    # setupUi

    def retranslateUi(self, DialogTitle):
        DialogTitle.setWindowTitle(QCoreApplication.translate("DialogTitle", u"New Connection Type", None))
        self.label_2.setText(QCoreApplication.translate("DialogTitle", u"Define a new category for your database connections", None))
        self.label_3.setText(QCoreApplication.translate("DialogTitle", u"Name:", None))
        self.label_4.setText(QCoreApplication.translate("DialogTitle", u"Type:", None))
        self.pushButton.setText(QCoreApplication.translate("DialogTitle", u"Save", None))
        self.pushButton_2.setText(QCoreApplication.translate("DialogTitle", u"Cancel", None))
        self.label.setText(QCoreApplication.translate("DialogTitle", u"Add Connection Type", None))
    # retranslateUi

