from PyQt5 import QtWidgets
import generatorui
import random


class ExampleApp(QtWidgets.QMainWindow, generatorui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.generate_variants)

    def generate_variants(self):
        """
          Случайным образом генерирует и выводит на экран
          номера билетов для каждого студента
        """
        students_count = int(self.lineEdit.text())
        exam_papers_count = int(self.lineEdit_2.text())

        self.textBrowser.clear()
        # self.textBrowser.repaint()

        # check if exam papers number more than students amount
        if exam_papers_count < students_count:
            for val in range(students_count):
                self.textBrowser.append(str(f'{val + 1:2}й студент - вариант № {random.randrange(exam_papers_count) + 1}'))

            return None

        # define list of exam papers numbers
        number_list = []

        # fulfill list by numbers
        for i in range(1, exam_papers_count + 1):
            number_list.append(i)

        # randomly shuffle fulfilled list
        random.shuffle(number_list)

        # formatting print exam papers number in order of students number
        for val in range(students_count):
            self.textBrowser.append(str(f'{val + 1:2}й студент - вариант № {number_list[val]}'))

        return None


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = ExampleApp()
    window.show()
    app.exec_()
