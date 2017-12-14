import random

with open('words.ini', 'r') as f:
    words = [w.strip() for w in f.readlines()]

word = random.choice(words)
shadow = '*'*len(word)

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

lives = reversed(range(1, 5))

while '*' in shadow:
    print(shadow)
    guess = input('Gissa bokstav: ')
    check = check_for_character(guess, word) 
    if not check:
        try:
            print('{} liv kvar'.format(next(lives)))
        except StopIteration:
            print('Game over')
            break
    else:
        print('{} finns.'.format(guess))
        for i in check:
            shadow = shadow[:i] + guess + shadow[i+1:]

print('\nOrdet var {}'.format(word))