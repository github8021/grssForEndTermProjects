import sys
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
# sjw
from selectDataBase import selectCompanyStatus, search_Basis_cash, search_Basis_profit
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

        result = search_Basic_assets.search_Basis_assets(1, [2018, 2019])
        print(result)
        # tup1 = (('physics', 'chemistry', 1997, 2000), ('physics', 'chemistry', 1997, 2000));
        self.tableMsg(result, "基础资产表");

        self.verticalLayout_2.addWidget(self.msgTable)
        # --------------------- table end --------------------------------------------

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

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
    def tableMsg(self, result, runningLog):
        # 进度条

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        font1 = QFont()
        font1.setPointSize(12)
        self.progressBar.setFont(font1)
        # for Percent in range(100 + 1):  # 从0计数到100
        #     self.progressBar.setValue(Percent)  # 设置当前进度值
        #     time.sleep(0.05)
        # 进度条

        self.gridLayout.addWidget(self.progressBar, 1, 0, 1, 1)
        self.runningLogText.append(runningLog + "- 开始查询")
        # 7788参数
        self.msgTable = QTableWidget(self.centralwidget)
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
            rowCount = len(result)
        else:
            print("结果集为空")
            return
        columnFirstCount = len(result[0])

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
            __qtablewidgetitem5 = QTableWidgetItem()
            self.msgTable.setVerticalHeaderItem(row, __qtablewidgetitem5)
            ___qtablewidgetitem4 = self.msgTable.verticalHeaderItem(row)
            ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", str(row), None));

            columnRange = int(columnFirstCount)
            for column in range(columnRange):
                msg = str(result[row][column])
                newItem = QTableWidgetItem(msg)
                self.msgTable.setItem(row, column, newItem)
        # warning log
        self.runningLogText.append(runningLog + "- 查询成功 ")
        self.progressBar.setValue(100)
        self.progressBar.reset()

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

            for j in range(1, len(subMessage)):
                yearAndStatus = subMessage[j]
                year = yearAndStatus[0]
                status1 = yearAndStatus[1]
                status2 = yearAndStatus[2]
                status3 = yearAndStatus[3]
                status4 = yearAndStatus[4]
                QTreeWidgetItem(__qtreewidgetitem1)
                ___qtreewidgetitem2 = ___qtreewidgetitem1.child(j - 1)
                ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", str(year), None));

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

        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u57fa\u7840\u8d44\u4ea7\u8868", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"\u57fa\u7840\u9650\u5b9a\u8868", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"\u57fa\u7840\u5229\u6da6\u8868", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u8f85\u52a9\u6570\u636e\u8868", None))

        self.menuactive.setTitle(QCoreApplication.translate("MainWindow", u"active", None))

        # radioButton
        self.ButtonGroup = QButtonGroup()
        self.ButtonGroup.addButton(self.radioButton_4)
        self.ButtonGroup.addButton(self.radioButton_2)
        self.ButtonGroup.addButton(self.radioButton_3)
        self.ButtonGroup.addButton(self.radioButton)

        # 监听事件
        self.ButtonGroup.buttonClicked.connect(self.PressButton)
        # self.optionalTree.connect(self, SIGNAL('itemClicked(QTreeWidgetItem*, int)'), self.onClick)

        self.optionalTree.itemClicked.connect(self.PressItem)

    def PressButton(self):
        tableName = self.ButtonGroup.checkedButton().text()
        if tableName == '基础资产表':
            self.msgTable.close()
            result = search_Basic_assets.search_Basis_assets(1, [2018])
            self.tableMsg(result, "基础资产表");
            self.verticalLayout_2.addWidget(self.msgTable)
        if tableName == '基础限定表':
            self.msgTable.close()
            result = search_Basis_cash.search_Basic_cash(1, [2018, 2019])
            self.tableMsg(result, "基础限定表");
            self.verticalLayout_2.addWidget(self.msgTable)

        if tableName == '基础利润表':
            self.msgTable.close()
            result2 = search_Basis_profit.search_Basic_profit(1, [2018, 2019])
            print(result2)
            self.tableMsg(result2, "基础利润表");
            self.verticalLayout_2.addWidget(self.msgTable)
        if tableName == '辅助数据表':
            print("123")

    def PressItem(self, item, column):
        # print(column)
        # print(self.optionalTree.parent())
        print(item.text(0))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
