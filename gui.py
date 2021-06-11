
from PyQt6 import QtCore, QtGui, QtWidgets
import database as db


class Ui_HotelReserve(object):
    def setupUi(self, HotelReserve):
        HotelReserve.setObjectName("HotelReserve")
        HotelReserve.resize(1122, 881)
        self.centralwidget = QtWidgets.QWidget(HotelReserve)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)
        self.AllWindows = QtWidgets.QTabWidget(self.centralwidget)
        self.AllWindows.setTabBarAutoHide(False)
        self.AllWindows.setObjectName("AllWindows")
        self.Reserve = QtWidgets.QWidget()
        self.Reserve.setObjectName("Reserve")
        self.dateEdit = QtWidgets.QDateEdit(self.Reserve)
        self.dateEdit.setGeometry(QtCore.QRect(0, 180, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")
        self.lineEdit = QtWidgets.QLineEdit(self.Reserve)
        self.lineEdit.setGeometry(QtCore.QRect(0, 70, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.textBrowser = QtWidgets.QTextBrowser(self.Reserve)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 381, 71))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.Reserve)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 110, 381, 71))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.Reserve)
        self.textBrowser_3.setGeometry(QtCore.QRect(0, 350, 381, 71))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.Reserve)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 420, 381, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.Reserve)
        self.textBrowser_4.setGeometry(QtCore.QRect(0, 240, 381, 71))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.Reserve)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 310, 381, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.spinBox = QtWidgets.QSpinBox(self.Reserve)
        self.spinBox.setGeometry(QtCore.QRect(30, 580, 121, 31))
        self.spinBox.setMinimum(0)
        self.spinBox.setMaximum(999)
        self.spinBox.setObjectName("spinBox")
        self.label_6 = QtWidgets.QLabel(self.Reserve)
        self.label_6.setGeometry(QtCore.QRect(40, 540, 91, 21))
        self.label_6.setObjectName("label_6")
        self.pushButton_11 = QtWidgets.QPushButton(self.Reserve)
        self.pushButton_11.setGeometry(QtCore.QRect(40, 640, 261, 41))
        self.pushButton_11.setObjectName("pushButton_11")
        self.spinBox_8 = QtWidgets.QSpinBox(self.Reserve)
        self.spinBox_8.setGeometry(QtCore.QRect(180, 580, 121, 31))
        self.spinBox_8.setMaximum(9999)
        self.spinBox_8.setObjectName("spinBox_8")
        self.label_26 = QtWidgets.QLabel(self.Reserve)
        self.label_26.setGeometry(QtCore.QRect(180, 540, 91, 16))
        self.label_26.setObjectName("label_26")
        self.tableWidget = QtWidgets.QTableWidget(self.Reserve)
        self.tableWidget.setGeometry(QtCore.QRect(430, 10, 611, 741))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.AllWindows.addTab(self.Reserve, "")
        self.Dnunbers = QtWidgets.QWidget()
        self.Dnunbers.setObjectName("Dnunbers")
        self.pushButton_6 = QtWidgets.QPushButton(self.Dnunbers)
        self.pushButton_6.setGeometry(QtCore.QRect(910, 0, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.Dnunbers)
        self.tableWidget_2.setGeometry(QtCore.QRect(20, 20, 871, 741))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.AllWindows.addTab(self.Dnunbers, "")
        self.AllNum = QtWidgets.QWidget()
        self.AllNum.setObjectName("AllNum")
        self.pushButton_5 = QtWidgets.QPushButton(self.AllNum)
        self.pushButton_5.setGeometry(QtCore.QRect(820, 30, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.AllNum)
        self.lineEdit_10.setGeometry(QtCore.QRect(840, 340, 181, 21))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.AllNum)
        self.lineEdit_12.setGeometry(QtCore.QRect(840, 380, 181, 21))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.AllNum)
        self.lineEdit_14.setGeometry(QtCore.QRect(840, 450, 181, 21))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.spinBox_2 = QtWidgets.QSpinBox(self.AllNum)
        self.spinBox_2.setGeometry(QtCore.QRect(840, 300, 42, 22))
        self.spinBox_2.setMaximum(9999)
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_7 = QtWidgets.QLabel(self.AllNum)
        self.label_7.setGeometry(QtCore.QRect(840, 240, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Mistral")
        font.setPointSize(24)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.radioButton = QtWidgets.QRadioButton(self.AllNum)
        self.radioButton.setGeometry(QtCore.QRect(840, 420, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.pushButton_12 = QtWidgets.QPushButton(self.AllNum)
        self.pushButton_12.setGeometry(QtCore.QRect(840, 490, 181, 41))
        self.pushButton_12.setObjectName("pushButton_12")
        self.label_8 = QtWidgets.QLabel(self.AllNum)
        self.label_8.setGeometry(QtCore.QRect(900, 300, 71, 21))
        self.label_8.setObjectName("label_8")
        self.label_20 = QtWidgets.QLabel(self.AllNum)
        self.label_20.setGeometry(QtCore.QRect(610, 250, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Mistral")
        font.setPointSize(23)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.spinBox_6 = QtWidgets.QSpinBox(self.AllNum)
        self.spinBox_6.setGeometry(QtCore.QRect(610, 450, 42, 22))
        self.spinBox_6.setMaximum(9999)
        self.spinBox_6.setObjectName("spinBox_6")
        self.label_21 = QtWidgets.QLabel(self.AllNum)
        self.label_21.setGeometry(QtCore.QRect(660, 450, 71, 21))
        self.label_21.setObjectName("label_21")
        self.pushButton_19 = QtWidgets.QPushButton(self.AllNum)
        self.pushButton_19.setGeometry(QtCore.QRect(610, 490, 191, 41))
        self.pushButton_19.setObjectName("pushButton_19")
        self.label_22 = QtWidgets.QLabel(self.AllNum)
        self.label_22.setGeometry(QtCore.QRect(660, 280, 81, 16))
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.AllNum)
        self.tableWidget_3.setGeometry(QtCore.QRect(20, 20, 581, 741))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.line = QtWidgets.QFrame(self.AllNum)
        self.line.setGeometry(QtCore.QRect(810, 250, 20, 281))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.AllWindows.addTab(self.AllNum, "")
        self.People = QtWidgets.QWidget()
        self.People.setObjectName("People")
        self.pushButton_4 = QtWidgets.QPushButton(self.People)
        self.pushButton_4.setGeometry(QtCore.QRect(910, 0, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.spinBox_3 = QtWidgets.QSpinBox(self.People)
        self.spinBox_3.setGeometry(QtCore.QRect(860, 310, 42, 22))
        self.spinBox_3.setObjectName("spinBox_3")
        self.label_11 = QtWidgets.QLabel(self.People)
        self.label_11.setGeometry(QtCore.QRect(910, 310, 71, 21))
        self.label_11.setObjectName("label_11")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.People)
        self.lineEdit_13.setGeometry(QtCore.QRect(860, 350, 113, 20))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.People)
        self.lineEdit_15.setGeometry(QtCore.QRect(860, 390, 113, 20))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.People)
        self.lineEdit_16.setGeometry(QtCore.QRect(860, 430, 113, 20))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.People)
        self.lineEdit_17.setGeometry(QtCore.QRect(860, 470, 113, 20))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.People)
        self.lineEdit_18.setGeometry(QtCore.QRect(860, 510, 113, 20))
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.pushButton_15 = QtWidgets.QPushButton(self.People)
        self.pushButton_15.setGeometry(QtCore.QRect(850, 540, 181, 41))
        self.pushButton_15.setObjectName("pushButton_15")
        self.spinBox_5 = QtWidgets.QSpinBox(self.People)
        self.spinBox_5.setGeometry(QtCore.QRect(600, 490, 42, 22))
        self.spinBox_5.setMaximum(999)
        self.spinBox_5.setObjectName("spinBox_5")
        self.label_18 = QtWidgets.QLabel(self.People)
        self.label_18.setGeometry(QtCore.QRect(660, 490, 71, 21))
        self.label_18.setObjectName("label_18")
        self.pushButton_18 = QtWidgets.QPushButton(self.People)
        self.pushButton_18.setGeometry(QtCore.QRect(600, 540, 201, 41))
        self.pushButton_18.setObjectName("pushButton_18")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.People)
        self.tableWidget_4.setGeometry(QtCore.QRect(10, 10, 571, 751))
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(0)
        self.tableWidget_4.setRowCount(0)
        self.label_10 = QtWidgets.QLabel(self.People)
        self.label_10.setGeometry(QtCore.QRect(860, 240, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Mistral")
        font.setPointSize(24)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_27 = QtWidgets.QLabel(self.People)
        self.label_27.setGeometry(QtCore.QRect(610, 250, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Mistral")
        font.setPointSize(23)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.line_2 = QtWidgets.QFrame(self.People)
        self.line_2.setGeometry(QtCore.QRect(820, 250, 20, 341))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.AllWindows.addTab(self.People, "")
        self.AllReserves = QtWidgets.QWidget()
        self.AllReserves.setObjectName("AllReserves")
        self.pushButton_3 = QtWidgets.QPushButton(self.AllReserves)
        self.pushButton_3.setGeometry(QtCore.QRect(910, 0, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4 = QtWidgets.QLabel(self.AllReserves)
        self.label_4.setGeometry(QtCore.QRect(30, 40, 601, 721))
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading |
                                  QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_4.setObjectName("label_4")
        self.spinBox_4 = QtWidgets.QSpinBox(self.AllReserves)
        self.spinBox_4.setGeometry(QtCore.QRect(870, 350, 42, 22))
        self.spinBox_4.setObjectName("spinBox_4")
        self.label_14 = QtWidgets.QLabel(self.AllReserves)
        self.label_14.setGeometry(QtCore.QRect(930, 350, 111, 21))
        self.label_14.setObjectName("label_14")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.AllReserves)
        self.lineEdit_19.setGeometry(QtCore.QRect(870, 380, 151, 21))
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.AllReserves)
        self.lineEdit_20.setGeometry(QtCore.QRect(870, 410, 151, 20))
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.AllReserves)
        self.lineEdit_22.setGeometry(QtCore.QRect(870, 470, 151, 20))
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.AllReserves)
        self.dateEdit_2.setGeometry(QtCore.QRect(870, 440, 151, 22))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.pushButton_17 = QtWidgets.QPushButton(self.AllReserves)
        self.pushButton_17.setGeometry(QtCore.QRect(870, 500, 181, 41))
        self.pushButton_17.setObjectName("pushButton_17")
        self.label_16 = QtWidgets.QLabel(self.AllReserves)
        self.label_16.setGeometry(QtCore.QRect(870, 680, 131, 16))
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.spinBox_7 = QtWidgets.QSpinBox(self.AllReserves)
        self.spinBox_7.setGeometry(QtCore.QRect(650, 460, 42, 22))
        self.spinBox_7.setObjectName("spinBox_7")
        self.label_24 = QtWidgets.QLabel(self.AllReserves)
        self.label_24.setGeometry(QtCore.QRect(720, 460, 101, 21))
        self.label_24.setObjectName("label_24")
        self.pushButton_20 = QtWidgets.QPushButton(self.AllReserves)
        self.pushButton_20.setGeometry(QtCore.QRect(650, 500, 191, 41))
        self.pushButton_20.setObjectName("pushButton_20")
        self.label_25 = QtWidgets.QLabel(self.AllReserves)
        self.label_25.setGeometry(QtCore.QRect(690, 380, 91, 21))
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        self.tableWidget_5 = QtWidgets.QTableWidget(self.AllReserves)
        self.tableWidget_5.setGeometry(QtCore.QRect(20, 30, 611, 741))
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(0)
        self.tableWidget_5.setRowCount(0)
        self.line_3 = QtWidgets.QFrame(self.AllReserves)
        self.line_3.setGeometry(QtCore.QRect(850, 290, 20, 251))
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_28 = QtWidgets.QLabel(self.AllReserves)
        self.label_28.setGeometry(QtCore.QRect(650, 280, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Mistral")
        font.setPointSize(23)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.label_12 = QtWidgets.QLabel(self.AllReserves)
        self.label_12.setGeometry(QtCore.QRect(870, 280, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Mistral")
        font.setPointSize(24)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.AllWindows.addTab(self.AllReserves, "")
        self.DatabaseWork = QtWidgets.QWidget()
        self.DatabaseWork.setObjectName("DatabaseWork")
        self.pushButton = QtWidgets.QPushButton(self.DatabaseWork)
        self.pushButton.setGeometry(QtCore.QRect(650, 20, 381, 91))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.DatabaseWork)
        self.pushButton_2.setGeometry(QtCore.QRect(650, 130, 381, 91))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_8 = QtWidgets.QPushButton(self.DatabaseWork)
        self.pushButton_8.setGeometry(QtCore.QRect(70, 60, 311, 71))
        self.pushButton_8.setObjectName("pushButton_8")
        self.checkBox = QtWidgets.QCheckBox(self.DatabaseWork)
        self.checkBox.setGeometry(QtCore.QRect(90, 170, 70, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.DatabaseWork)
        self.checkBox_2.setGeometry(QtCore.QRect(180, 170, 70, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.DatabaseWork)
        self.checkBox_3.setGeometry(QtCore.QRect(270, 170, 91, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.DatabaseWork)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 420, 461, 351))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout.addWidget(self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout.addWidget(self.lineEdit_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout.addWidget(self.lineEdit_6)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout.addWidget(self.lineEdit_7)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.pushButton_9 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout.addWidget(self.pushButton_9)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.DatabaseWork)
        self.verticalLayoutWidget_2.setGeometry(
            QtCore.QRect(540, 420, 511, 351))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_2.addWidget(self.lineEdit_8)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_2.addWidget(self.lineEdit_9)
        self.checkBox_4 = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_2.addWidget(self.checkBox_4)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.verticalLayout_2.addWidget(self.lineEdit_11)
        self.pushButton_10 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_2.addWidget(self.pushButton_10)
        self.label_29 = QtWidgets.QLabel(self.DatabaseWork)
        self.label_29.setGeometry(QtCore.QRect(10, 300, 461, 101))
        font = QtGui.QFont()
        font.setFamily("Mistral")
        font.setPointSize(44)
        self.label_29.setFont(font)
        self.label_29.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.DatabaseWork)
        self.label_30.setGeometry(QtCore.QRect(540, 300, 511, 101))
        font = QtGui.QFont()
        font.setFamily("Mistral")
        font.setPointSize(46)
        self.label_30.setFont(font)
        self.label_30.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.AllWindows.addTab(self.DatabaseWork, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_21.setGeometry(QtCore.QRect(30, 80, 241, 41))
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(30, 20, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_13 = QtWidgets.QPushButton(self.tab)
        self.pushButton_13.setGeometry(QtCore.QRect(30, 140, 241, 51))
        self.pushButton_13.setObjectName("pushButton_13")
        self.tableWidget_6 = QtWidgets.QTableWidget(self.tab)
        self.tableWidget_6.setGeometry(QtCore.QRect(380, 40, 681, 711))
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.setColumnCount(0)
        self.tableWidget_6.setRowCount(0)
        self.lineEdit_23 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_23.setGeometry(QtCore.QRect(30, 440, 241, 41))
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(30, 380, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_14 = QtWidgets.QPushButton(self.tab)
        self.pushButton_14.setGeometry(QtCore.QRect(30, 500, 241, 51))
        self.pushButton_14.setObjectName("pushButton_14")
        self.AllWindows.addTab(self.tab, "")
        self.gridLayout.addWidget(self.AllWindows, 0, 0, 1, 1)
        HotelReserve.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(HotelReserve)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1122, 21))
        self.menubar.setObjectName("menubar")
        HotelReserve.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(HotelReserve)
        self.statusbar.setObjectName("statusbar")
        HotelReserve.setStatusBar(self.statusbar)
        self.actionCheckAprNumbers = QtGui.QAction(HotelReserve)
        self.actionCheckAprNumbers.setObjectName("actionCheckAprNumbers")

        self.retranslateUi(HotelReserve)
        self.AllWindows.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(HotelReserve)

    def retranslateUi(self, HotelReserve):
        _translate = QtCore.QCoreApplication.translate
        HotelReserve.setWindowTitle(_translate("HotelReserve", "MainWindow"))
        self.textBrowser.setHtml(_translate("HotelReserve", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Введите, пожалуйста, количество людей для брони.</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("HotelReserve", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Введите, пожалуйста, время для брони.</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("HotelReserve", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">После ввода, нажмите кнопку &quot;Показать доступные номера&quot;.</span></p></body></html>"))
        self.pushButton_7.setText(_translate(
            "HotelReserve", "Показать доступные номера."))
        self.textBrowser_4.setHtml(_translate("HotelReserve", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Введите, пожалуйста, количество дней отдыха.</span></p></body></html>"))
        self.label_6.setText(_translate("HotelReserve", "id человека"))
        self.pushButton_11.setText(_translate(
            "HotelReserve", "Создать резервацию"))
        self.label_26.setText(_translate("HotelReserve", "id номера"))
        self.AllWindows.setTabText(self.AllWindows.indexOf(
            self.Reserve), _translate("HotelReserve", "Резерв"))
        self.pushButton_6.setText(_translate("HotelReserve", "Refresh"))
        self.AllWindows.setTabText(self.AllWindows.indexOf(
            self.Dnunbers), _translate("HotelReserve", "Доступные номера"))
        self.pushButton_5.setText(_translate("HotelReserve", "Refresh"))
        self.lineEdit_10.setText(_translate("HotelReserve", "floor"))
        self.lineEdit_12.setText(_translate("HotelReserve", "Number of beds"))
        self.lineEdit_14.setText(_translate("HotelReserve", "Price"))
        self.label_7.setText(_translate("HotelReserve", "Изменить запись"))
        self.radioButton.setText(_translate("HotelReserve", "Sea view"))
        self.pushButton_12.setText(_translate("HotelReserve", "Edit"))
        self.label_8.setText(_translate("HotelReserve", "Id of number"))
        self.label_20.setText(_translate("HotelReserve", "Удалить запись"))
        self.label_21.setText(_translate("HotelReserve", "Id of number"))
        self.pushButton_19.setText(_translate("HotelReserve", "Delete"))
        self.AllWindows.setTabText(self.AllWindows.indexOf(
            self.AllNum), _translate("HotelReserve", "Все номера"))
        self.pushButton_4.setText(_translate("HotelReserve", "Refresh"))
        self.label_11.setText(_translate("HotelReserve", "Id of human"))
        self.lineEdit_13.setText(_translate("HotelReserve", "FirstName"))
        self.lineEdit_15.setText(_translate("HotelReserve", "lastname"))
        self.lineEdit_16.setText(_translate("HotelReserve", "age"))
        self.lineEdit_17.setText(_translate("HotelReserve", "Phone number"))
        self.lineEdit_18.setText(_translate("HotelReserve", "email"))
        self.pushButton_15.setText(_translate("HotelReserve", "Edit"))
        self.label_18.setText(_translate("HotelReserve", "Id of human"))
        self.pushButton_18.setText(_translate("HotelReserve", "Delete"))
        self.label_10.setText(_translate("HotelReserve", "Изменить запись"))
        self.label_27.setText(_translate("HotelReserve", "Удалить запись"))
        self.AllWindows.setTabText(self.AllWindows.indexOf(
            self.People), _translate("HotelReserve", "Люди"))
        self.pushButton_3.setText(_translate("HotelReserve", "Refresh"))
        self.label_14.setText(_translate("HotelReserve", "Id of reservation"))
        self.lineEdit_19.setText(_translate("HotelReserve", "human_id"))
        self.lineEdit_20.setText(_translate("HotelReserve", "number_id"))
        self.lineEdit_22.setText(_translate("HotelReserve", "number of days"))
        self.pushButton_17.setText(_translate("HotelReserve", "Edit"))
        self.label_24.setText(_translate("HotelReserve", "Id of reservation"))
        self.pushButton_20.setText(_translate("HotelReserve", "Delete"))
        self.label_28.setText(_translate("HotelReserve", "Удалить запись"))
        self.label_12.setText(_translate("HotelReserve", "Изменить запись"))
        self.AllWindows.setTabText(self.AllWindows.indexOf(
            self.AllReserves), _translate("HotelReserve", "Все резервы"))
        self.pushButton.setText(_translate("HotelReserve", "Create database"))
        self.pushButton_2.setText(_translate(
            "HotelReserve", "Delete database"))
        self.pushButton_8.setText(_translate(
            "HotelReserve", "Очистить выбранные таблицы"))
        self.checkBox.setText(_translate("HotelReserve", "people"))
        self.checkBox_2.setText(_translate("HotelReserve", "numbers"))
        self.checkBox_3.setText(_translate("HotelReserve", "reservations"))
        self.lineEdit_4.setText(_translate("HotelReserve", "Name"))
        self.lineEdit_5.setText(_translate("HotelReserve", "Surname"))
        self.lineEdit_6.setText(_translate("HotelReserve", "Age"))
        self.lineEdit_7.setText(_translate("HotelReserve", "Phone number"))
        self.lineEdit_3.setText(_translate("HotelReserve", "email"))
        self.pushButton_9.setText(_translate(
            "HotelReserve", "Добавить нового клиента"))
        self.lineEdit_8.setText(_translate("HotelReserve", "Этаж"))
        self.lineEdit_9.setText(_translate("HotelReserve", "Кол-во кроватей"))
        self.checkBox_4.setText(_translate("HotelReserve", "Вид на море"))
        self.lineEdit_11.setText(_translate("HotelReserve", "Цена"))
        self.pushButton_10.setText(_translate(
            "HotelReserve", "Добавить новую комнату"))
        self.label_29.setText(_translate("HotelReserve", "Добавление клиента"))
        self.label_30.setText(_translate("HotelReserve", "Добавление комнаты"))
        self.AllWindows.setTabText(self.AllWindows.indexOf(
            self.DatabaseWork), _translate("HotelReserve", "Работа с базой данных"))
        self.lineEdit_21.setText(_translate("HotelReserve", "Введите фамилию"))
        self.label.setText(_translate(
            "HotelReserve", "Поиск человека по фамилии"))
        self.pushButton_13.setText(_translate("HotelReserve", "Найти"))
        self.lineEdit_23.setText(_translate("HotelReserve", "Введите фамилию"))
        self.label_2.setText(_translate(
            "HotelReserve", "Удаление человека по фамилии"))
        self.pushButton_14.setText(_translate("HotelReserve", "Удалить"))
        self.AllWindows.setTabText(self.AllWindows.indexOf(
            self.tab), _translate("HotelReserve", "Поиск/удаление людей"))
        self.actionCheckAprNumbers.setText(
            _translate("HotelReserve", "CheckAprNumbers"))

    def connect_funcs(self):
        self.pushButton_10.clicked.connect(lambda: db.add_number(self.lineEdit_8.text(
        ), self.lineEdit_9.text(), self.checkBox_4.isChecked(), self.lineEdit_11.text()))
        self.pushButton_9.clicked.connect(lambda: db.add_man(self.lineEdit_4.text(), self.lineEdit_5.text(
        ), self.lineEdit_6.text(), self.lineEdit_7.text(), self.lineEdit_3.text()))
        self.pushButton_8.clicked.connect(lambda: db.clear_tables(
            self.checkBox.isChecked(), self.checkBox_2.isChecked(), self.checkBox_3.isChecked()))
        self.pushButton.clicked.connect(db.create_database)
        self.pushButton_2.clicked.connect(db.drop_database)
        self.pushButton_3.clicked.connect(
            lambda: db.print_all_reservations(self))
        self.pushButton_4.clicked.connect(lambda: db.print_all_people(self))
        self.pushButton_5.clicked.connect(lambda: db.print_all_numbers(self))
        self.pushButton_6.clicked.connect(
            lambda: db.print_apr_numbers_for_all(self))
        self.pushButton_7.clicked.connect(lambda: db.print_apr_numbers_for_current_human(
            self, self.lineEdit.text(), self.dateEdit.date().toString('dd.MM.yyyy'), self.lineEdit_2.text()))
        self.pushButton_11.clicked.connect(lambda: db.add_reservation(self.spinBox.value(
        ), self.spinBox_8.value(), self.dateEdit.date().toString('dd.MM.yyyy'), self.lineEdit_2.text()))
        self.pushButton_17.clicked.connect(lambda: db.edit_reservations(self.spinBox_4.value(), self.lineEdit_19.text(
        ), self.lineEdit_20.text(), self.dateEdit_2.date().toString('dd.MM.yyyy'), self.lineEdit_22.text()))
        self.pushButton_15.clicked.connect(lambda: db.edit_people(self.spinBox_3.value(), self.lineEdit_13.text(
        ), self.lineEdit_15.text(), self.lineEdit_16.text(), self.lineEdit_17.text(), self.lineEdit_18.text()))
        self.pushButton_12.clicked.connect(lambda: db.edit_numbers(self.spinBox_2.value(), self.lineEdit_10.text(
        ), self.lineEdit_12.text(), self.radioButton.isChecked(), self.lineEdit_14.text()))
        self.pushButton_18.clicked.connect(
            lambda: db.delete_human(self.spinBox_5.value()))
        self.pushButton_20.clicked.connect(
            lambda: db.delete_reservation(self.spinBox_7.value()))
        self.pushButton_19.clicked.connect(
            lambda: db.delete_number(self.spinBox_6.value()))
        self.pushButton_13.clicked.connect(
            lambda: db.find_human_by_lastname(self, self.lineEdit_21.text()))
        self.pushButton_14.clicked.connect(
            lambda: db.delete_human_by_lastname(self.lineEdit_23.text()))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("Roflan application")
    HotelReserve = QtWidgets.QMainWindow()
    ui = Ui_HotelReserve()
    ui.setupUi(HotelReserve)
    ui.connect_funcs()
    HotelReserve.show()
    sys.exit(app.exec())