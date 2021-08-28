from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_passwordGeneratorUi(object):
    def setupUi(self, passwordGeneratorUi):
        passwordGeneratorUi.setObjectName("passwordGeneratorUi")
        passwordGeneratorUi.resize(324, 82)
        passwordGeneratorUi.setMinimumSize(QtCore.QSize(324, 82))
        passwordGeneratorUi.setMaximumSize(QtCore.QSize(324, 82))
        self.passwordLabel = QtWidgets.QLabel(passwordGeneratorUi)
        self.passwordLabel.setGeometry(QtCore.QRect(10, 50, 301, 21))
        self.passwordLabel.setText("")
        self.passwordLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.passwordLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.passwordLabel.setObjectName("passwordLabel")
        self.splitter_2 = QtWidgets.QSplitter(passwordGeneratorUi)
        self.splitter_2.setEnabled(True)
        self.splitter_2.setGeometry(QtCore.QRect(50, 20, 215, 28))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setEnabled(True)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.pwLengthLabel = QtWidgets.QLabel(self.splitter)
        self.pwLengthLabel.setEnabled(True)
        self.pwLengthLabel.setObjectName("pwLengthLabel")
        self.lengthBox = QtWidgets.QSpinBox(self.splitter)
        self.lengthBox.setEnabled(True)
        self.lengthBox.setMinimum(16)
        self.lengthBox.setMaximum(25)
        self.lengthBox.setObjectName("lengthBox")
        self.pushButton = QtWidgets.QPushButton(self.splitter_2)
        self.pushButton.setEnabled(True)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(passwordGeneratorUi)
        QtCore.QMetaObject.connectSlotsByName(passwordGeneratorUi)

    def retranslateUi(self, passwordGeneratorUi):
        _translate = QtCore.QCoreApplication.translate
        passwordGeneratorUi.setWindowTitle(_translate("passwordGeneratorUi", "Password Generator"))
        self.pwLengthLabel.setText(_translate("passwordGeneratorUi", "Length"))
        self.pushButton.setText(_translate("passwordGeneratorUi", "Generate"))
