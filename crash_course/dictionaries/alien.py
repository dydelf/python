alien_0 = {'color': 'green'}
print("the alien is " + alien_0['color'])

alien_0['color'] = 'yellow'
print("the alien is " + alien_0['color'] + " now")

alien_1 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x position: " + str(alien_1['x_position']))

#move alien to the right
#determine how far to move alien based on its current speed
if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    #this is a fast alien
    x_increment = 3

#the new position is the old position with the increment
alien_1['x_position'] = alien_1['x_position'] + x_increment

print("new position: " + str(alien_1['x_position']))


