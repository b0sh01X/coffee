import sys
import sqlite3

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.connection = sqlite3.connect('coffee.db')
        self.select_data()

    def select_data(self):
        # Получим результат запроса, 
        # который ввели в текстовое поле
        res = self.connection.cursor().execute('SELECT coffee.id, coffee.name, Zharka.name, moloto.name, coffee.opisan, coffee.price, coffee.obj '
                                               'FROM coffee LEFT JOIN Zharka ON coffee.obg_id=Zharka.id '
                                               'LEFT JOIN moloto ON coffee.mol_id=moloto.id').fetchall()
        # Заполним размеры таблицы
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setItem(
                    0, 0, QTableWidgetItem(str('ID')))
        self.tableWidget.setItem(
                    0, 1, QTableWidgetItem(str('название сорта')))
        self.tableWidget.setItem(
                    0, 2, QTableWidgetItem(str('степень обжарки')))
        self.tableWidget.setItem(
                    0, 3, QTableWidgetItem(str('молотось')))
        self.tableWidget.setItem(
                    0, 4, QTableWidgetItem(str('описание')))
        self.tableWidget.setItem(
                    0, 5, QTableWidgetItem(str('цена')))
        self.tableWidget.setItem(
                    0, 6, QTableWidgetItem(str('объём упаковки')))
        # Заполняем таблицу элементами
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i + 1, j, QTableWidgetItem(str(elem)))

    def closeEvent(self, event):
        self.connection.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())