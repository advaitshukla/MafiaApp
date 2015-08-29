"""Basic user for the mafia app"""
import sys
from enum import Enum

class user(object):
	Types = Enum('Mafioso', 'Innocent')

	"""docstring for user"""
	def __init__(self, name, type):
		super(user, self).__init__()
		self.name = name
		self.living = true
		self.voteCount = 0
		self.type = type


	"""See if the user is alive"""
	def isAlive(self):
		return self.living
		
	"""Get the user name"""
	def getName(self):
		return self.name

	"""get the vote count"""
	def getVoteCount(self):
		return self.voteCount

	"""clear the vote count"""
	def clearVoteCount(self):
		self.voteCount = 0
		return True
