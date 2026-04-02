# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QSplitter, QStatusBar,
    QTabWidget, QTableView, QTextEdit, QToolButton,
    QTreeView, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1169, 675)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actionsave = QAction(MainWindow)
        self.actionsave.setObjectName(u"actionsave")
        self.actionsave_as = QAction(MainWindow)
        self.actionsave_as.setObjectName(u"actionsave_as")
        self.actionopen = QAction(MainWindow)
        self.actionopen.setObjectName(u"actionopen")
        self.actionredo = QAction(MainWindow)
        self.actionredo.setObjectName(u"actionredo")
        self.actionundo = QAction(MainWindow)
        self.actionundo.setObjectName(u"actionundo")
        self.actioncut = QAction(MainWindow)
        self.actioncut.setObjectName(u"actioncut")
        self.actionminimize = QAction(MainWindow)
        self.actionminimize.setObjectName(u"actionminimize")
        self.actionmaximize = QAction(MainWindow)
        self.actionmaximize.setObjectName(u"actionmaximize")
        self.actionquery_tool = QAction(MainWindow)
        self.actionquery_tool.setObjectName(u"actionquery_tool")
        self.actionclose = QAction(MainWindow)
        self.actionclose.setObjectName(u"actionclose")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_12 = QGridLayout(self.centralwidget)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.splitter_3 = QSplitter(self.centralwidget)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Orientation.Horizontal)
        self.splitter = QSplitter(self.splitter_3)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.frame = QFrame(self.splitter)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(200, 0))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.widget, 0, 1, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(Qt.TextFormat.AutoText)

        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)

        self.treeView = QTreeView(self.frame)
        self.treeView.setObjectName(u"treeView")

        self.gridLayout_4.addWidget(self.treeView, 1, 0, 1, 3)

        self.toolButton = QToolButton(self.frame)
        self.toolButton.setObjectName(u"toolButton")

        self.gridLayout_4.addWidget(self.toolButton, 0, 2, 1, 1)

        self.splitter.addWidget(self.frame)
        self.frame_2 = QFrame(self.splitter)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.treeView_2 = QTreeView(self.frame_2)
        self.treeView_2.setObjectName(u"treeView_2")

        self.gridLayout_5.addWidget(self.treeView_2, 0, 0, 1, 1)

        self.splitter.addWidget(self.frame_2)
        self.splitter_3.addWidget(self.splitter)
        self.splitter_2 = QSplitter(self.splitter_3)
        self.splitter_2.setObjectName(u"splitter_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy1)
        self.splitter_2.setOrientation(Qt.Orientation.Vertical)
        self.tabWidget = QTabWidget(self.splitter_2)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabsClosable(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_11 = QGridLayout(self.tab)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.tabWidget_3 = QTabWidget(self.tab)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayout_10 = QGridLayout(self.tab_6)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.plainTextEdit = QPlainTextEdit(self.tab_6)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout_10.addWidget(self.plainTextEdit, 0, 0, 1, 1)

        self.tabWidget_3.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.gridLayout_7 = QGridLayout(self.tab_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.splitter_4 = QSplitter(self.tab_7)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Orientation.Horizontal)
        self.treeView_3 = QTreeView(self.splitter_4)
        self.treeView_3.setObjectName(u"treeView_3")
        self.splitter_4.addWidget(self.treeView_3)
        self.groupBox = QGroupBox(self.splitter_4)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_6 = QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.textEdit = QTextEdit(self.groupBox)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout_6.addWidget(self.textEdit, 0, 0, 1, 4)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_6.addWidget(self.pushButton, 1, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_6.addWidget(self.pushButton_2, 1, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.groupBox)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_6.addWidget(self.pushButton_3, 1, 2, 1, 1)

        self.pushButton_9 = QPushButton(self.groupBox)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout_6.addWidget(self.pushButton_9, 1, 3, 1, 1)

        self.splitter_4.addWidget(self.groupBox)

        self.gridLayout_7.addWidget(self.splitter_4, 0, 0, 1, 1)

        self.tabWidget_3.addTab(self.tab_7, "")

        self.gridLayout_11.addWidget(self.tabWidget_3, 3, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.tab)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_11.addWidget(self.comboBox_2, 0, 0, 1, 1)

        self.widget_2 = QWidget(self.tab)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_6 = QPushButton(self.widget_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSave))
        self.pushButton_6.setIcon(icon)

        self.gridLayout_2.addWidget(self.pushButton_6, 0, 2, 1, 1)

        self.pushButton_7 = QPushButton(self.widget_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentOpen))
        self.pushButton_7.setIcon(icon1)

        self.gridLayout_2.addWidget(self.pushButton_7, 0, 3, 1, 1)

        self.toolButton_2 = QToolButton(self.widget_2)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setPopupMode(QToolButton.ToolButtonPopupMode.MenuButtonPopup)

        self.gridLayout_2.addWidget(self.toolButton_2, 0, 5, 1, 1)

        self.pushButton_8 = QPushButton(self.widget_2)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout_2.addWidget(self.pushButton_8, 0, 6, 1, 1)

        self.pushButton_5 = QPushButton(self.widget_2)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_2.addWidget(self.pushButton_5, 0, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.widget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_2.addWidget(self.pushButton_4, 0, 0, 1, 1)

        self.toolButton_3 = QToolButton(self.widget_2)
        self.toolButton_3.setObjectName(u"toolButton_3")
        self.toolButton_3.setPopupMode(QToolButton.ToolButtonPopupMode.MenuButtonPopup)

        self.gridLayout_2.addWidget(self.toolButton_3, 0, 4, 1, 1)


        self.gridLayout_11.addWidget(self.widget_2, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.splitter_2.addWidget(self.tabWidget)
        self.tabWidget_2 = QTabWidget(self.splitter_2)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_3 = QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tableView = QTableView(self.tab_3)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout_3.addWidget(self.tableView, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_9 = QGridLayout(self.tab_4)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.plainTextEdit_3 = QPlainTextEdit(self.tab_4)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")

        self.gridLayout_9.addWidget(self.plainTextEdit_3, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_8 = QGridLayout(self.tab_5)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.plainTextEdit_4 = QPlainTextEdit(self.tab_5)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")

        self.gridLayout_8.addWidget(self.plainTextEdit_4, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget_2.addTab(self.tab_2, "")
        self.splitter_2.addWidget(self.tabWidget_2)
        self.splitter_3.addWidget(self.splitter_2)

        self.gridLayout_12.addWidget(self.splitter_3, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1169, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        self.menuWindow = QMenu(self.menubar)
        self.menuWindow.setObjectName(u"menuWindow")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuAction = QMenu(self.menubar)
        self.menuAction.setObjectName(u"menuAction")
        MainWindow.setMenuBar(self.menubar)
        QWidget.setTabOrder(self.tabWidget, self.pushButton_4)
        QWidget.setTabOrder(self.pushButton_4, self.pushButton_5)
        QWidget.setTabOrder(self.pushButton_5, self.pushButton_6)
        QWidget.setTabOrder(self.pushButton_6, self.tabWidget_2)
        QWidget.setTabOrder(self.tabWidget_2, self.plainTextEdit)
        QWidget.setTabOrder(self.plainTextEdit, self.tableView)
        QWidget.setTabOrder(self.tableView, self.plainTextEdit_3)
        QWidget.setTabOrder(self.plainTextEdit_3, self.plainTextEdit_4)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuAction.menuAction())
        self.menuFile.addAction(self.actionsave)
        self.menuFile.addAction(self.actionsave_as)
        self.menuFile.addAction(self.actionopen)
        self.menuEdit.addAction(self.actionredo)
        self.menuEdit.addAction(self.actionundo)
        self.menuEdit.addAction(self.actioncut)
        self.menuTools.addAction(self.actionquery_tool)
        self.menuWindow.addAction(self.actionminimize)
        self.menuWindow.addAction(self.actionmaximize)
        self.menuAction.addAction(self.actionclose)

        self.retranslateUi(MainWindow)
        self.tabWidget.tabCloseRequested.connect(self.tabWidget.repaint)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionsave.setText(QCoreApplication.translate("MainWindow", u"save", None))
        self.actionsave_as.setText(QCoreApplication.translate("MainWindow", u"save as", None))
        self.actionopen.setText(QCoreApplication.translate("MainWindow", u"open", None))
        self.actionredo.setText(QCoreApplication.translate("MainWindow", u"redo", None))
        self.actionundo.setText(QCoreApplication.translate("MainWindow", u"undo", None))
        self.actioncut.setText(QCoreApplication.translate("MainWindow", u"cut", None))
        self.actionminimize.setText(QCoreApplication.translate("MainWindow", u"minimize", None))
        self.actionmaximize.setText(QCoreApplication.translate("MainWindow", u"maximize", None))
        self.actionquery_tool.setText(QCoreApplication.translate("MainWindow", u"query_tool", None))
        self.actionclose.setText(QCoreApplication.translate("MainWindow", u"close", None))
        self.lineEdit.setPlaceholderText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Object_Explorer", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"new", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Query_Editor", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Query_Details", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Copy to Editor", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Remove all", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"History", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"sqlite", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"postgres", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"oracle", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"db", None))

        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"save", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"open_file", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"Explain Analyze", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"new_worksheet", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"cancel", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"execute", None))
        self.toolButton_3.setText(QCoreApplication.translate("MainWindow", u"Limit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"worksheet1", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Output", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Message", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Notification", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Processes", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.menuWindow.setTitle(QCoreApplication.translate("MainWindow", u"Window", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuAction.setTitle(QCoreApplication.translate("MainWindow", u"Action", None))
    # retranslateUi

