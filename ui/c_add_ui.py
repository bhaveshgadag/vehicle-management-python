# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c_add.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(425, 327)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setObjectName("formLayout")
        self.label_c_id = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_c_id.setFont(font)
        self.label_c_id.setObjectName("label_c_id")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_c_id)
        self.input_c_id = QtWidgets.QLineEdit(self.frame)
        self.input_c_id.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.input_c_id.setFont(font)
        self.input_c_id.setObjectName("input_c_id")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.input_c_id)
        self.input_c_name = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.input_c_name.setFont(font)
        self.input_c_name.setObjectName("input_c_name")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.input_c_name)
        self.label_c_name = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_c_name.setFont(font)
        self.label_c_name.setObjectName("label_c_name")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_c_name)
        self.label_c_address = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_c_address.setFont(font)
        self.label_c_address.setObjectName("label_c_address")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_c_address)
        self.label_c_contact = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_c_contact.setFont(font)
        self.label_c_contact.setObjectName("label_c_contact")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_c_contact)
        self.input_c_contact = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.input_c_contact.setFont(font)
        self.input_c_contact.setObjectName("input_c_contact")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.input_c_contact)
        self.label_c_email = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_c_email.setFont(font)
        self.label_c_email.setObjectName("label_c_email")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_c_email)
        self.input_c_email = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.input_c_email.setFont(font)
        self.input_c_email.setObjectName("input_c_email")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.input_c_email)
        self.input_c_address = QtWidgets.QTextEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.input_c_address.setFont(font)
        self.input_c_address.setTabChangesFocus(True)
        self.input_c_address.setObjectName("input_c_address")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.input_c_address)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bt_ok = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.bt_ok.setFont(font)
        self.bt_ok.setObjectName("bt_ok")
        self.horizontalLayout.addWidget(self.bt_ok)
        self.bt_cancel = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.bt_cancel.setFont(font)
        self.bt_cancel.setObjectName("bt_cancel")
        self.horizontalLayout.addWidget(self.bt_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_c_id.setText(_translate("Dialog", "ID"))
        self.input_c_id.setText(_translate("Dialog", "AUTOMATIC"))
        self.label_c_name.setText(_translate("Dialog", "Name"))
        self.label_c_address.setText(_translate("Dialog", "Address"))
        self.label_c_contact.setText(_translate("Dialog", "Contact No. "))
        self.label_c_email.setText(_translate("Dialog", "Email"))
        self.bt_ok.setText(_translate("Dialog", "OK"))
        self.bt_cancel.setText(_translate("Dialog", "Cancel"))

