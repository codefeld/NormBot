import discord
from dotenv import load_dotenv
from os import getenv

hangman_games = {}

class HangmanGame:
	def __init__(self):
		self.word = "cheese"
		self.guesses = []

	def add_guess(self, letter):
		self.guesses.append(letter.upper())

	def display(self):
		reply = "Your word is: `"
		for letter in self.word:
			if letter.upper() in self.guesses:
				reply += (" %s " % letter.lower())
			else:
				reply += " _ "
		reply += "`"
		reply += """
```
┏━━━━━━╤━
┃┃    😬
┃┃   /👕👍
┃┃    🩳
┃┃    / \\
┃┃   🦶 👢
┻┻━━━━━━━━━━━━━
```
"""
		if len(self.guesses) != 0:
			reply += "You have guessed the following letters:\n"
			for letter in self.guesses:
				reply += letter.lower()
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
		
async def guess_letter(message):
	if message.author.id in hangman_games:
		game = hangman_games[message.author.id]
		game.add_guess(message.content.split(" ")[1])
		await message.reply(game.display(), mention_author=True)
	else:
		await message.reply("You have somehow successfully broken the code.", mention_author=True)