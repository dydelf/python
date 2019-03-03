alien_1 = {'color': 'green', 'points': '5'}
alien_2 = {'color': 'yellow', 'points': '10'}
alien_3 = {'color': 'red', 'points': '15'}

aliens = [alien_1, alien_2, alien_3]
print(aliens)

for alien in aliens:
    print(alien)

#creating a list of aliens automatically
aliens_1 = []

#make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': '5', 'speed': 'slow'}
    aliens_1.append(new_alien)

#changing the first 3 aliens
for alien in aliens_1[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = '10'
        alien['speed'] = 'medium'

#show the first 5 aliens
for alien in aliens_1[:5]:
    print(alien)
print("...")

#show how many aliens you have created
print("total number of aliens: " + str(len(aliens_1)))
