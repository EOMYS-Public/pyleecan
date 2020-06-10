# -*- coding: utf-8 -*-

# File generated according to PHoleM58.ui
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PHoleM58(object):
    def setupUi(self, PHoleM58):
        PHoleM58.setObjectName("PHoleM58")
        PHoleM58.resize(740, 440)
        PHoleM58.setMinimumSize(QtCore.QSize(740, 440))
        PHoleM58.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.horizontalLayout = QtWidgets.QHBoxLayout(PHoleM58)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.img_slot = QtWidgets.QLabel(PHoleM58)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_slot.sizePolicy().hasHeightForWidth())
        self.img_slot.setSizePolicy(sizePolicy)
        self.img_slot.setMinimumSize(QtCore.QSize(500, 170))
        self.img_slot.setMaximumSize(QtCore.QSize(500, 170))
        self.img_slot.setText("")
        self.img_slot.setPixmap(
            QtGui.QPixmap(":/images/images/MachineSetup/WSlot/Slot_58.PNG")
        )
        self.img_slot.setScaledContents(True)
        self.img_slot.setObjectName("img_slot")
        self.verticalLayout_3.addWidget(self.img_slot)
        self.txt_constraint = QtWidgets.QTextEdit(PHoleM58)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.txt_constraint.sizePolicy().hasHeightForWidth()
        )
        self.txt_constraint.setSizePolicy(sizePolicy)
        self.txt_constraint.setMinimumSize(QtCore.QSize(200, 0))
        self.txt_constraint.setMaximumSize(QtCore.QSize(16777215, 100))
        self.txt_constraint.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txt_constraint.setTextInteractionFlags(
            QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse
        )
        self.txt_constraint.setObjectName("txt_constraint")
        self.verticalLayout_3.addWidget(self.txt_constraint)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.in_H0 = QtWidgets.QLabel(PHoleM58)
        self.in_H0.setObjectName("in_H0")
        self.gridLayout.addWidget(self.in_H0, 0, 0, 1, 1)
        self.lf_H0 = FloatEdit(PHoleM58)
        self.lf_H0.setObjectName("lf_H0")
        self.gridLayout.addWidget(self.lf_H0, 0, 1, 1, 1)
        self.unit_R0 = QtWidgets.QLabel(PHoleM58)
        self.unit_R0.setObjectName("unit_R0")
        self.gridLayout.addWidget(self.unit_R0, 7, 2, 1, 1)
        self.unit_H0 = QtWidgets.QLabel(PHoleM58)
        self.unit_H0.setObjectName("unit_H0")
        self.gridLayout.addWidget(self.unit_H0, 0, 2, 1, 1)
        self.unit_W2 = QtWidgets.QLabel(PHoleM58)
        self.unit_W2.setObjectName("unit_W2")
        self.gridLayout.addWidget(self.unit_W2, 5, 2, 1, 1)
        self.unit_W0 = QtWidgets.QLabel(PHoleM58)
        self.unit_W0.setObjectName("unit_W0")
        self.gridLayout.addWidget(self.unit_W0, 3, 2, 1, 1)
        self.unit_W1 = QtWidgets.QLabel(PHoleM58)
        self.unit_W1.setObjectName("unit_W1")
        self.gridLayout.addWidget(self.unit_W1, 4, 2, 1, 1)
        self.in_W3 = QtWidgets.QLabel(PHoleM58)
        self.in_W3.setObjectName("in_W3")
        self.gridLayout.addWidget(self.in_W3, 6, 0, 1, 1)
        self.lf_W0 = FloatEdit(PHoleM58)
        self.lf_W0.setObjectName("lf_W0")
        self.gridLayout.addWidget(self.lf_W0, 3, 1, 1, 1)
        self.in_W1 = QtWidgets.QLabel(PHoleM58)
        self.in_W1.setObjectName("in_W1")
        self.gridLayout.addWidget(self.in_W1, 4, 0, 1, 1)
        self.in_W2 = QtWidgets.QLabel(PHoleM58)
        self.in_W2.setObjectName("in_W2")
        self.gridLayout.addWidget(self.in_W2, 5, 0, 1, 1)
        self.in_R0 = QtWidgets.QLabel(PHoleM58)
        self.in_R0.setObjectName("in_R0")
        self.gridLayout.addWidget(self.in_R0, 7, 0, 1, 1)
        self.lf_W1 = FloatEdit(PHoleM58)
        self.lf_W1.setObjectName("lf_W1")
        self.gridLayout.addWidget(self.lf_W1, 4, 1, 1, 1)
        self.in_H1 = QtWidgets.QLabel(PHoleM58)
        self.in_H1.setObjectName("in_H1")
        self.gridLayout.addWidget(self.in_H1, 1, 0, 1, 1)
        self.in_H2 = QtWidgets.QLabel(PHoleM58)
        self.in_H2.setObjectName("in_H2")
        self.gridLayout.addWidget(self.in_H2, 2, 0, 1, 1)
        self.lf_W2 = FloatEdit(PHoleM58)
        self.lf_W2.setObjectName("lf_W2")
        self.gridLayout.addWidget(self.lf_W2, 5, 1, 1, 1)
        self.in_W0 = QtWidgets.QLabel(PHoleM58)
        self.in_W0.setObjectName("in_W0")
        self.gridLayout.addWidget(self.in_W0, 3, 0, 1, 1)
        self.unit_H2 = QtWidgets.QLabel(PHoleM58)
        self.unit_H2.setObjectName("unit_H2")
        self.gridLayout.addWidget(self.unit_H2, 2, 2, 1, 1)
        self.lf_W3 = FloatEdit(PHoleM58)
        self.lf_W3.setObjectName("lf_W3")
        self.gridLayout.addWidget(self.lf_W3, 6, 1, 1, 1)
        self.lf_R0 = FloatEdit(PHoleM58)
        self.lf_R0.setText("")
        self.lf_R0.setObjectName("lf_R0")
        self.gridLayout.addWidget(self.lf_R0, 7, 1, 1, 1)
        self.lf_H1 = FloatEdit(PHoleM58)
        self.lf_H1.setObjectName("lf_H1")
        self.gridLayout.addWidget(self.lf_H1, 1, 1, 1, 1)
        self.lf_H2 = FloatEdit(PHoleM58)
        self.lf_H2.setObjectName("lf_H2")
        self.gridLayout.addWidget(self.lf_H2, 2, 1, 1, 1)
        self.unit_H1 = QtWidgets.QLabel(PHoleM58)
        self.unit_H1.setObjectName("unit_H1")
        self.gridLayout.addWidget(self.unit_H1, 1, 2, 1, 1)
        self.unit_W3 = QtWidgets.QLabel(PHoleM58)
        self.unit_W3.setObjectName("unit_W3")
        self.gridLayout.addWidget(self.unit_W3, 6, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.w_mat_0 = WMatSelect(PHoleM58)
        self.w_mat_0.setMinimumSize(QtCore.QSize(100, 0))
        self.w_mat_0.setObjectName("w_mat_0")
        self.verticalLayout_2.addWidget(self.w_mat_0)
        self.g_output = QtWidgets.QGroupBox(PHoleM58)
        self.g_output.setMinimumSize(QtCore.QSize(200, 0))
        self.g_output.setObjectName("g_output")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.g_output)
        self.verticalLayout.setObjectName("verticalLayout")
        self.out_slot_surface = QtWidgets.QLabel(self.g_output)
        self.out_slot_surface.setObjectName("out_slot_surface")
        self.verticalLayout.addWidget(self.out_slot_surface)
        self.out_magnet_surface = QtWidgets.QLabel(self.g_output)
        self.out_magnet_surface.setObjectName("out_magnet_surface")
        self.verticalLayout.addWidget(self.out_magnet_surface)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.g_output)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(PHoleM58)
        QtCore.QMetaObject.connectSlotsByName(PHoleM58)
        PHoleM58.setTabOrder(self.lf_H0, self.lf_H1)
        PHoleM58.setTabOrder(self.lf_H1, self.lf_H2)
        PHoleM58.setTabOrder(self.lf_H2, self.lf_W0)
        PHoleM58.setTabOrder(self.lf_W0, self.lf_W1)
        PHoleM58.setTabOrder(self.lf_W1, self.lf_W2)
        PHoleM58.setTabOrder(self.lf_W2, self.lf_W3)
        PHoleM58.setTabOrder(self.lf_W3, self.lf_R0)
        PHoleM58.setTabOrder(self.lf_R0, self.txt_constraint)

    def retranslateUi(self, PHoleM58):
        _translate = QtCore.QCoreApplication.translate
        PHoleM58.setWindowTitle(_translate("PHoleM58", "Form"))
        self.txt_constraint.setHtml(
            _translate(
                "PHoleM58",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600; text-decoration: underline;">Constraints :</span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'MS Shell Dlg 2\'; font-size:14pt;">W1 + W2 &lt; W0</span></p></body></html>',
            )
        )
        self.in_H0.setText(_translate("PHoleM58", "H0 :"))
        self.unit_R0.setText(_translate("PHoleM58", "m"))
        self.unit_H0.setText(_translate("PHoleM58", "m"))
        self.unit_W2.setText(_translate("PHoleM58", "m"))
        self.unit_W0.setText(_translate("PHoleM58", "m"))
        self.unit_W1.setText(_translate("PHoleM58", "m"))
        self.in_W3.setText(_translate("PHoleM58", "W3 :"))
        self.in_W1.setText(_translate("PHoleM58", "W1 :"))
        self.in_W2.setText(_translate("PHoleM58", "W2 :"))
        self.in_R0.setText(_translate("PHoleM58", "R0 :"))
        self.in_H1.setText(_translate("PHoleM58", "H1 :"))
        self.in_H2.setText(_translate("PHoleM58", "H2 :"))
        self.in_W0.setText(_translate("PHoleM58", "W0 :"))
        self.unit_H2.setText(_translate("PHoleM58", "m"))
        self.unit_H1.setText(_translate("PHoleM58", "m"))
        self.unit_W3.setText(_translate("PHoleM58", "rad"))
        self.g_output.setTitle(_translate("PHoleM58", "Output"))
        self.out_slot_surface.setText(_translate("PHoleM58", "Hole suface : ?"))
        self.out_magnet_surface.setText(_translate("PHoleM58", "Magnet surface : ?"))


from ......GUI.Dialog.DMatLib.WMatSelect.WMatSelect import WMatSelect
from ......GUI.Tools.FloatEdit import FloatEdit
from pyleecan.GUI.Resources import pyleecan_rc
