#!/usr/bin/env python3

import random

with open('words.ini', 'r') as f:
	words = [w.strip() for w in f.readlines()]

def setup(words):
	word = random.choice(words)
	shadow = '*'*len(word)
	lives = reversed(range(1, 5))
	main_loop(word, lives, shadow)
	
def main_loop(word, lives, shadow):
	while True:
		if '*' in shadow:
			print(shadow)
			guess = input('Gissa bokstav: ')
			check = check_for_character(guess, word)
			if not check:
				try:
					print('{} liv kvar'.format(next(lives)))
				except StopIteration:
					print('Game over.')
					break
			else:
				print('{} finns.'.format(guess))
				for i in check:
					shadow = shadow[:i] + guess + shadow[i+1:]
		else:
			print('Ordet var {}'.format(word))
			if input('Spela igen? (j)') == 'j':
				setup(words)
			else:
				break
	
def check_for_character(c, word):
	indices = []
	if c in word:
		for i, a in enumerate(word):
			if a == c:
				indices.append(i)
		return indices
	else:
		print('{} finns inte'.format(c))
		return False

if __name__ == '__main__':
	setup(words)