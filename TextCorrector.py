import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QLCDNumber, QLineEdit, QColorDialog
import PyQt5.QtGui as QtGui
from PyQt5 import QtCore, QIcon
import requests

TRANSLATE = '' 
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
KEY = 'trnsl.1.1.20160119T035517Z.50c6906978ef1961.08d0c5ada49017ed764c042723895ffab867be7a' 
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.setGeometry(1000, 1000, 1000, 1000)
        self.setWindowTitle('Корректировщик текста')
        
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        self.btn = QPushButton('Транслит', self)
        self.btn.resize(100, 50)
        self.btn.move(10, 130)

        self.btn1 = QPushButton('Раскладка\nс русского', self)
        self.btn1.resize(100, 50)
        self.btn1.move(115, 130)

        self.btn2 = QPushButton('Раскладка\nс английского', self)
        self.btn2.resize(100, 50)
        self.btn2.move(220, 130)

        self.btn3 = QPushButton('Перевод (rus-eng\nen-rus', self)
        self.btn3.resize(100, 50)
        self.btn3.move(325, 130)

        self.btn4 = QPushButton('Цвет кнопок', self)
        self.btn4.resize(100, 50)
        self.btn4.move(10, 180)

        self.btn.clicked.connect(self.translit)

        self.btn1.clicked.connect(self.raskladka_from_rus)

        self.btn2.clicked.connect(self.raskladka_from_eng)

        self.btn3.clicked.connect(self.translate_yandex)

        self.btn4.clicked.connect(self.run)

        self.text_input = QLineEdit(self)
        self.text_input.move(110, 10)
        self.text_input.resize(275, 100)

        self.name_label = QLabel(self)
        self.name_label.setText("Выберите тип работы с текстом:")
        self.name_label.move(10, 110)

        self.name_label = QLabel(self)
        self.name_label.setText("Введите ваш текст")
        self.name_label.move(10, 10)

        self.show()

    def run(self):
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
            self.btn4.setStyleSheet(
                "background-color: {}".format(color.name())
            )
            self.btn.setStyleSheet(
                "background-color: {}".format(color.name())
            )

 
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
        for j in text:
            if j in d:
                translit.append(d[j])
            else:
                translit.append(j)
        translit = ''.join(translit)
        with open('transliteration.txt', 'w') as q:
            q.write(translit)

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
        translit = []
        for i in text:
            if i in d:
                translit.append(d[i])
            else:
                translit.append(i)
        translit = ''.join(translit)
        with open('raskladka_from_rus.txt', 'w') as q:
            q.write(translit)
        
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
        translit = []
        for i in text:
            if i in d:
                translit.append(d[i])
            else:
                translit.append(i)
        translit = ''.join(translit)
        with open('raskladka_from_eng.txt', 'w') as q:
            q.write(translit)
        print('')

    def ru_en(t):
        en = [chr(i) for i in range(65, 123)]
        for i in t[:5]:
            if i in en:
                return 'en-ru'
            else:
                return 'ru-en'

    def translate_yandex(self):
        text = self.text_input.text()
        lang = ru_en(text)
        r = requests.post(URL, data={'key': KEY, 'text': TEXT, 'lang': lang})
        with open('translate.txt', 'w') as q:
            q.write(r.text[r.text.find('['):-1][2:-2])
        
           
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

