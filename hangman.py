import discord
from dotenv import load_dotenv
from os import getenv

hangman_games = {}

class HangmanGame:
	def __init__(self):
		self.word = "cheese"
		self.guesses = []

	def display(self):
		reply = "Your word is: `"
		for letter in self.word:
			reply += " _ "
		reply += "`"
		reply += """
```
┏━━━━━━╤━
┃┃
┃┃
┃┃
┃┃
┃┃
┻┻━━━━━━━━━━━━━
```
"""
		if len(self.guesses) != 0:
			reply += "You have guessed the following letters:\n"
			for letter in self.guesses:
				reply += letter
				reply += " "
		else:
			reply += "You have not guessed yet. Send a letter once you are ready."
		return reply


async def play_hangman(message):
	if message.author.id in hangman_games:
		await message.reply("You are already playing a hangman game. I don't have enough compute power to play two at once.", mention_author=True)
	else:
		game = HangmanGame()
		hangman_games[message.author.id] = game
		await message.reply(game.display(), mention_author=True)
		#create a new game
		# pick a word, any word
		# display stick hang thingy with underscores for the word
		
