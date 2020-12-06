import sys
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
# sjw
from selectDataBase import selectCompanyStatus
# cr
from selectDataBase import search_Basic_assets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1331, 800)
        MainWindow.setMinimumSize(QSize(1280, 800))
        self.saveActive = QAction(MainWindow)
        self.saveActive.setObjectName(u"saveActive")
        self.chartAction = QAction(MainWindow)
        self.chartAction.setObjectName(u"chartAction")
        self.actionspecification = QAction(MainWindow)
        self.actionspecification.setObjectName(u"actionspecification")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.optionalTree = QTreeWidget(self.centralwidget)

        self.optionalTree.setObjectName(u"optionalTree")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.optionalTree.sizePolicy().hasHeightForWidth())
        self.optionalTree.setSizePolicy(sizePolicy)
        self.optionalTree.setMinimumSize(QSize(291, 0))
        self.optionalTree.setMaximumSize(QSize(1000000, 500))
        self.optionalTree.setSizeIncrement(QSize(989, 1000))

        self.verticalLayout.addWidget(self.optionalTree)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.label)

        self.runningLogText = QTextBrowser(self.centralwidget)
        self.runningLogText.setObjectName(u"runningLogText")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.runningLogText.sizePolicy().hasHeightForWidth())
        self.runningLogText.setSizePolicy(sizePolicy2)
        self.runningLogText.setMinimumSize(QSize(256, 192))

        self.verticalLayout.addWidget(self.runningLogText)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout_4.addWidget(self.radioButton)

        self.radioButton_4 = QRadioButton(self.centralwidget)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.horizontalLayout_4.addWidget(self.radioButton_4)

        self.radioButton_3 = QRadioButton(self.centralwidget)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout_4.addWidget(self.radioButton_3)

        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_4.addWidget(self.radioButton_2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        #   ！！！！！！！！！！！！！！！！！！！
        # 布局
        self.msgTable = QTableWidget(self.centralwidget)

        result = search_Basic_assets.search_Basis_assets(1, [2018, 2019])
        self.tableMsg(result);

        self.verticalLayout_2.addWidget(self.msgTable)
        # --------------------- table end --------------------------------------------

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        font1 = QFont()
        font1.setPointSize(12)
        self.progressBar.setFont(font1)
        self.progressBar.setValue(24)

        self.gridLayout.addWidget(self.progressBar, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1331, 22))
        self.menuactive = QMenu(self.menubar)
        self.menuactive.setObjectName(u"menuactive")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuactive.menuAction())
        self.menuactive.addAction(self.chartAction)
        self.menuactive.addSeparator()
        self.menuactive.addAction(self.actionspecification)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # 入参格式 ：二维数组
    # 表格构建
    def tableMsg(self, result):
        # 7788参数
        self.msgTable.setObjectName(u"msgTable")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.msgTable.sizePolicy().hasHeightForWidth())
        self.msgTable.setSizePolicy(sizePolicy3)
        self.msgTable.setMinimumSize(QSize(1000, 500))
        self.msgTable.setMaximumSize(QSize(10000000, 16777215))
        self.msgTable.setStyleSheet(u"")

        # 接口 search_Basis_assets
        if not result is None:
            columnFirstCount = len(result[0])
        else:
            print("结果集为空")
        rowCount = len(result)
        print(columnFirstCount)
        self.msgTable.setColumnCount(columnFirstCount)
        self.msgTable.setRowCount(rowCount)
        for i in range(columnFirstCount):
            __qtablewidgetitem = QTableWidgetItem()
            self.msgTable.setHorizontalHeaderItem(i, __qtablewidgetitem)
            ___qtablewidgetitem = self.msgTable.horizontalHeaderItem(i)
            ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", "指标", None));
        # row
        rowCountRange = int(columnFirstCount + 1)
        for row in range(rowCount):
            print(row)

            __qtablewidgetitem5 = QTableWidgetItem()
            self.msgTable.setVerticalHeaderItem(row, __qtablewidgetitem5)
            ___qtablewidgetitem4 = self.msgTable.verticalHeaderItem(row)
            ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", str(row), None));

            columnRange = int(columnFirstCount)
            for column in range(columnRange):
                print(column)
                msg = str(result[row][column])
                print(msg)
                newItem = QTableWidgetItem(msg)
                self.msgTable.setItem(row, column, newItem)

    def choosenTree(self):
        # tree
        font = QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setFont(0, font);
        self.optionalTree.setHeaderItem(__qtreewidgetitem)

        # 个数
        # 公司 - 年份 - 状态
        messages = selectCompanyStatus.select_all_company_and_status()
        # 每个公司信息
        for i in range(len(messages)):
            subMessage = messages[i]
            # 主键 and 公司名
            companyName = subMessage[0]
            __qtreewidgetitem1 = QTreeWidgetItem(self.optionalTree)
            ___qtreewidgetitem1 = self.optionalTree.topLevelItem(i)
            ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", companyName[1], None));

            for j in range(1, 4):
                yearAndStatus = subMessage[j]
                year = yearAndStatus[0]
                status1 = yearAndStatus[1]
                status2 = yearAndStatus[2]
                status3 = yearAndStatus[3]
                status4 = yearAndStatus[4]
                QTreeWidgetItem(__qtreewidgetitem1)
                ___qtreewidgetitem2 = ___qtreewidgetitem1.child(j - 1)
                ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", str(year), None));
                # ___qtreewidgetitem3 = ___qtreewidgetitem1.child(1)
                # ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"table1_2", None));

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.saveActive.setText(QCoreApplication.translate("MainWindow", u"save", None))
        self.chartAction.setText(QCoreApplication.translate("MainWindow", u"chart", None))
        self.actionspecification.setText(QCoreApplication.translate("MainWindow", u"specification", None))
        ___qtreewidgetitem = self.optionalTree.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"chosen tree", None));

        __sortingEnabled = self.optionalTree.isSortingEnabled()
        self.optionalTree.setSortingEnabled(False)
        self.choosenTree()

        # 四张表状态

        self.optionalTree.setSortingEnabled(__sortingEnabled)

        self.label.setText(QCoreApplication.translate("MainWindow", u" running log", None))
        self.runningLogText.setHtml(QCoreApplication.translate("MainWindow",
                                                               u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                               "p, li { white-space: pre-wrap; }\n"
                                                               "</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">running log</p>\n"
                                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">running log</p>\n"
                                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">running log</p>\n"
                                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">running log</p>\n"
                                                               "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-bloc"
                                                               "k-indent:0; text-indent:0px; font-family:'SimSun'; font-size:9pt;\"><br /></p>\n"
                                                               "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'SimSun'; font-size:9pt;\"><br /></p>\n"
                                                               "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>",
                                                               None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u57fa\u7840\u8d44\u4ea7\u8868", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"\u57fa\u7840\u9650\u5b9a\u8868", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"\u57fa\u7840\u5229\u6da6\u8868", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u8f85\u52a9\u6570\u636e\u8868", None))
        # ___qtablewidgetitem = self.msgTable.horizontalHeaderItem(0)
        # ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"2016", None));
        # ___qtablewidgetitem1 = self.msgTable.horizontalHeaderItem(1)
        # ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"2017", None));
        # ___qtablewidgetitem2 = self.msgTable.horizontalHeaderItem(2)
        # ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2018", None));
        # ___qtablewidgetitem3 = self.msgTable.horizontalHeaderItem(3)
        # ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"2019", None));
        # ___qtablewidgetitem8 = self.msgTable.horizontalHeaderItem(4)
        # ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"2019", None));
        # ___qtablewidgetitem9 = self.msgTable.horizontalHeaderItem(5)
        # ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"2019", None));

        # ___qtablewidgetitem4 = self.msgTable.verticalHeaderItem(0)
        # ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"row1", None));
        # ___qtablewidgetitem5 = self.msgTable.verticalHeaderItem(1)
        # ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"row2", None));
        # ___qtablewidgetitem6 = self.msgTable.verticalHeaderItem(2)
        # ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"row3", None));
        # ___qtablewidgetitem7 = self.msgTable.verticalHeaderItem(3)
        # ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"row4", None));

        self.menuactive.setTitle(QCoreApplication.translate("MainWindow", u"active", None))
    # retranslateUi


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
