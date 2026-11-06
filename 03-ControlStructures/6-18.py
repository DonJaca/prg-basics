def yes_no(question):
    return input(question + ' (y/n): ').lower() == 'y'
interested = yes_no('Are you interested in computer science?')
games = yes_no('Do you like playing computer games?')
instagram = yes_no('Do you have an Instagram account?')
print('\nSURVEY RESULTS')
print(f'Interested in computer science: {"Yes" if interested else "No"}')
print(f'Playing computer games: {"Yes" if games else "No"}')
print(f'Has an Instagram account: {"Yes" if instagram else "No"}')
