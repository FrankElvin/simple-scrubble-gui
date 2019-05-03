﻿import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from random import randint

from widgets.GameField import GameField
from widgets.PlayerField import PlayerField
from widgets.SelectField import SelectField

if __name__ == '__main__':

	app = QApplication(sys.argv)

	# Build the window widget
	mainWindow = QWidget()
	mainWindow.setWindowTitle(u"Скромный интерфейс Scrubble на русском")
	
	# Add a label with tooltip
	#label = QLabel(u"Буквы ниже")
	#label.setToolTip("This is a <b>QLabel</b> widget with Tooltip")
	#label.resize(label.sizeHint())
	#label.move(80, 50)
	#
	## try layout
	layout = QHBoxLayout()
	#
	#letters = [
	#u"А", u"Б", u"В", u"Г", u"Д", u"Е",
	#u"Ё", u"Ж", u"З", u"И", u"Й", u"К",
	#u"Л", u"М", u"Н", u"О", u"П", u"Р",
	#u"С", u"Т", u"У", u"Ф", u"Х", u"Ц",
	#u"Ч", u"Ш", u"Щ", u"Ъ", u"Ы", u"Ь",
	#u"Э", u"Ю", u"Я", u""
	#]
	#
	#for i in range(0,14):
	#for j in range(0,14):
	#layout.addWidget(
	#LetterButton(letters[randint(1,len(letters)-1)]),
	#i, j
	#)
	playerField = PlayerField(['Player1', 'Player2'])
	gameField = GameField()
	selectField = SelectField(['Player1', 'Player2'])

	layout.addWidget(playerField)
	layout.addWidget(gameField)
	layout.addWidget(selectField)
	mainWindow.setLayout(layout)

	# Show window and run
	mainWindow.show()
	app.exec_()
