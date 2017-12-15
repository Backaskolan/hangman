#!/usr/bin/env python3

import random

with open('words.ini', 'r') as f:
	words = [w.strip() for w in f.readlines()]
# Hämta alla ord i filen words.ini och stoppa in dem i listan words

heart = u'\u2665' 
# Unicode för hjärtsymbol

def setup(words):
	word = random.choice(words)
	# Plocka ett slumpmässigt ord ur words
	shadow = '*'*len(word)
	# Skriv så många * som det finns bokstäver i word
	lives = reversed(range(1, 5))
	# Räkna ned från 5
	main_loop(word, lives, shadow)
	# Kör funktionen main_loop()
	
def main_loop(word, lives, shadow):
	while '*' in shadow:
	# Så länge det finns * kvar i shadow
		print(shadow)
		# Skriv ut shadow
		guess = input('Gissa bokstav: ')
		# Innehållet i variabeln guess blir spelarens gissning
		check = check_for_character(guess, word)
		# check blir resultatet av funktionen check_for_character(), det vill säga False om gissningen är fel, annars en lista med var i strängen gissningen finns.
		if not check:
		# Om check är False
			try:
			# Försök skriva ut hur många liv som är kvar
				print('{} liv kvar'.format(heart*next(lives)))
				# next() räknar ner liven från 5 till 1
			except StopIteration:
			# Om det inte finns några liv kvar
				print('Game over.\n')
				# \n skriver en ny rad
				break
				# Spelet slut, hoppa ut ur loopen
		else:
		# Om check inte är False är det en lista med index som talar om var i strängen gissningen finns
			print('{} finns.'.format(guess))
			# Skriv att gissningen finns
			for i in check:
			# För varje index i check
				shadow = shadow[:i] + guess + shadow[i+1:]
				# Byt ut * mot den gissade bokstaven i shadow
	
	# Spela igen?
	if input('Ordet var {}.\nSpela igen? (j) '.format(word)) == 'j':
		setup(words)
	else:
		exit()

def check_for_character(guess, word):
	indices = []
	# Gör en tom lista att samla index i
	if guess in word:
	# Om gissningen guess finns i strängen word
		for i, a in enumerate(word):
		# Loopa igenom strängen word. enumerate() gör att Python räknar varje runda av loopen i variabeln i. a är bokstaven i just den här rundan (första bokstaven i första rundan, och så vidare).	
			if a == guess:
			# Om den gissade bokstaven finns på den här platsen i strängen
				indices.append(i)
				# Lägg till bokstavens index i listan med index
		return indices
		# Ge tillbaka listan med index
	else:
	# Om gissningen inte finns i strängen word
		print('{} finns inte'.format(guess))
		return False
		# Ge tillbaka False, vilket vi använder i main_loop() för att kolla om gissningen stämmer

if __name__ == '__main__':
	setup(words)