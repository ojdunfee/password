import sys
from PyQt5.QtWidgets import QDialog, QApplication
from password import Ui_passwordGeneratorUi
from passwordGenerator import PasswordGenerator

class Password(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_passwordGeneratorUi()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.generate_password)

    def generate_password(self):
        pw = PasswordGenerator(length=self.ui.lengthBox.value()).password
        self.ui.passwordLabel.setText(pw)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    password_generator = Password()
    password_generator.show()
    sys.exit(app.exec_())
        
