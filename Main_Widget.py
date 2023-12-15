import os
import sys
import os.path
from datetime import datetime

from PyQt6 import QtCore, QtGui, QtWidgets
import sqlite3

from pypdf import PdfMerger
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors

from ConfigBase_Widget import ConfigBaseWidget


class ZAVOD(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.count = 1

        self.list_products_init()
        self.NAME_INDEX = 1
        self.truba_names = {'Труба', 'труба', 'ТРУБА'}
        self.krug_names = {'Круг', 'круг', 'КРУГ'}
        self.delete_icon = QtGui.QIcon(r".\Src\delete.png")
        self.setWindowTitle("Гидравлика Трейд")
        self.setObjectName("MainWindow")
        self.resize(1479, 801)
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.font_rows = QtGui.QFont('Times New Roman', 14)
        self.frame_columns_names = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_columns_names.setMaximumSize(QtCore.QSize(16777215, 91))
        self.frame_columns_names.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_columns_names.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_columns_names.setObjectName("frame_columns_names")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_columns_names)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.frame_columns_names)
        self.label.setMinimumSize(QtCore.QSize(200, 0))
        self.label.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("‘Open Sans Condensed’,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.label.setFont(font)
        self.label.setAcceptDrops(True)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("color: #111;\n"
                                 "font-family: ‘Open Sans Condensed’, sans-serif;\n"
                                 "font-size: 14px;\n"
                                 "font-weight: 700;\n"
                                 "line-height: 64px;\n"
                                 "margin: 0 0 0;\n"
                                 "padding: 20px 30px;\n"
                                 "text-align: center;\n"
                                 "text-transform: uppercase;")
        self.label.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(parent=self.frame_columns_names)
        self.label_2.setMinimumSize(QtCore.QSize(150, 0))
        self.label_2.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("‘Open Sans Condensed’,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.label_2.setFont(font)
        self.label_2.setMouseTracking(False)
        self.label_2.setAcceptDrops(False)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("color: #111;\n"
                                   "font-family: ‘Open Sans Condensed’, sans-serif;\n"
                                   "font-size: 14px;\n"
                                   "font-weight: 700;\n"
                                   "line-height: 64px;\n"
                                   "margin: 0 0 0;\n"
                                   "padding: 20px 30px;\n"
                                   "text-align: center;\n"
                                   "text-transform: uppercase;")
        self.label_2.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setOpenExternalLinks(False)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.MinimumExpanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(parent=self.frame_columns_names)
        self.label_3.setMinimumSize(QtCore.QSize(150, 0))
        self.label_3.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("‘Open Sans Condensed’,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.label_3.setFont(font)
        self.label_3.setAcceptDrops(True)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("color: #111;\n"
                                   "font-family: ‘Open Sans Condensed’, sans-serif;\n"
                                   "font-size: 14px;\n"
                                   "font-weight: 700;\n"
                                   "line-height: 64px;\n"
                                   "margin: 0 0 0;\n"
                                   "padding: 20px 30px;\n"
                                   "text-align: center;\n"
                                   "text-transform: uppercase;")
        self.label_3.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setOpenExternalLinks(False)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.MinimumExpanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_4 = QtWidgets.QLabel(parent=self.frame_columns_names)
        self.label_4.setMinimumSize(QtCore.QSize(150, 0))
        self.label_4.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("‘Open Sans Condensed’,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.label_4.setFont(font)
        self.label_4.setAcceptDrops(True)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet("color: #111;\n"
                                   "font-family: ‘Open Sans Condensed’, sans-serif;\n"
                                   "font-size: 14px;\n"
                                   "font-weight: 700;\n"
                                   "line-height: 64px;\n"
                                   "margin: 0 0 0;\n"
                                   "padding: 20px 30px;\n"
                                   "text-align: center;\n"
                                   "text-transform: uppercase;")
        self.label_4.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setOpenExternalLinks(False)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        spacerItem3 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.MinimumExpanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.label_5 = QtWidgets.QLabel(parent=self.frame_columns_names)
        self.label_5.setMinimumSize(QtCore.QSize(150, 0))
        self.label_5.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("‘Open Sans Condensed’,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.label_5.setFont(font)
        self.label_5.setAcceptDrops(True)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet("color: #111;\n"
                                   "font-family: ‘Open Sans Condensed’, sans-serif;\n"
                                   "font-size: 14px;\n"
                                   "font-weight: 700;\n"
                                   "line-height: 64px;\n"
                                   "margin: 0 0 0;\n"
                                   "padding: 20px 30px;\n"
                                   "text-align: center;\n"
                                   "text-transform: uppercase;")
        self.label_5.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setOpenExternalLinks(False)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        spacerItem4 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.MinimumExpanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.label_6 = QtWidgets.QLabel(parent=self.frame_columns_names)
        self.label_6.setMinimumSize(QtCore.QSize(150, 0))
        self.label_6.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("‘Open Sans Condensed’,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.label_6.setFont(font)
        self.label_6.setAcceptDrops(True)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setStyleSheet("color: #111;\n"
                                   "font-family: ‘Open Sans Condensed’, sans-serif;\n"
                                   "font-size: 14px;\n"
                                   "font-weight: 700;\n"
                                   "line-height: 64px;\n"
                                   "margin: 0 0 0;\n"
                                   "padding: 20px 30px;\n"
                                   "text-align: center;\n"
                                   "text-transform: uppercase;")
        self.label_6.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setOpenExternalLinks(False)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        spacerItem5 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.MinimumExpanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.label_7 = QtWidgets.QLabel(parent=self.frame_columns_names)
        self.label_7.setMinimumSize(QtCore.QSize(150, 0))
        self.label_7.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("‘Open Sans Condensed’,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.label_7.setFont(font)
        self.label_7.setAcceptDrops(True)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setStyleSheet("color: #111;\n"
                                   "font-family: ‘Open Sans Condensed’, sans-serif;\n"
                                   "font-size: 14px;\n"
                                   "font-weight: 700;\n"
                                   "line-height: 64px;\n"
                                   "margin: 0 0 0;\n"
                                   "padding: 20px 30px;\n"
                                   "text-align: center;\n"
                                   "text-transform: uppercase;")
        self.label_7.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setWordWrap(True)
        self.label_7.setOpenExternalLinks(False)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        spacerItem6 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.MinimumExpanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.label_8 = QtWidgets.QLabel(parent=self.frame_columns_names)
        self.label_8.setMinimumSize(QtCore.QSize(130, 0))
        self.label_8.setMaximumSize(QtCore.QSize(130, 16777215))
        font = QtGui.QFont()
        font.setFamily("‘Open Sans Condensed’,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.label_8.setFont(font)
        self.label_8.setAcceptDrops(True)
        self.label_8.setAutoFillBackground(False)
        self.label_8.setStyleSheet("color: #111;\n"
                                   "font-family: ‘Open Sans Condensed’, sans-serif;\n"
                                   "font-size: 14px;\n"
                                   "font-weight: 700;\n"
                                   "line-height: 64px;\n"
                                   "margin: 0 0 0;\n"
                                   "padding: 20px 30px;\n"
                                   "text-align: center;\n"
                                   "text-transform: uppercase;")
        self.label_8.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_8.setScaledContents(False)
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setWordWrap(True)
        self.label_8.setOpenExternalLinks(False)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        spacerItem7 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.MinimumExpanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.label_9 = QtWidgets.QLabel(parent=self.frame_columns_names)
        self.label_9.setMinimumSize(QtCore.QSize(51, 0))
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.verticalLayout.addWidget(self.frame_columns_names)

        # скролл ареа
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1459, 517))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # общий фрейм для всех строк
        self.frame_for_rows = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.frame_for_rows.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_for_rows.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_for_rows.setObjectName("frame_for_rows")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_for_rows)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        # фрейм для каждой строки
        self.frame_rows_1 = QtWidgets.QFrame(parent=self.frame_for_rows)
        self.frame_rows_1.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_rows_1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_rows_1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_rows_1.setObjectName("frame_rows_1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_rows_1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        # комбобокс, значение названия
        self.comboBox_name = QtWidgets.QComboBox(parent=self.frame_rows_1)
        self.comboBox_name.setMinimumSize(QtCore.QSize(180, 0))
        self.comboBox_name.setMaximumSize(QtCore.QSize(180, 16777215))
        self.comboBox_name.setObjectName("comboBox_name")
        self.comboBox_name.setFont(self.font_rows)
        self.comboBox_name.setEditable(True)
        self.comboBox_name.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.NoInsert)
        self.comboBox_name.completer().setCompletionMode(QtWidgets.QCompleter.CompletionMode.PopupCompletion)
        self.comboBox_name.completer().popup().setFont(self.font_rows)
        self.comboBox_name.completer().setFilterMode(QtCore.Qt.MatchFlag.MatchContains)
        self.comboBox_name.lineEdit().setFont(self.font_rows)
        self.horizontalLayout_3.addWidget(self.comboBox_name)

        spacerItem8 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.MinimumExpanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)

        # значение кол-во изделий
        self.lineEdit_count_prod = QtWidgets.QLineEdit(parent=self.frame_rows_1)
        self.lineEdit_count_prod.setMinimumSize(QtCore.QSize(145, 0))
        self.lineEdit_count_prod.setMaximumSize(QtCore.QSize(145, 16777215))
        self.lineEdit_count_prod.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_count_prod.setReadOnly(False)
        self.lineEdit_count_prod.setFont(self.font_rows)
        self.lineEdit_count_prod.setObjectName("lineEdit_count_prod")
        self.lineEdit_count_prod.setReadOnly(True)
        self.horizontalLayout_3.addWidget(self.lineEdit_count_prod)

        spacerItem9 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.MinimumExpanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)

        # значение тип металла
        self.lineEdit_type_metall = QtWidgets.QLineEdit(parent=self.frame_rows_1)
        self.lineEdit_type_metall.setMinimumSize(QtCore.QSize(145, 0))
        self.lineEdit_type_metall.setMaximumSize(QtCore.QSize(145, 16777215))
        self.lineEdit_type_metall.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_type_metall.setReadOnly(True)
        self.lineEdit_type_metall.setFont(self.font_rows)
        self.lineEdit_type_metall.setObjectName("lineEdit_type_metall")
        self.horizontalLayout_3.addWidget(self.lineEdit_type_metall)

        spacerItem10 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.MinimumExpanding,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)

        # значение марка стали
        self.lineEdit_mark_steel = QtWidgets.QLineEdit(parent=self.frame_rows_1)
        self.lineEdit_mark_steel.setMinimumSize(QtCore.QSize(145, 0))
        self.lineEdit_mark_steel.setMaximumSize(QtCore.QSize(145, 16777215))
        self.lineEdit_mark_steel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_mark_steel.setReadOnly(True)
        self.lineEdit_mark_steel.setFont(self.font_rows)
        self.lineEdit_mark_steel.setObjectName("lineEdit_mark_steel")
        self.horizontalLayout_3.addWidget(self.lineEdit_mark_steel)

        spacerItem11 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.MinimumExpanding,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)

        # значение заготовка d
        self.lineEdit_zagotovka = QtWidgets.QLineEdit(parent=self.frame_rows_1)
        self.lineEdit_zagotovka.setMinimumSize(QtCore.QSize(145, 0))
        self.lineEdit_zagotovka.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEdit_zagotovka.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_zagotovka.setReadOnly(True)
        self.lineEdit_zagotovka.setFont(self.font_rows)
        self.lineEdit_zagotovka.setObjectName("lineEdit_zagotovka")
        self.horizontalLayout_3.addWidget(self.lineEdit_zagotovka)

        spacerItem12 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.MinimumExpanding,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem12)

        # значение длина
        self.lineEdit_lenght = QtWidgets.QLineEdit(parent=self.frame_rows_1)
        self.lineEdit_lenght.setMinimumSize(QtCore.QSize(145, 0))
        self.lineEdit_lenght.setMaximumSize(QtCore.QSize(145, 16777215))
        self.lineEdit_lenght.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_lenght.setReadOnly(True)
        self.lineEdit_lenght.setFont(self.font_rows)
        self.lineEdit_lenght.setObjectName("lineEdit_lenght")
        self.horizontalLayout_3.addWidget(self.lineEdit_lenght)

        spacerItem13 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.MinimumExpanding,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem13)

        # значение кол-во заготовок
        self.line_edit_weight = QtWidgets.QLineEdit(parent=self.frame_rows_1)
        self.line_edit_weight.setMinimumSize(QtCore.QSize(145, 0))
        self.line_edit_weight.setMaximumSize(QtCore.QSize(145, 16777215))
        self.line_edit_weight.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.line_edit_weight.setReadOnly(True)
        self.line_edit_weight.setFont(self.font_rows)
        self.line_edit_weight.setObjectName("line_edit_weight")
        self.horizontalLayout_3.addWidget(self.line_edit_weight)

        spacerItem14 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.MinimumExpanding,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem14)

        # значение чертеж
        self.lineEdit_drower = QtWidgets.QLineEdit(parent=self.frame_rows_1)
        self.lineEdit_drower.setMinimumSize(QtCore.QSize(105, 0))
        self.lineEdit_drower.setMaximumSize(QtCore.QSize(105, 16777215))
        self.lineEdit_drower.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_drower.setReadOnly(True)
        self.lineEdit_drower.setFont(self.font_rows)
        self.lineEdit_drower.setObjectName("lineEdit_drower")
        self.horizontalLayout_3.addWidget(self.lineEdit_drower)

        spacerItem15 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.MinimumExpanding,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem15)

        # кнопка удалить строку
        self.btn_del_row = QtWidgets.QPushButton(parent=self.frame_rows_1)
        self.btn_del_row.setMaximumSize(QtCore.QSize(27, 16777215))
        self.btn_del_row.setText("")
        self.btn_del_row.setObjectName("btn_del_row")
        self.btn_del_row.setIcon(self.delete_icon)
        self.horizontalLayout_3.addWidget(self.btn_del_row)
        self.verticalLayout_3.addWidget(self.frame_rows_1)
        spacerItem16 = QtWidgets.QSpacerItem(10, 1, QtWidgets.QSizePolicy.Policy.Minimum,
                                             QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        self.verticalLayout_3.addItem(spacerItem16)
        self.verticalLayout_2.addWidget(self.frame_for_rows)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.frame_btns = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_btns.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_btns.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_btns.setObjectName("frame_btns")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_btns)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # кнопка добавить строку
        self.add_row = QtWidgets.QPushButton(parent=self.frame_btns)
        self.add_row.setMinimumSize(QtCore.QSize(100, 100))
        self.add_row.setObjectName("add_row")
        self.add_row.setFont(self.font_rows)
        self.horizontalLayout.addWidget(self.add_row)

        # кнопка очистить
        self.clear_all = QtWidgets.QPushButton(parent=self.frame_btns)
        self.clear_all.setMinimumSize(QtCore.QSize(100, 100))
        self.clear_all.setObjectName("clear_all")
        self.clear_all.setFont(self.font_rows)
        self.horizontalLayout.addWidget(self.clear_all)

        # кнопка выгрузить в пдф
        self.upload_to_pdf = QtWidgets.QPushButton(parent=self.frame_btns)
        self.upload_to_pdf.setMinimumSize(QtCore.QSize(100, 100))
        self.upload_to_pdf.setObjectName("upload_to_pdf")
        self.upload_to_pdf.setFont(self.font_rows)
        self.horizontalLayout.addWidget(self.upload_to_pdf)

        # кнопка датабазы
        self.database_btn = QtWidgets.QPushButton(parent=self.frame_btns)
        self.database_btn.setMinimumSize(QtCore.QSize(100, 100))
        self.database_btn.setObjectName("database_btn")
        self.database_btn.setFont(self.font_rows)
        self.horizontalLayout.addWidget(self.database_btn)
        self.verticalLayout.addWidget(self.frame_btns)
        self.setCentralWidget(self.centralwidget)

        self.label.setText("Продукция")
        self.label_2.setText('Кол-во изделий')
        self.label_3.setText("Тип металла")
        self.label_4.setText("Марка стали")
        self.label_5.setText("Заготовка d, мм")
        self.label_6.setText("Длина, мм")
        self.label_7.setText("Общий вес(кг)")
        self.label_8.setText("Чертёж")
        self.add_row.setText("Добавить")
        self.clear_all.setText("Очистить всё")
        self.upload_to_pdf.setText("Выгрузить в PDF")
        self.database_btn.setText("База данных")

        self.main_class_slots_init()

    def main_class_slots_init(self):  # привязка главного класса к сигналам и слотам и combobox init
        self.comboBox_name.currentIndexChanged.connect(self.choose_product)
        self.clear_all.clicked.connect(self.clear_all_frames)
        self.upload_to_pdf.clicked.connect(self.unload_to_pdf)
        self.btn_del_row.clicked.connect(self.remove_frame)
        self.lineEdit_count_prod.textChanged.connect(self.amount_product_changed)
        self.database_btn.clicked.connect(self.configurate_database)
        self.comboBox_name.addItems([*self.product_list])
        self.add_row.clicked.connect(self.add_frame)

    def frame_slots_init(self):  # привязка нового фрейма к сигналам и слотам
        self.comboBox_name.currentIndexChanged.connect(self.choose_product)
        self.btn_del_row.clicked.connect(self.remove_frame)
        self.lineEdit_count_prod.textChanged.connect(self.amount_product_changed)
        self.comboBox_name.addItems([*self.product_list])

    def list_products_init(self):  # получение списка продукции для combobox
        self.product_list = ['']
        with sqlite3.connect(f'{DATA_PATH}database.db') as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT product FROM Products order by product')
            for product_row in cursor.fetchall():
                self.product_list.append(product_row[0])
        cursor.close()  # насчет close подумать
        connection.close()

    def choose_product(self):  # slot combobox выбрать продукцию
        combobox = self.sender()
        combobox_text = combobox.currentText()
        parent_frame = combobox.parent()
        parent_frame_children = parent_frame.children()
        if combobox_text != '':
            with sqlite3.connect(f'{DATA_PATH}database.db') as connection:
                cursor = connection.cursor()
                cursor.execute('SELECT diameter, type_metall, type_steel, lenght, weight, draw_path '
                               'FROM Products WHERE product = ?', (combobox_text,))
                selected_data: tuple = cursor.fetchone()
                transformed_data = {'lineEdit_zagotovka': selected_data[0],
                                    'lineEdit_type_metall': selected_data[1],
                                    'lineEdit_mark_steel': selected_data[2],
                                    'lineEdit_lenght': selected_data[3],
                                    'line_edit_weight': selected_data[4],
                                    'lineEdit_drower': selected_data[5]}
            cursor.close()  # ????????
            connection.close()  # ///учетка памяти если не закрывать, хотя менеджер контекста стоит xdxdxd///
            amount_line_edit = parent_frame.findChild(QtWidgets.QLineEdit, 'lineEdit_count_prod')
            amount_line_edit.setPlaceholderText('1')
            amount_line_edit.setReadOnly(False)
            for i in parent_frame_children:
                if i.objectName() == 'line_edit_weight':
                    i.setPlaceholderText(f'{transformed_data[i.objectName()]}')
                    continue
                if i.objectName() in transformed_data:
                    i.setText(f'{transformed_data[i.objectName()]}')
        else:
            for i in parent_frame_children:
                if isinstance(i, QtWidgets.QComboBox | QtWidgets.QPushButton | QtWidgets.QHBoxLayout):
                    continue
                else:
                    i: QtWidgets.QLineEdit
                    if i.objectName() == 'lineEdit_count_prod':
                        i.setReadOnly(True)
                    i.setText('')
                    i.setPlaceholderText('')

    def add_frame(self):  # slot кнопки добавить 1 фрейм
        self.count += 1
        # фрейм для каждой строки
        self.frame_rows_1 = QtWidgets.QFrame(parent=self.frame_for_rows)
        self.frame_rows_1.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_rows_1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_rows_1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_rows_1.setObjectName(f"frame_rows_{self.count}")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_rows_1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        # комбобокс, значение названия
        self.comboBox_name = QtWidgets.QComboBox(parent=self.frame_rows_1)
        self.comboBox_name.setMinimumSize(QtCore.QSize(180, 0))
        self.comboBox_name.setMaximumSize(QtCore.QSize(180, 16777215))
        self.comboBox_name.setObjectName("comboBox_name")
        self.comboBox_name.setFont(self.font_rows)
        self.comboBox_name.setEditable(True)
        self.comboBox_name.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.NoInsert)
        self.comboBox_name.completer().setCompletionMode(QtWidgets.QCompleter.CompletionMode.PopupCompletion)
        self.comboBox_name.completer().setFilterMode(QtCore.Qt.MatchFlag.MatchContains)
        self.comboBox_name.completer().popup().setFont(self.font_rows)
        self.comboBox_name.lineEdit().setFont(self.font_rows)
        self.horizontalLayout_3.addWidget(self.comboBox_name)

        spacerItem8 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.MinimumExpanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)

        # значение кол-во изделий
        self.lineEdit_count_prod = QtWidgets.QLineEdit(parent=self.frame_rows_1)
        self.lineEdit_count_prod.setMinimumSize(QtCore.QSize(145, 0))
        self.lineEdit_count_prod.setMaximumSize(QtCore.QSize(145, 16777215))
        self.lineEdit_count_prod.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_count_prod.setReadOnly(True)
        self.lineEdit_count_prod.setFont(self.font_rows)
        self.lineEdit_count_prod.setObjectName("lineEdit_count_prod")
        self.horizontalLayout_3.addWidget(self.lineEdit_count_prod)

        spacerItem9 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.MinimumExpanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)

        # значение тип металла
        self.lineEdit_type_metall = QtWidgets.QLineEdit(parent=self.frame_rows_1)
        self.lineEdit_type_metall.setMinimumSize(QtCore.QSize(145, 0))
        self.lineEdit_type_metall.setMaximumSize(QtCore.QSize(145, 16777215))
        self.lineEdit_type_metall.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_type_metall.setReadOnly(True)
        self.lineEdit_type_metall.setFont(self.font_rows)
        self.lineEdit_type_metall.setObjectName("lineEdit_type_metall")
        self.horizontalLayout_3.addWidget(self.lineEdit_type_metall)

        spacerItem10 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.MinimumExpanding,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)

        # значение марка стали
        self.lineEdit_mark_steel = QtWidgets.QLineEdit(parent=self.frame_rows_1)
        self.lineEdit_mark_steel.setMinimumSize(QtCore.QSize(145, 0))
        self.lineEdit_mark_steel.setMaximumSize(QtCore.QSize(145, 16777215))
        self.lineEdit_mark_steel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_mark_steel.setReadOnly(True)
        self.lineEdit_mark_steel.setFont(self.font_rows)
        self.lineEdit_mark_steel.setObjectName("lineEdit_mark_steel")
        self.horizontalLayout_3.addWidget(self.lineEdit_mark_steel)

        spacerItem11 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.MinimumExpanding,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)

        # значение заготовка d
        self.lineEdit_zagotovka = QtWidgets.QLineEdit(parent=self.frame_rows_1)
        self.lineEdit_zagotovka.setMinimumSize(QtCore.QSize(145, 0))
        self.lineEdit_zagotovka.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEdit_zagotovka.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_zagotovka.setReadOnly(True)
        self.lineEdit_zagotovka.setFont(self.font_rows)
        self.lineEdit_zagotovka.setObjectName("lineEdit_zagotovka")
        self.horizontalLayout_3.addWidget(self.lineEdit_zagotovka)

        spacerItem12 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.MinimumExpanding,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem12)

        # значение длина
        self.lineEdit_lenght = QtWidgets.QLineEdit(parent=self.frame_rows_1)
        self.lineEdit_lenght.setMinimumSize(QtCore.QSize(145, 0))
        self.lineEdit_lenght.setMaximumSize(QtCore.QSize(145, 16777215))
        self.lineEdit_lenght.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_lenght.setReadOnly(True)
        self.lineEdit_lenght.setFont(self.font_rows)
        self.lineEdit_lenght.setObjectName("lineEdit_lenght")
        self.horizontalLayout_3.addWidget(self.lineEdit_lenght)

        spacerItem13 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.MinimumExpanding,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem13)

        # значение кол-во заготовок
        self.line_edit_weight = QtWidgets.QLineEdit(parent=self.frame_rows_1)
        self.line_edit_weight.setMinimumSize(QtCore.QSize(145, 0))
        self.line_edit_weight.setMaximumSize(QtCore.QSize(145, 16777215))
        self.line_edit_weight.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.line_edit_weight.setReadOnly(True)
        self.line_edit_weight.setFont(self.font_rows)
        self.line_edit_weight.setObjectName("line_edit_weight")
        self.horizontalLayout_3.addWidget(self.line_edit_weight)

        spacerItem14 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.MinimumExpanding,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem14)

        # значение чертеж
        self.lineEdit_drower = QtWidgets.QLineEdit(parent=self.frame_rows_1)
        self.lineEdit_drower.setMinimumSize(QtCore.QSize(105, 0))
        self.lineEdit_drower.setMaximumSize(QtCore.QSize(105, 16777215))
        self.lineEdit_drower.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_drower.setReadOnly(True)
        self.lineEdit_drower.setFont(self.font_rows)
        self.lineEdit_drower.setObjectName("lineEdit_drower")
        self.horizontalLayout_3.addWidget(self.lineEdit_drower)

        spacerItem15 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.MinimumExpanding,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem15)

        # кнопка удалить строку
        self.btn_del_row = QtWidgets.QPushButton(parent=self.frame_rows_1)
        self.btn_del_row.setMaximumSize(QtCore.QSize(27, 16777215))
        # self.btn_del_row.setText("")
        self.btn_del_row.setObjectName("btn_del_row")
        self.btn_del_row.setIcon(self.delete_icon)
        self.horizontalLayout_3.addWidget(self.btn_del_row)

        self.frame_slots_init()

        self.verticalLayout_3.insertWidget(0, self.frame_rows_1)

    def remove_frame(self):  # slot кнопки удалить 1 фрейм(del_btn)
        del_btn = self.sender()
        parent_frame: QtWidgets.QFrame = del_btn.parent()
        # parent_frame.setParent(None) ///вариант удаления hz v chem raznica///
        parent_frame.deleteLater()

    def amount_product_changed(self):  # slot редактируемой QLineEdit(кол-во продукции)
        amount_line = self.sender()
        amount_line_text: str = amount_line.text()
        parent_frame = amount_line.parent()
        diameter_line_text = parent_frame.findChild(QtWidgets.QLineEdit, 'lineEdit_zagotovka').text()
        len_line_text = parent_frame.findChild(QtWidgets.QLineEdit, 'lineEdit_lenght').text()
        weight_line = parent_frame.findChild(QtWidgets.QLineEdit, 'line_edit_weight')
        if amount_line_text.isnumeric() and diameter_line_text != '' and len_line_text != '':
            weight_result = round(int(amount_line_text) * float(weight_line.placeholderText()), 1)
            parent_frame.findChild(QtWidgets.QLineEdit, 'line_edit_weight').setText(f'{weight_result}')
        else:
            weight_line.setText('')

    def clear_all_frames(self):
        self.count = 1
        main_frame = self.findChild(QtWidgets.QFrame, 'frame_for_rows')
        for frame in main_frame.children():
            if isinstance(frame, QtWidgets.QFrame):
                # frame.setParent(None)  # вариант удаления(v chem raznica - hz)
                frame.deleteLater()  # ///собирает в кучу что надо удалять потом удаляет(pyqt moment)///

    def configurate_database(self):  # slot кнопки конфигурации базы продуктов
        with sqlite3.connect(f'{DATA_PATH}database.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT product, diameter, type_metall, type_steel, lenght, weight, draw_path, id FROM Products order by product')
            rows_data = cursor.fetchall()
        cursor.close()
        conn.close()
        self.config_widget = ConfigBaseWidget(rows_data, DATA_PATH, DRAWS_PATH, OUTPUT_PATH, SRC_PATH, self)
        self.config_widget.setStyleSheet('QWidget#config_base { background-color: #cbcfd0 }')
        self.config_widget.show()

    def unload_to_pdf(self):  # slot кнопки выгрузки в pdf
        main_frame = self.findChild(QtWidgets.QFrame, 'frame_for_rows')
        upload_data = dict()  # {'frame': [QLineEdit1, QLineEdit2, QLinEdit3]}
        for frame in main_frame.children():
            if isinstance(frame, QtWidgets.QFrame):
                if frame.findChild(QtWidgets.QComboBox, 'comboBox_name').currentText() == '':
                    continue
                upload_data[f'{frame.objectName()}'] = list()
                for child_object in frame.children():
                    if isinstance(child_object, QtWidgets.QComboBox):
                        upload_data[f'{frame.objectName()}'].append(child_object.currentText())
                        continue
                    if isinstance(child_object, QtWidgets.QLineEdit):
                        upload_data[f'{frame.objectName()}'].append(child_object.text())

        # ///обработка ошибок///
        if len(upload_data) == 0:
            self.create_warn_messange('Предупреждение', 'Выберите хотя бы одну продукцию')
            return None

        for i in upload_data:
            if not os.path.isfile(f'{DRAWS_PATH}/{upload_data[i][-1]}'):
                self.create_warn_messange('Предупреждение', 'У одного или нескольких продуктов неверно задан путь к чертежу', '400')
                return None

        # ///дальше логика выгрузки в pdf из upload_data///
        pdfmetrics.registerFont(TTFont('RUSSIA', f'{SRC_PATH}font_TimesET_90.ttf'))
        data_drowers = list()
        data = [['Продукция', 'Количество изделий', 'Тип металла', 'Марка стали', 'Заготовка d, мм', 'Длина, мм',
                 'Общий вес(кг)']]
        for i in upload_data:
            data.append(upload_data[i])
        file_name = 'table.pdf'
        for i in data:
            if len(i) == 8:
                data_drowers.append(f"{DRAWS_PATH}{i.pop()}")
        # удаление путей чертежей из самой таблицы
        for i in data:
            if len(i) == 6:
                i.pop()
        # создание файла пдф с начальной таблицей
        P_sryle = ParagraphStyle("My style paragraph",
                                     fontName='Times-Roman',
                                     fontSize=16)
        P = Paragraph(DATE_RESULT, P_sryle)
        doc = SimpleDocTemplate(
            file_name,
            pagesize=letter
        )
        table = Table(data, spaceBefore=10)
        style = TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'RUSSIA'),
            ('FONTSIZE', (0,0), (-1, 0), 10),
            ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BOX', (0, 0), (-1, -1), 2, colors.black),
            ('BOX', (0, 0), (-1, 0), 2, colors.black),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ])
        table.setStyle(style)
        elems = []
        elems.append(P)
        elems.append(table)
        doc.build(elems)
        # объединение чертежей и начальной таблицы
        merger = PdfMerger()
        merger.append('table.pdf')
        for pdf in data_drowers:
            merger.append(pdf)
        while True:
            if not os.path.isfile(f"{OUTPUT_PATH}{DATE_RESULT}.pdf"):
                merger.write(f"{OUTPUT_PATH}{DATE_RESULT}.pdf")
                merger.close()
                break
            else:
                if not os.path.isfile(f"{OUTPUT_PATH}{DATE_RESULT}_{self.NAME_INDEX}.pdf"):
                    merger.write(f"{OUTPUT_PATH}{DATE_RESULT}_{self.NAME_INDEX}.pdf")
                    merger.close()
                    break
                else:
                    self.NAME_INDEX += 1
        os.remove('table.pdf')
        self.create_warn_messange('Уведомление', 'PDF файл успешно сохранён')

    def accepting_msg_box_1(self):
        self.warn_msg.deleteLater()

    def closeEvent(self, a0):
        if self.sender() is self.parent():
            app.exit()

    def create_warn_messange(self, title: str, text: str, size: str = '250') -> None:
        self.warn_msg = QtWidgets.QMessageBox()
        self.warn_msg.setWindowTitle(f'{title}')
        self.warn_msg.setStyleSheet(f'QLabel {{ min-width: {size}px}}')
        self.warn_msg.setText(f'{text}')
        self.warn_msg.accepted.connect(self.accepting_msg_box_1)
        self.warn_msg.show()

    def app_config(self):  # slot кнопки конфигурации приложения
        pass


