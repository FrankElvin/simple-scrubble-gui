﻿import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from widgets.MainWindow import MainWindow
from widgets.StartDialogs import PlayerNumberDialog, PlayerNameDialog

from impl.Bag import Bag
from impl.Player import Player

def showStartDialog():
	numberDialog = PlayerNumberDialog()
	numberDialog.exec_()
	if not numberDialog.result():
		return []

	nameDialog = PlayerNameDialog(numberDialog.playerCounter.value())
	nameDialog.exec_()
	if not nameDialog.result():
		return []

	players = []
	for player in nameDialog.players:
		#players.append(player.input.text())
		players.append(
			Player(player.input.text())
		)
	return players


if __name__ == '__main__':

	app = QApplication(sys.argv)
	
	# get the initial data from dialogs
	playerList = showStartDialog()
	if playerList:

		# initialize the bag
		letterBag = Bag()

		# Build the window widget
		mainWindow = MainWindow(playerList, letterBag)

		# Show window and run
		mainWindow.show()
		app.exec_()
