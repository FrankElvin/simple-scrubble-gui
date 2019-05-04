﻿from PyQt4.QtGui import *
from PyQt4.QtCore import *

from letter.SelectLetter import SelectLetter
from selecter.LetterSelecter import LetterSelecter
from selecter.TurnInfo import TurnInfo

class SelectField(QWidget):

	def __init__(self, playerList, letterBag, playerField):
		super(SelectField, self).__init__()

		self.playerList = playerList
		self.startLetterNum = 7
		self.activePlayer = 0
		self.letterBag = letterBag
		self.playerField = playerField
		self.frameList = []
		self.turnInfoList = []
		self.letterSelecterList = []

		layout = QVBoxLayout()

		# initialize 1 frame per 1 player
		for player in self.playerList:

			frame = QFrame()
			ly = QVBoxLayout()

			letterList = []
			turnInfo = TurnInfo()

			for i in range(self.startLetterNum):
				letterList.append(
					SelectLetter(self.letterBag.take_from_bag().get_letter(), turnInfo)
				)

			btn = QPushButton(u"Завершить ход")
			btn.clicked.connect(self.nextTurn)

			ly.addWidget( QLabel(u"Ход игрока %s" %player.get_name()))
			letterSelecter = LetterSelecter(player, letterList)
			ly.addWidget(letterSelecter)
			ly.addStretch(20)
			ly.addWidget(turnInfo)
			ly.addWidget(btn)

			frame.setLayout(ly)
			self.frameList.append(frame)
			self.turnInfoList.append(turnInfo)
			self.letterSelecterList.append(letterSelecter)

		for frame in self.frameList:
			layout.addWidget(frame)

		# hide all frames but first
		for frame in self.frameList[1:]:
			frame.hide()

		self.setLayout(layout)
		print "Select field initialized"
	
	def getNextPlayer(self):
		if self.activePlayer == len(self.playerList) -1:
			self.activePlayer = 0
		else:
			self.activePlayer += 1
	
	def nextTurn(self):
		""" Switches the frame with player menu """
		self.frameList[self.activePlayer].hide()
		# add current points to the real Player instance
		self.playerList[self.activePlayer].increase_score(self.turnInfoList[self.activePlayer].plusScore)
		# actualize points on the Player screen basing on Player instance
		self.playerField.actualizePoints(self.activePlayer)
		# set turn info conditions to zeros
		self.turnInfoList[self.activePlayer].endTurn()

		# clear old letters from the letter list
		self.letterSelecterList[self.activePlayer].removeUsedLetters()

		# add new letters to players hand
		for i in range(self.turnInfoList[self.activePlayer].letterCounter.value()):
			self.letterSelecterList[self.activePlayer].addLetter(
				SelectLetter(
					self.letterBag.take_from_bag().get_letter(),
					self.turnInfoList[self.activePlayer]
				)
			)
		self.letterSelecterList[self.activePlayer].reloadLetters()

		self.getNextPlayer()
		self.frameList[self.activePlayer].show()


