import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton,
                             QLabel, QLCDNumber, QLineEdit,
                             QColorDialog, QAction, QComboBox)
import PyQt5.QtGui as QtGui
from PyQt5 import QtCore
import requests

DICT_WITH_LANGS = {'Русский': 'ru', 'Испанский': 'es', 'Английский': 'en',
                   'Итальянский': 'it', 'Французский': 'fr', 'Немецкий': 'de',
                   'Нидерландский': 'nl', 'Украинский': 'uk',
                   'Словенский': 'sl', 'Норвежский': 'no', 'Литовский': 'lt',
                   'Латинский': 'la', 'Белорусский': 'be'}
LANGUAGE1, LANGUAGE2 = '', ''
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
a = 'trnsl.1.1.20160119T035517Z.50c6906978ef1961'
b = '.08d0c5ada49017ed764c042723895ffab867be7a'
KEY = a + b


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 150, 400, 300)
        self.setWindowTitle('TEXT ENGINE')

        combo = QComboBox(self)
        combo.addItem("---")
        combo.addItem("Русский")
        combo.addItem("Английский")
        combo.addItem('Белорусский')
        combo.addItem("Испанский")
        combo.addItem("Итальянский")
        combo.addItem('Латинский')
        combo.addItem('Литовский')
        combo.addItem("Немецкий")
        combo.addItem("Нидерландский")
        combo.addItem('Норвежский')
        combo.addItem('Словенский')
        combo.addItem('Украинский')
        combo.addItem("Французский")

        combo.move(130, 182)

        combo.activated[str].connect(self.onActivated)

        combo1 = QComboBox(self)
        combo1.addItem("---")
        combo1.addItem("Русский")
        combo1.addItem("Английский")
        combo1.addItem('Белорусский')
        combo1.addItem("Испанский")
        combo1.addItem("Итальянский")
        combo1.addItem('Латинский')
        combo1.addItem('Литовский')
        combo1.addItem("Немецкий")
        combo1.addItem("Нидерландский")
        combo1.addItem('Норвежский')
        combo1.addItem('Словенский')
        combo1.addItem('Украинский')
        combo1.addItem("Французский")
        combo1.move(130, 207)

        combo1.activated[str].connect(self.onActivated1)

        combomenu = QComboBox(self)
        combomenu.addItem('Настройки')
        combomenu.addItem('Цвет Кнопок')
        combomenu.addItem('Шрифт')
        combomenu.move(10, 25)

        combomenu.activated[str].connect(self.onActivatedMenu)

        self.btn = QPushButton('Транслит', self)
        self.btn.resize(100, 50)
        self.btn.move(10, 130)

        self.btn1 = QPushButton('Раскладка\nс русского', self)
        self.btn1.resize(100, 50)
        self.btn1.move(115, 130)

        self.btn2 = QPushButton('Раскладка\nс английского', self)
        self.btn2.resize(120, 50)
        self.btn2.move(220, 130)

        self.btn3 = QPushButton('Перевeсти', self)
        self.btn3.resize(100, 50)
        self.btn3.move(10, 180)

        self.btn.clicked.connect(self.translit)

        self.btn1.clicked.connect(self.raskladka_from_rus)

        self.btn2.clicked.connect(self.raskladka_from_eng)

        self.btn3.clicked.connect(self.translate_yandex)

        self.text_input = QLineEdit(self)
        self.text_input.move(115, 10)
        self.text_input.resize(275, 100)

        self.name_label = QLabel(self)
        self.name_label.setText("Выберите тип работы с текстом:")
        self.name_label.move(10, 110)
        self.name_label.setFont(QtGui.QFont(None, 10, QtGui.QFont.Bold))

        self.name_label = QLabel(self)
        q = "Если текст, полученный в результате работы программы"
        e = "\nне отображается"
        w = ' полностью, то он запишется в .txt файл'
        self.name_label.setText(q + e + w)
        self.name_label.move(10, 260)
        self.name_label.setFont(QtGui.QFont(None, 10, QtGui.QFont.Bold))

        self.name_labelq = QLabel(self)
        self.name_labelq.setText("Здесь будет результат                      ")
        self.name_labelq.move(10, 240)
        self.name_labelq.setFont(QtGui.QFont("Times New Roman", 10))

        self.name_labelfrom = QLabel(self)
        self.name_labelfrom.setText("C")
        self.name_labelfrom.move(115, 185)

        self.name_labelto = QLabel(self)
        self.name_labelto.setText("Ha")
        self.name_labelto.move(115, 210)

        self.name_labelin = QLabel(self)
        self.name_labelin.setText("Введите ваш текст")
        self.name_labelin.move(10, 10)

        self.show()

    def onActivatedMenu(self, text):
        if text == 'Цвет Кнопок':
            color = QColorDialog.getColor()
            if color.isValid():
                self.btn1.setStyleSheet(
                    "background-color: {}".format(color.name())
                )
                self.btn2.setStyleSheet(
                    "background-color: {}".format(color.name())
                )
                self.btn3.setStyleSheet(
                    "background-color: {}".format(color.name())
                )
                self.btn.setStyleSheet(
                    "background-color: {}".format(color.name())
                )
        if text == 'Шрифт':
            self.btn1.setFont(QtGui.QFont("Times New Roman",
                                          11, QtGui.QFont.Bold))
            self.btn.setFont(QtGui.QFont("Times New Roman",
                                         11, QtGui.QFont.Bold))
            self.btn2.setFont(QtGui.QFont("Times New Roman",
                                          11, QtGui.QFont.Bold))
            self.btn3.setFont(QtGui.QFont("Times New Roman",
                                          11, QtGui.QFont.Bold))
            self.name_labelq.setFont(QtGui.QFont("Times New Roman", 11))

    def onActivated(self, text):
        global LANGUAGE1
        if text in DICT_WITH_LANGS:
            LANGUAGE1 = DICT_WITH_LANGS[text]

    def onActivated1(self, text):
        global LANGUAGE2
        if text in DICT_WITH_LANGS:
            LANGUAGE2 = DICT_WITH_LANGS[text]

    def translit(self):
        text = self.text_input.text()
        d = {"й": "j", "ц": "c", "у": "u", "к": "k", "е": "e", "н": "n",
             "г": "g", "ш": "sh", "щ": "shh", "з": "z", "х": "h", "ъ": "#",
             "ф": "f", "ы": "y", "в": "v", "а": "a", "п": "p", "р": "r",
             "о": "o", "л": "l", "д": "d", "ж": "zh", "э": "je", "я": "ya",
             "ч": "ch", "с": "s", "м": "m", "и": "i", "т": "t", "ь": "'",
             "б": "b", "ю": "ju", "ё": "jo",
             "Й": "J", "Ц": "C", "У": "U", "К": "K", "Е": "E", "Н": "N",
             "Г": "G", "Ш": "Sh", "Щ": "Shh", "З": "Z", "Х": "H",
             "Ф": "F", "Ы": "Y", "В": "V", "А": "A", "П": "P", "Р": "R",
             "О": "O", "Л": "L", "Д": "D", "Ж": "Zh", "Э": "Je", "Я": "Ya",
             "Ч": "Ch", "С": "S", "М": "M", "И": "I", "Т": "T",
             "Б": "B", "Ю": "Ju", "Ё": "Jo"}
        translit = []
        for symbol in text:
            if symbol in d:
                translit.append(d[symbol])
            else:
                translit.append(symbol)
        translit = ''.join(translit)
        with open('transliteration.txt', 'w') as q:
            q.write(translit)
        self.name_labelq.setText(translit)

    def raskladka_from_rus(self):
        text = self.text_input.text()
        d = {"й": "q", "ц": "w", "у": "e", "к": "r", "е": "t", "н": "y",
             "г": "u", "ш": "i", "щ": "o", "з": "p", "х": "[", "ъ": "]",
             "ф": "a", "ы": "s", "в": "d", "а": "f", "п": "g", "р": "h",
             "о": "j", "л": "k", "д": "l", "ж": ";", "э": "'", "я": "z",
             "ч": "x", "с": "c", "м": "v", "и": "b", "т": "n", "ь": "m",
             "б": ",", "ю": ".", "ё": "`",
             "Й": "Q", "Ц": "W", "У": "E", "К": "R", "Е": "T", "Н": "Y",
             "Г": "U", "Ш": "I", "Щ": "O", "З": "P", "Х": "{", 'Ъ': '}',
             "Ф": "A", "Ы": "S", "В": "D", "А": "F", "П": "G", "Р": "H",
             "О": "J", "Л": "K", "Д": "L", "Ж": ":", "Э": '"', "Я": "Z",
             "Ч": "X", "С": "C", "М": "V", "И": "B", "Т": "N",
             "Б": "<", "Ю": ">", "Ё": "~", 'Ь': 'M', '.': '/', ',': '?'}
        data = []
        for symbol in text:
            if symbol in d:
                data.append(d[symbol])
            else:
                data.append(symbol)
        data = ''.join(data)
        with open('raskladka.txt', 'w') as q:
            q.write(data)
        self.name_labelq.setText(data)

    def raskladka_from_eng(self):
        text = self.text_input.text()
        d = {"q": "й", "w": "ц", "e": "у", "r": "к", "t": "е", "y": "н",
             "u": "г", "i": "ш", "o": "щ", "p": "з", "[": "х", "]": "ъ",
             "a": "ф", "s": "ы", "d": "в", "f": "а", "g": "п", "h": "р",
             "j": "о", "k": "л", "l": "д", ";": "ж", "'": "э", "z": "я",
             "x": "ч", "c": "с", "v": "м", "b": "и", "n": "т", "m": "ь",
             ",": "б", ".": "ю", "`": "ё",
             "Q": "Й", "W": "Ц", "E": "У", "R": "К", "T": "Е", "Y": "Н",
             "U": "Г", "I": "Ш", "O": "Щ", "P": "З", "{": "Х", '}': 'Ъ',
             "A": "Ф", "S": "Ы", "D": "В", "F": "А", "G": "П", "H": "Р",
             "J": "О", "K": "Л", "L": "Д", ":": "Ж", '"': 'Э', "Z": "Я",
             "X": "Ч", "C": "С", "V": "М", "B": "И", "N": "Т",
             "<": "Б", ">": "Ю", "~": "Ё", 'M': 'Ь', '/': '.', '?': ','}
        data = []
        for symbol in text:
            if symbol in d:
                data.append(d[symbol])
            else:
                data.append(symbol)
        data = ''.join(data)
        with open('raskladka.txt', 'w') as q:
            q.write(data)
        self.name_labelq.setText(data)

    def translate_yandex(self):
        text = self.text_input.text()
        lang = LANGUAGE1 + '-' + LANGUAGE2
        r = requests.post(URL, data={'key': KEY, 'text': text, 'lang': lang})
        with open('translate.txt', 'w') as q:
            q.write(r.text[r.text.find('['):-1][2:-2])
        self.name_labelq.setText(r.text[r.text.find('['):-1][2:-2])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