if __name__ == "__main__":
    settings_set = {'Путь для чертежей', 'Путь базы данных', 'Путь результатов', 'Путь src'}
    if not os.path.isfile('settings.ini'):
        with open('settings.ini', 'w', encoding='UTF-8') as settings_create:
            settings_create.write('Путь для чертежей=./чертежи/\n'
                                  'Путь базы данных=./data/\n'
                                  'Путь результатов=./результаты выгрузки/\n'
                                  'Путь src=./src/\n\n'
                                  '# пути можно указать абсолютные либо относительные(default: ./чертежи/ | ./data/)')
        print('создан файл settings.ini')
    with open('settings.ini', 'r', encoding='UTF-8') as settings:
        r_lines = [x.strip() for x in settings if x.strip().split('=')[0] in settings_set]
    if len(r_lines) != 4:
        with open('settings.ini', 'w', encoding='UTF-8') as settings_create:
            settings_create.write('Путь для чертежей=./чертежи/\n'
                                  'Путь базы данных=./data/\n'
                                  'Путь результатов=./результаты выгрузки/\n'
                                  'Путь src=./src/\n\n'
                                  '# пути можно указать абсолютные либо относительные(default: ./чертежи/ ./data/)')
            print('исправлен файл settings.ini и выставлены параметры по умолчанию')
        with open('settings.ini', 'r', encoding='UTF-8') as settings:
            r_lines = [x.strip() for x in settings if x.strip().split('=')[0] in settings_set]

    DRAWS_PATH = ''.join([x.split('=')[1].strip() for x in r_lines if x.split('=')[0] == 'Путь для чертежей'])
    DATA_PATH = ''.join([x.split('=')[1].strip() for x in r_lines if x.split('=')[0] == 'Путь базы данных'])
    OUTPUT_PATH = ''.join([x.split('=')[1].strip() for x in r_lines if x.split('=')[0] == 'Путь результатов'])
    SRC_PATH = ''.join([x.split('=')[1].strip() for x in r_lines if x.split('=')[0] == 'Путь src'])
    a = str(datetime.now().date())
    DATE_RESULT = a[-2:] + '.' + a[5:7] + '.' + a[:4]
    if not os.path.exists(f'{DATA_PATH}'):
        os.mkdir(f'{DATA_PATH}')
        print(f'Создана папка data {DATA_PATH}')
    if not os.path.exists(f'{SRC_PATH}'):
        os.mkdir(f'{SRC_PATH}')
        with open('ПРОЧИТАЙ_МЕНЯ.txt', 'w', encoding='UTF-8') as f:
            f.write('Папка src была только что создана, и в ней отсутствует русский font для pdf\n'
                    'Его нужно скачать(любой), положить в src и переименовать в font_TimesET_90.ttf')
        print(f'Создана папка src {SRC_PATH} и файл "ПРОЧИТАЙ МЕНЯ", завершение процесса')
        quit()
    if not os.path.isfile(f'{SRC_PATH}font_TimesET_90.ttf'):
        with open('ПРОЧИТАЙ_МЕНЯ.txt', 'w', encoding='UTF-8') as f:
            f.write('В папке src отсутствует русский font для pdf\n'
                    'Его нужно скачать(любой), положить в src и переименовать в font_TimesET_90.ttf')
        print('Нужно прочитать файл "ПРОЧИТАЙ_МЕНЯ.txt"')
        quit()
    if not os.path.exists(f'{DRAWS_PATH}'):
        os.mkdir(f'{DRAWS_PATH}')
        print(f'Создана папка для чертежей {DRAWS_PATH}')
    if not os.path.exists(f'{OUTPUT_PATH}'):
        os.mkdir(f'{OUTPUT_PATH}')
        print(f'Создана папка для результатов')
    if not os.path.isfile(f'{DATA_PATH}database.db'):
        with sqlite3.connect(f'{DATA_PATH}database.db') as first_start:
            first_cursor = first_start.cursor()
            first_cursor.execute('''CREATE TABLE Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product TEXT NOT NULL,
            diameter TEXT,
            type_metall TEXT,
            type_steel TEXT,
            lenght TEXT,
            weight TEXT,
            draw_path TEXT);
            ''')
        first_cursor.close()
        first_start.close()
        print(f'Создана новая база данных')
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet('QMainWindow { background-color: #cbcfd0 }')
    app.setWindowIcon(QtGui.QIcon(f'{SRC_PATH}app_icon.ico'))
    MainWindow = ZAVOD()
    MainWindow.setStyleSheet('QComboBox QAbstractItemView{min-width: 300px;} QListView {min-width: 300px;}')
    MainWindow.show()
    sys.exit(app.exec())
