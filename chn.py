import pprint
import random

wins = {}
wins['wins'] = 0 
wins['losses'] = 0
wins['ties'] = 0


def newline():
	print('\n')


def outcome(d):
	print(f'Computer: {d["Computer"].title()}')
	print(f'{name}: {d[name].title()}')
	newline()


def print_winner(winner, d):
	newline()
	if winner == 'Computer':
		outcome(d)
		print(f'Whomp, whomp. {name} lost. Victory belongs to the Computer!')
		newline()
	else:
		outcome(d)
		print(f'Huzzah, huzzah! {name} wins! The singularity has not yet been reached.')
		newline()


def print_tie(d):
	newline()
	outcome(d)
	print(f'TIE! You both chose {d[name].title()}.')
	newline()


def game_play(wins):
	d = {}

	choice = input()
	d[name] = choice
	
	selections = ['chocolate', 'hug', 'norbert']
	
	computer_choice = random.choice(selections)
	d['Computer'] = computer_choice

	if d[name] == d['Computer']:
		print_tie(d)
		wins['ties'] += 1

	if 'chocolate' in d.values() and 'hug' in d.values():
		winner = list(d.keys())[list(d.values()).index('hug')]
		print_winner(winner, d)
		if winner == name:
			wins['wins'] += 1
		if winner == 'Computer':
			wins['losses'] += 1

	if 'norbert' in d.values() and 'chocolate' in d.values():
		winner = list(d.keys())[list(d.values()).index('chocolate')]		
		print_winner(winner, d)
		if winner == name:
			wins['wins'] += 1
		if winner == 'Computer':
			wins['losses'] += 1

	if 'norbert' in d.values() and 'hug' in d.values():
		winner = list(d.keys())[list(d.values()).index('norbert')]
		print_winner(winner, d)
		if winner == name:
			wins['wins'] += 1
		if winner == 'Computer':
			wins['losses'] += 1


	print('Play again? Y or n.')
	play = input()
	
	if play == 'y':
		newline()
		print('Your play.')
		game_play(wins)
	else:
		newline()
		print('Final tally:')
		pprint.pp(wins)
		newline()
		if wins['wins'] > wins['losses']:
			print(f'Great job, {name}!')
		elif wins['wins'] < wins['losses']:
			print(f'You need some skills, {name}! Better stay in school.')
		else:
			print(f'Sometimes life is about compromises.')
		newline()
		exit()


if __name__ == '__main__':

	newline()
	print('Hello! Welcome to Chocolate, Hug, Norbert! I am honored to be playing with you.\n\nWhat is your name?')
	name = input()	
	
	newline()
	print(f'Hello {name}! Would you like to read the rules? Y or n.')
	rules = input()
		
	newline()
	if rules == 'y':
		print('This game is just like Rock, Paper, Scissors, with a few differences. In this game:\n\n1) Hug beats Chocolate.\n\n2) Norbert beats Hug.\n\n3) And Chocolate, because chocolate kills dogs, beats Norbert.\n\nGot it? Good.')

	newline()
	print('Okay. You go first. Chocolate, Hug, or Norbert?')


	game_play(wins)



