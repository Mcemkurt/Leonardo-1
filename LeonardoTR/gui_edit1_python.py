# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/ARGE/PycharmProjects/pythonProject3/gui_edit1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from leonardo_window import Ui_Leonardo



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #Ui
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.horizontalLayout.addWidget(self.treeWidget)
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.horizontalLayout.addWidget(self.verticalScrollBar)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.verticalLayout.addWidget(self.tabWidget)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setLineWidth(1)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 5)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 492, 22))
        self.menubar.setObjectName("menubar")
        self.menuDosya = QtWidgets.QMenu(self.menubar)
        self.menuDosya.setObjectName("menuDosya")
        self.menuD_zenle = QtWidgets.QMenu(self.menubar)
        self.menuD_zenle.setObjectName("menuD_zenle")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionLEONARDO = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/leonardo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLEONARDO.setIcon(icon)
        self.actionLEONARDO.setObjectName("actionLEONARDO")
        self.menubar.addAction(self.menuDosya.menuAction())
        self.menubar.addAction(self.menuD_zenle.menuAction())
        self.toolBar.addAction(self.actionLEONARDO)
        self.toolBar.addSeparator()
        #Uİ


        self.retranslateUi(MainWindow)

        self.tabWidget.tabCloseRequested.connect(self.removeTabs)   #Tab Closing
        self.treeWidget.doubleClicked.connect(self.addTabs)         #Tab Adding
        self.actionLEONARDO.triggered.connect(self.leonardoWindow)  #Leonardo Logo New Window

        self.leonardo_window = Ui_Leonardo()

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Leonardo", "Leonardo"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "New Column"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "New Subitem"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "New Subitem"))
        self.treeWidget.topLevelItem(1).child(0).child(0).setText(0, _translate("MainWindow", "New Subitem"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("MainWindow", "Canlı Destek"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.menuDosya.setTitle(_translate("MainWindow", "Dosya"))
        self.menuD_zenle.setTitle(_translate("MainWindow", "Düzenle"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionLEONARDO.setText(_translate("MainWindow", ""))
        self.actionLEONARDO.setToolTip(_translate("MainWindow", "https://leonardocompany.com.tr/tr/"))

    def removeTabs(self,index):
        self.tabWidget.removeTab(index)

    def addTabs(self):
        have_child = self.treeWidget.currentItem().childCount()
        print("Debug")

        if(have_child == 0):
           self.tabWidget.addTab(QtWidgets.QWidget(),"Tab"+ str(self.tabWidget.count()+1),)
        else:
            pass

    def leonardoWindow(self):
        self.leonardo_window.show()

import icons_py
