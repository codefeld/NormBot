import discord
from dotenv import load_dotenv
from os import getenv
import random
from hangman import guess_letter, play_hangman

print("Booting up")

load_dotenv()

class MyClient(discord.Client):
	async def on_ready(self):
		print('Logged in as')
		print(self.user.name)
		print(self.user.id)
		print('------')

	async def on_message(self, message):
		# we do not want the bot to reply to itself
		if message.author.id == self.user.id:
			return

		for mention in message.mentions:
			if self.user.id == mention.id:
				await parse_message(message)
			else:
				print("????")
				print(message)

async def parse_message(message):
	if "favorite color" in message.content.lower():
		await message.reply(favorite_color(), mention_author=True)
	elif "favourite colour" in message.content.lower():
		await message.reply(favorite_color(), mention_author=True)
	elif "favorite colour" in message.content.lower():
		await message.reply(favorite_color(), mention_author=True)
	elif "favourite color" in message.content.lower():
		await message.reply(favorite_color(), mention_author=True)
	elif len(message.content.split(" ")[1]) == 1:
		#todo: also check if game is started
		await guess_letter(message)
	elif "hangman" in message.content.lower():
		await play_hangman(message)
	else:
		await message.reply("Is this a trick question?", mention_author=True)

def favorite_color():
	colors = ["Blue",'Red',"Green","Brown","Fuchsia","Bleu cheese","Baby blue","Maroon","Lavender","Gray","Metal","Black. Oh yeah; that's not a color.","Beige","Tan", "Orange", "Yellow", "Amber", "I like all colors. In other words, I like white.", "Blueberry", "Blackberry. Wait; black isn't a color!", "Blue...wait no, green!"]
	color = random.choice(colors)
	return color

client = MyClient()

client.run(getenv("TOKEN"))