import random


def pick_lang():
	print('Pick a language. English or Italian.')
	lang = input()

	return lang


def get_word(lines):
	word = random.choice(lines)

	return word.upper()


def get_letter():
	print('Guess a letter!')
	letter = input()

	return letter


def newline():
	print('\n')


def print_shnuggles(shnuggles):
	for s in shnuggles:
		print(s, end=' ')
	newline()


def get_hint():
	pass


if __name__ == '__main__':

	newline()
	print("Welcome to my very own Word Guessing Game!\n\nAre you ready to play?")
	newline()
	lang = pick_lang()
	if lang == 'e':
		text = 'You\'re playing English-mode. Easy peasy! Now let\'s play!'
		with open('usa.txt', 'r') as f:
			lines = [f.replace('\n', "") for f in f.readlines()]
	else:
		text = 'You\'re playing Italian-mode. In bocca al lupo! Cominciamo!'
		with open('italiano.txt', 'r', encoding="utf8", errors='ignore') as f:
			lines = [f.replace('\n', "") for f in f.readlines()]

	newline()
	print(text)
	newline()
	
	word = get_word(lines)
	for_final = word
	guessed = '_' * len(word)
	word = list(word)
	guessed = list(guessed)
	lstGuessed = []
	
	shnuggles = ['❤' for i in range(10)]
	print(f'Hearts left:')
	print_shnuggles(shnuggles)
	letter = get_letter()
	while len(shnuggles) > 0:
		if letter.upper() in lstGuessed:
			letter = ''
			newline()
			print("You already guessed that letter, friend! Guess again.")
			shnuggles.append('❤')
			newline()
		elif letter.upper() in word:
			index = word.index(letter.upper())
			guessed[index] = letter.upper()
			word[index] = '_'
		else:
			print(''.join(guessed))
			if letter != '':
				lstGuessed.append(letter.upper())
			shnuggles.pop(-1)
			newline()
			print(f'Hearts left:')
			print_shnuggles(shnuggles)
			letter = get_letter()


		if '_' not in guessed:
			newline()
			print('ʕ•ᴥ•ʔ'*10)
			print(f"Huzzah! You've won the game! The word is {for_final}!")
			newline()
			exit()

	newline()
	print('Do you think you know what the word is? Hazzard a final guess.')
	final_guess = input()
	if final_guess.upper() == for_final:
		newline()
		print('ʕ•ᴥ•ʔ'*10)
		print(f'You\'ve won the game! The word was {for_final}!')
	else:
		newline()
		print('(._. )( ._.)'*5)
		print(f'Sadly, you have lost this game, but you are still a winner in my book!\nThe word was {for_final}.')
		newline()





	
