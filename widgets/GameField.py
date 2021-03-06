from PyQt4.QtGui import *
from PyQt4.QtCore import *

from .letter.GameLetter import GameLetter
from .BadWordDialog import BadWordDialog

class GameField(QWidget):

	def __init__(self, letterBag, dbChecker):
		super(GameField, self).__init__()

		self.letterBag = letterBag
		self.dbChecker = dbChecker
		self.currentWord = ""
		gameLayout = QGridLayout()

		TRIPLE_WORD_SCORE = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
		DOUBLE_WORD_SCORE = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10))
		TRIPLE_LETTER_SCORE = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
		DOUBLE_LETTER_SCORE = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11), (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))

		self.letterMatrix = []
		letterString = []


		for i in range(15):
			letterString = []
			for j in range(15):
				if (i,j) in TRIPLE_WORD_SCORE: multiplier = {"type": "word", "number": 3}
				elif (i,j) in DOUBLE_WORD_SCORE: multiplier = {"type": "word", "number": 2}
				elif (i,j) in TRIPLE_LETTER_SCORE: multiplier = {"type": "letter", "number": 3}
				elif (i,j) in DOUBLE_LETTER_SCORE: multiplier = {"type": "letter", "number": 2}
				else: multiplier = {"type": "none", "number": 1}

				letter = GameLetter("", i, j, multiplier)
				if i == 7 and j == 7:
					letter.setAcceptDrops(True)
				
				gameLayout.addWidget(letter, i, j)
				letterString.append(letter)
			self.letterMatrix.append(letterString)

		self.setLayout(gameLayout)

	def getMatrixColumn(self, i):
		return [row[i] for row in self.letterMatrix]
	
	def confirmActions(self):
		self.currentWord = ""
		for i in self.letterMatrix:
			for j in i:
				if j.filled: j.openNearby()

		for row in self.letterMatrix:
			# to calculate points later correctly
			for letter in row: letter.filledNow = False
	
	def checkWordInDb(self):
		if self.currentWord == "": 
			return True

		if not self.dbChecker.checkWordInDb(self.currentWord):
			badWordDialog = BadWordDialog(self.currentWord)
			retval = badWordDialog.exec_()

		return self.dbChecker.checkWordInDb(self.currentWord)
	
	def revertActions(self):
		self.currentWord = ""
		for row in self.letterMatrix:
			for letter in row:
				letter.setAcceptDrops(False)
				if letter.filledNow:
					letter.erase()	

		for row in self.letterMatrix:
			for letter in row:
				if letter.filled:
					letter.openNearby()


