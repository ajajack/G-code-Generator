############################################################
# SPIRAL PATTERN GCODE GENERATOR
# Andrew Jajack
############################################################

f = open('spiral.gcode','w')

x = 50
y = 100
length = 150
delta = 3
speed = 15000
f.write('G1 X%f Y%f F10000\n' % (x, y))

while length > 0:
	f.write('G1 X%f Y%f F%f\n' % (x,          y + length, speed)) #UP
	f.write('G1 X%f Y%f F%f\n' % (x + length, y + length, speed)) #RIGHT
	f.write('G1 X%f Y%f F%f\n' % (x + length, y + delta,  speed)) #DOWN
	f.write('G1 X%f Y%f F%f\n' % (x + delta,  y + delta,  speed)) #LEFT
	length = length - (2 * delta)
	x = x + delta
	y = y + delta

f.close()
