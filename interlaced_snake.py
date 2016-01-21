############################################################
# INTERLACED SNAKE PATTERN GCODE GENERATOR
# Andrew Jajack
############################################################

############################################################
# CONFIGURATION
############################################################
delay    = 5000   # Delay at start for nozzle (milliseconds)
length_x = 90     # Length in x-dir (mm)
length_y = 90     # Length in y-dir (mm)
delta    = 2      # Space between lines (mm)
x_int    = 5      # Initial x (default: 0)
y_int    = 5      # Initial y (default: 0)
speed    = 1900   # mm/min
############################################################

f = open('interlaced_snake.gcode','w')

f.write('G0 X0 Y0\n')       # Go home
f.write('G4 P0\n')          # Block
f.write('M42 S0 P47\n')     # Disable syringe press
f.write('M42 S255 P47\n')   # Enable syringe press
f.write('G4 P%f\n' % delay) # Delay to clear line

# Initialize start points
x = x_int
y = y_int

f.write('G1 X%f Y%f F%f\n' % (x, y, speed)) # Goto start

# Pass 1: up
while y - y_int < length_y:
	f.write('G1 X%f Y%f F%f\n' % (x + length_x, y,               speed)) #RIGHT
	f.write('G1 X%f Y%f F%f\n' % (x + length_x, y + delta,       speed)) #UP
	f.write('G1 X%f Y%f F%f\n' % (x,            y + delta,       speed)) #LEFT
	f.write('G1 X%f Y%f F%f\n' % (x,            y + (2 * delta), speed)) #UP
	y = y + (2 * delta)

f.write('G1 X%f Y%f F%f\n'     % (x + length_x, y,               speed)) #RIGHT
offset = 1
y = y - offset
f.write('G1 X%f Y%f F%f\n'     % (x + length_x, y,               speed)) #DOWN (OFFSET)

#Pass 2: down
while y > y_int:
	f.write('G1 X%f Y%f F%f\n' % (x,            y,               speed)) #LEFT
	f.write('G1 X%f Y%f F%f\n' % (x,            y - delta,       speed)) #DOWN
	f.write('G1 X%f Y%f F%f\n' % (x + length_x, y - delta,       speed)) #RIGHT
	f.write('G1 X%f Y%f F%f\n' % (x + length_x, y - (2 * delta), speed)) #DOWN
	y = y - (2 * delta)

#Pass 3: up
f.write('G1 X%f Y%f F%f\n'     % (x,            y,               speed)) #LEFT
offset = 0.5
y = y + offset
f.write('G1 X%f Y%f F%f\n'     % (x,            y,               speed)) #DOWN (OFFSET)

while (y + delta) - y_int < length_y:
	f.write('G1 X%f Y%f F%f\n' % (x + length_x, y,               speed)) #RIGHT
	f.write('G1 X%f Y%f F%f\n' % (x + length_x, y + delta,       speed)) #UP
	f.write('G1 X%f Y%f F%f\n' % (x,            y + delta,       speed)) #LEFT
	f.write('G1 X%f Y%f F%f\n' % (x,            y + (2 * delta), speed)) #UP
	y = y + (2 * delta)

f.write('G1 X%f Y%f F%f\n'     % (x + length_x, y,               speed)) #RIGHT
offset = 1
y = y - offset
f.write('G1 X%f Y%f F%f\n'     % (x + length_x, y,               speed)) #DOWN (OFFSET)

#Pass 4: down
while y > y_int:
	f.write('G1 X%f Y%f F%f\n' % (x,            y,               speed)) #LEFT
	f.write('G1 X%f Y%f F%f\n' % (x,            y - delta,       speed)) #DOWN
	f.write('G1 X%f Y%f F%f\n' % (x + length_x, y - delta,       speed)) #RIGHT
	f.write('G1 X%f Y%f F%f\n' % (x + length_x, y - (2 * delta), speed)) #DOWN
	y = y - (2 * delta)

f.write('G4 P0\n')      # Block
f.write('M42 S0 P47\n') # Disable syringe press

f.close()
