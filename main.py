#!/usr/bin/env python3

import random
import json

heart = u'\u2665' # Unicode för hjärtsymbol

class HangmanGame:
	def __init__(self):
		print('*** HÄNGA GUBBEN ***')
		with open('config.json', 'r') as f:
			self.cfg = json.load(f)
		with open('words.ini', 'r') as f:
			self.words = [w.strip() for w in f.readlines()]
		with open('scores.json', 'r') as f:
			self.scores = json.load(f)
		self.lives = reversed(range(1, int(self.cfg['lives'])))
		self.player_name = input('Namn: ')
		self.game_round = 0
	
	def get_action(self):
		action = input('(s)pela | (i)nställningar | (h)ighscores | (a)vsluta\n')
		self.actionhandler(action)()

	def actionhandler(self, action):
		actions = {
			's': self.main_loop,
			'i': self.edit_config,
			'h': self.show_highscores,
			'a': self.quit_game,
			'': self.get_action
		}

		return actions.get(action)

	def main_loop(self):
		self.word = random.choice(self.words)
		shadow = '*'*len(self.word)
		self.game_round = self.game_round + 1
		print('Runda {}'.format(self.game_round))
		while '*' in shadow:
			print(shadow)
			self.guess = input('Gissa bokstav: ')
			check = self.check_for_character()
			if not check:
				try:
					print('{} liv kvar'.format(heart*next(self.lives)))
				except StopIteration:
					print(f'Game over.\nOrdet var {self.word}.\n')
					self.save_scores()
			else:
				print('{} finns.'.format(self.guess))
				for i in check:
					shadow = shadow[:i] + self.guess + shadow[i+1:]

		self.play_again()
		
	def play_again(self):
		if input('Ordet var {}.\nSpela igen? (j) '.format(self.word)) == 'j':
			self.main_loop()
		else:
			self.save_scores()

	def check_for_character(self):
		indices = []
		if self.guess in self.word:
			for i, a in enumerate(self.word):
				if a == self.guess:
					indices.append(i)
			return indices
		else:
			print('{} finns inte'.format(self.guess))
			return False

	def save_scores(self):	
		self.scores.append({'player_name': self.player_name, 'highest_round': self.game_round, 'lives': self.cfg['lives'], 'difficulty': self.cfg['difficulty']})
			
		with open('scores.json', 'w') as f:
			json.dump(self.scores, f)
		print('Sparade resultat.')
		self.get_action()

	def edit_config(self):
		print('Skriv inställning värde')
		for k, v in self.cfg.items():
			print('{}: {}'.format(k, v))
		c = input().split(' ')
		try:
			self.cfg[c[0]] = c[1]
			if input('Ändrade {} till {}. \nSpara ändringar? (j/N)'.format(c[0], c[1])) == 'j':
				with open('config.json', 'w') as f:
					json.dump(self.cfg, f)
				print('Sparade ändringarna.')
			else:
				print('Okej, ändringarna gäller bara för den här gången.')
		except IndexError:
			print('Avbrutet.')
		self.get_action()

	def show_highscores(self):
		print('Namn\tHögsta runda\tAntal liv\tSvårighetsgrad')
		for r in self.scores:
			print('{}\t\t{}\t\t{}\t\t{}'.format(r['player_name'], r['highest_round'], r['lives'], r['difficulty']))
		self.get_action()

	def quit_game(self):
		print('Tack för att du spelade!')
		exit()

if __name__ == '__main__':
	game = HangmanGame()
	game.get_action()