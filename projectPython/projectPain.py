import sys
import math
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QColor, QPixmap
from PyQt5.QtCore import *


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI() 
        self.b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.cows = 0
        self.turns = 0
        self.bulls = 0
        self.name = ''
        self.number = ''
        self.guess = 0
        self.mode = 'pen'
        self.points = set()
        self.size = 5
        self.x = 0
        self.color = QColor(255, 0, 0)
        self.color2 = QColor(255, 255, 255)
        self.isLoad = False
        self.isNew = False
 
    def initUI(self):
        self.file_name = QLineEdit(self)
        self.file_name.move(160, 0)
        
        self.lb1 = QLabel(self)
        self.lb1.setText('')
        self.lb1.hide()
        self.lb1.move(5, 20)
         
        self.lb2 = QLabel(self)
        self.lb2.setText('')
        self.lb2.hide()
        self.lb2.move(5, 20)
        
        self.lb3 = QLabel(self)
        self.lb3.setText('')
        self.lb3.hide()
        self.lb3.move(5, 20)
        
        self.write = QLabel(self)
        self.write.setText('Введите трехзначное число: ')
        self.write.hide()
        self.write.move(5, 20)
        
        self.res = QLabel(self) 
        self.res.setText('                                                    ')
        self.res.hide()
        self.res.resize(200, self.res.height())
        self.res.move(80, 50)
        
        self.back = QPushButton('Назад', self)
        self.back.resize(self.back.sizeHint())
        self.back.move(100, 110)
        self.back.hide()
        self.back.clicked.connect(self.tomenu)
        
        self.savef = QPushButton('Сохранить', self)
        self.savef.resize(self.savef.sizeHint())
        self.savef.move(100, 110)
        self.savef.hide()
        self.savef.clicked.connect(self.saveFile)
        
        self.check = QPushButton('Проверить', self)
        self.check.resize(self.check.sizeHint())
        self.check.move(100, 80)
        self.check.hide()
        self.check.clicked.connect(self.checkn)
        
        self.cb = QLineEdit(self)
        self.cb.move(155, 20)        
        self.cb.hide()
        
        self.newFile = QLineEdit(self)
        self.newFile.move(155, 20)        
        self.newFile.hide()        
        
        self.enter = QLabel(self)
        self.enter.setText('Введите название файла: ')
        self.enter.move(20, 0)
        
        self.load = QPushButton('Загрузить', self)
        self.load.resize(self.load.sizeHint())
        self.load.move(90, 30)
        self.load.clicked.connect(self.loadf)

        self.sphere = QPushButton('Круг', self)
        self.sphere.resize(self.sphere.sizeHint())
        self.sphere.move(0, 0)
        self.sphere.hide()
        self.sphere.clicked.connect(self.csphere)
        
        self.square = QPushButton('Квадрат', self)
        self.square.resize(self.square.sizeHint())
        self.square.move(0, 0)
        self.square.hide()
        self.square.clicked.connect(self.csquare)
        
        self.penc = QPushButton('Ручка', self)
        self.penc.resize(self.penc.sizeHint())
        self.penc.hide()
        self.penc.clicked.connect(self.pencil)
        
        self.inc = QPushButton('Увеличить', self)
        self.inc.resize(self.inc.sizeHint())
        self.inc.move(0, 0)
        self.inc.hide()
        self.inc.clicked.connect(self.incr)
        
        self.dec = QPushButton('Уменьшить', self)
        self.dec.resize(self.dec.sizeHint())
        self.dec.move(0, 0)
        self.dec.hide()
        self.dec.clicked.connect(self.decr)
        
        self.ccolor = QPushButton('Выбор цвета', self)
        self.ccolor.resize(self.ccolor.sizeHint())
        self.ccolor.move(0, 0)
        self.ccolor.hide()
        self.ccolor.clicked.connect(self.change)
        
        self.save2 = QPushButton('Сохранить', self)
        self.save2.resize(self.save2.sizeHint())
        self.save2.hide()
        self.save2.clicked.connect(self.save2file)
        
        self.Or = QLabel(self)
        self.Or.setText('или')
        self.Or.move(115, 60)
        
        self.new = QPushButton('Создать новый файл', self)
        self.new.resize(self.new.sizeHint())
        self.new.move(70, 80)
        self.new.clicked.connect(self.paint)
        
        self.Or2 = QLabel(self)
        self.Or2.setText('или')
        self.Or2.move(115, 110)
        
        self.game = QPushButton('Поиграть в быки и коровы', self)
        self.game.resize(self.game.sizeHint())
        self.game.move(55, 130)
        self.game.clicked.connect(self.gamecb)
        
        self.leaders = QPushButton('Доска лидеров', self)
        self.leaders.resize(self.leaders.sizeHint())
        self.leaders.move(65 + self.game.width(), 130)
        self.leaders.clicked.connect(self.leaderboard)
        
        self.setGeometry(300, 300, 300, 155)
        self.setWindowTitle('Запуск')
        self.show()
    
    def saveFile(self):
        if self.isLoad:
            p = QPixmap(self.pixmap.width(), self.height()
                        - self.sphere.height() - self.square.height() 
                        - self.inc.height())
            self.render(p)
            p.save(self.name) # Сохранение файла с загруженным фоном
        else:
            self.newFile.show()
            self.newFile.move(20, 20)
            self.save2.show()
            self.save2.move(20, 40)
            self.resize(170, 70)
            self.setWindowTitle('Сохранение')
            self.sphere.hide()
            self.square.hide()
            self.inc.hide()
            self.ccolor.hide()
            self.dec.hide()
            self.penc.hide()
            self.savef.hide() # окно сохранения нового файла с новым названием
    
    def save2file(self):
        self.newFile.hide()
        self.save2.hide()
        self.sphere.show()
        self.square.show()
        self.inc.show()
        self.dec.show()
        self.ccolor.show()
        self.penc.show()
        self.savef.show()
        self.resize(500, self.dec.y() + self.dec.height())
        self.setWindowTitle('Рисуйте')
        p = QPixmap(500, self.sphere.y())
        self.render(p)
        p.save(self.newFile.text()) # сохранение нового файла с возможностью
        # нового названия
        
    def loadf(self):
        self.isLoad = True
        self.name = self.file_name.text()
        self.leaders.hide()
        self.file_name.hide()
        self.enter.hide()
        self.load.hide()
        self.Or.hide()
        self.new.hide()
        self.Or2.hide()
        self.game.hide()
        self.back.hide()
        
        self.pixmap = QPixmap(self.name)
        
        self.sphere.move(0, self.pixmap.height())
        self.sphere.resize(self.pixmap.width() / 2, self.sphere.height())
        self.sphere.show()
        
        self.square.move(0, self.pixmap.height() + self.sphere.height())
        self.square.resize(self.pixmap.width() / 2, self.square.height())
        self.square.show()
        
        self.inc.move(0, self.pixmap.height() + self.sphere.height()
                      + self.square.height())
        self.inc.resize(self.pixmap.width() / 2, self.inc.height())
        self.inc.show()
        
        self.dec.move(self.inc.width(), self.inc.y())
        self.dec.resize(self.pixmap.width() / 2, self.inc.height())
        self.dec.show()
        
        self.ccolor.move(self.sphere.width(), self.pixmap.height())
        self.ccolor.resize(self.pixmap.width() / 2, self.inc.height())
        self.ccolor.show()
        
        self.penc.move(self.square.width(), self.ccolor.y()
                       + self.ccolor.height())
        self.penc.resize(self.pixmap.width() / 4, self.inc.height())
        self.penc.show()
        
        self.savef.move(self.penc.x() + self.penc.width(),
                        self.ccolor.y() + self.ccolor.height())
        self.savef.resize(self.pixmap.width() / 4, self.inc.height())
        self.savef.show()
        
        self.resize(self.pixmap.width(), self.pixmap.height() +
                    self.sphere.height() + self.square.height() +
                    self.inc.height())
        self.setWindowTitle('Рисуйте') # окно редактора с загруженным фоном
        
    def paint(self):
        self.isNew = True
        self.leaders.hide()
        self.file_name.hide()
        self.enter.hide()
        self.load.hide()
        self.Or.hide()
        self.Or2.hide()
        self.game.hide()        
        self.new.hide()
        self.back.hide()
        self.check.hide()
        self.sphere.show()
        self.square.show()
        self.inc.show()
        self.dec.show()
        self.ccolor.show()
        self.penc.show()
        self.savef.show()
        self.setGeometry(300, 300, 500, 500)
        self.sphere.move(0, 400)
        self.sphere.resize(250, self.sphere.height())
        self.square.move(0, 400 + self.sphere.height())
        self.square.resize(250, self.sphere.height())
        self.inc.move(0, self.square.y() + self.square.height())
        self.inc.resize(250, self.sphere.height())
        self.dec.move(self.inc.width(), self.inc.y())
        self.dec.resize(250, self.sphere.height())
        self.ccolor.move(self.sphere.width(), 400)
        self.ccolor.resize(250, self.sphere.height())
        self.savef.move(375, 400 + self.ccolor.height())
        self.savef.resize(125, self.sphere.height())
        self.penc.move(self.square.width(), 400 + self.ccolor.height())
        self.penc.resize(125, self.sphere.height())
        self.penc.setText('Ручка')
        self.setWindowTitle('Рисуйте')
        self.resize(500, self.dec.y() + self.dec.height()) # окно редактора с
        # белым фоном
    
    def gamecb(self):
        c = ''
        self.leaders.hide()
        self.turns = 0
        for i in range(3):
            d = str(random.choice(self.b))
            self.b.remove(int(d))
            c += d
        self.guess = int(''.join(c))
        self.file_name.hide()
        self.enter.hide()
        self.load.hide()
        self.Or.hide()
        self.Or2.hide()
        self.game.hide()        
        self.new.hide()   
        self.cb.show()
        self.write.show()
        self.check.show()
        self.res.show()
        self.res.setText('                                                    ')
        self.back.show()
        self.setWindowTitle('Быки и коровы')
        self.resize(290, 150) # окно игры быки и коровы
        
    def tomenu(self):
        self.lb1.hide()
        self.lb2.hide()
        self.lb3.hide()
        self.leaders.hide()
        self.leaders.show()
        self.res.setText('                                                    ')
        self.guess = 0
        self.turns = 0
        self.cows = 0
        self.bulls = 0
        self.res.clear()
        self.res.hide()
        self.back.hide()
        self.cb.hide()
        self.cb.clear()
        self.write.hide()
        self.b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.number = ''
        self.file_name.show()
        self.enter.show()
        self.load.show()
        self.Or.show()
        self.Or2.show()
        self.game.show()        
        self.new.show()
        self.setGeometry(300, 300, 300, 155)
        self.setWindowTitle('Запуск') # реализация кнопки
        # для возвращения в главное меню
    
    def checkn(self):
        self.turns += 1
        isRepeat = False
        self.cows = 0
        self.bulls = 0
        a = list(self.cb.text())[:3]
        self.cb.clear()
        b = list(str(self.guess))
        for i in range(3):
            if a[i] == b[i] and a.count(a[i]) == 1:
                self.bulls += 1
            elif a[i] in b and a.count(a[i]) == 1:
                self.cows += 1
            if a.count(a[i]) > 1:
                isRepeat = True
        if isRepeat:
            self.res.setText('Нельзя повторять цифры')
        else:
            if self.bulls == 3:
                self.res.setText('Вы угадали число за ' + str(self.turns)
                                 + ' ходов')
                with open('candbResults.txt', 'a') as file:
                    file.write(str(self.turns) + ' ')                
            else:
                self.res.setText('Коров: ' + str(self.cows) + ', Быков: '
                                 + str(self.bulls)) # проверка заданного числа 
                # на крупный рогатый скот
     
    def closeEvent(self, e):
        result = QMessageBox.question(self, 'Подтверждение закрытия окна',
                                      'Вы уверены?',
                                      QMessageBox.Yes | QMessageBox.No,
                                      QMessageBox.No)
        if result == QMessageBox.Yes:
            e.accept()
            QWidget.closeEvent(self, e)
        else:
            e.ignore()

    def mouseMoveEvent(self, event):
        self.points.add((event.x(), event.y(), self.size, self.color.getRgb(),
                         self.color2.getRgb(), self.mode))
        self.repaint()
        
    def paintEvent(self, event):
        if self.isLoad:
            qp = QPainter()
            qp.begin(self)
            qp.drawPixmap(0, 0, self.width(), self.height()
                          - self.sphere.height() - self.square.height()
                          - self.inc.height(), self.pixmap)
            for point in self.points:
                if point[5] == 'pen':              
                    qp.setBrush(QColor().fromRgb(*point[3]))
                    qp.setPen(QColor().fromRgb(*point[3]))                 
                    qp.drawEllipse(point[0], point[1],
                                   point[2], point[2])
                elif point[5] == 'sphere':              
                    qp.setBrush(QColor().fromRgb(*point[4]))
                    qp.setPen(QColor().fromRgb(*point[3]))                 
                    qp.drawEllipse(point[0], point[1],
                                   point[2], point[2]) 
                elif point[5] == 'square':                      
                    qp.setBrush(QColor().fromRgb(*point[4]))
                    qp.setPen(QColor().fromRgb(*point[3]))                 
                    qp.drawRect(point[0], point[1],
                                point[2], point[2])
            qp.end()
        if self.isNew:
            qp = QPainter()
            qp.begin(self)
            for point in self.points:
                if point[5] == 'pen':              
                    qp.setBrush(QColor().fromRgb(*point[3]))
                    qp.setPen(QColor().fromRgb(*point[3]))                 
                    qp.drawEllipse(point[0], point[1],
                                   point[2], point[2])
                elif point[5] == 'sphere':              
                    qp.setBrush(QColor().fromRgb(*point[4]))
                    qp.setPen(QColor().fromRgb(*point[3]))                 
                    qp.drawEllipse(point[0], point[1],
                                   point[2], point[2]) 
                elif point[5] == 'square':                      
                    qp.setBrush(QColor().fromRgb(*point[4]))
                    qp.setPen(QColor().fromRgb(*point[3]))                 
                    qp.drawRect(point[0], point[1],
                                point[2], point[2])
            qp.end()            
     # обработчики событий прорисовки, движения мыши и закрытия программы
    def csphere(self):
        self.mode = 'sphere' 
    
    def csquare(self):
        self.mode = 'square'
    
    def pencil(self):
        self.mode = 'pen' # изменение типа фигуры
        
    def incr(self):
        self.size += 2
        
    def decr(self):
        if self.size > 2:
            self.size -= 2 # изменение размера кисти
    
    def change(self):
        self.color = QColorDialog.getColor() # окно выбора цвета
    
    def leaderboard(self):
        self.leaders.hide()
        self.file_name.hide()
        self.enter.hide()
        self.load.hide()
        self.Or.hide()
        self.new.hide()
        self.Or2.hide()
        self.game.hide()
        self.check.hide()
        self.back.show()  
        self.lb1.show()
        self.lb2.show()
        self.lb3.show()
        file = open('candbResults.txt', mode='r')
        a = 1000000
        lines = file.readlines()
        lines2 = ''.join(lines).split()
        if len(lines2) >= 1:
            for i in range(len(lines2)):
                if int(lines2[i]) < a:
                    a = int(lines2[i])
            lines2.remove(str(a))
            self.lb1.setText('Первое место - ' + str(a) + ' - Вы')
        a = 1000000
        if len(lines2) >= 1:
            for i in range(len(lines2)):
                if int(lines2[i]) < a:
                    a = int(lines2[i])
            lines2.remove(str(a))
            self.lb2.setText('Второе место - ' + str(a) + ' - Вы')
        a = 1000000
        if len(lines2) >= 1:
            for i in range(len(lines2)):
                if int(lines2[i]) < a:
                    a = int(lines2[i])
            lines2.remove(str(a))
            self.lb3.setText('Третье место - ' + str(a)         + ' - Вы')
        self.lb1.move(30, 30)
        self.lb1.resize(200, self.lb1.height())
        self.lb2.move(30, 50)
        self.lb2.resize(200, self.lb2.height())
        self.lb3.move(30, 70)
        self.lb3.resize(200, self.lb3.height())
        self.setWindowTitle('Доска лидеров')
        self.resize(200, 200) # Прочитываем результаты из файла с ходами,
        # выводим до трех лучших результатов 
        
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())