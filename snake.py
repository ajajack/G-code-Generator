############################################################
# SNAKE PATTERN GCODE GENERATOR
# Andrew Jajack
############################################################

############################################################
# CONFIGURATION
############################################################
delay    = 5000   # Delay at start for nozzle (milliseconds)
length_x = 80     # Length in x-dir (mm)
length_y = 80     # Length in y-dir (mm)
delta    = 0.5    # Space between lines (mm)
x_int    = 0      # Initial x (default: 0)
y_int    = 0      # Initial y (default: 0)
speed    = 4100   # mm/min
############################################################

f = open('snake.gcode','w')

f.write('G0 X0 Y0\n')       # Go home
f.write('G4 P0\n')          # Block
f.write('M42 S0 P47\n')     # Disable syringe press
f.write('M42 S255 P47\n')   # Enable syringe press
f.write('G4 P%f\n' % delay) # Delay to clear line

# Initialize start points
x = x_int
y = y_int

f.write('G1 X%f Y%f F%f\n' % (x, y, speed)) # Goto start

while y - y_int < length_y:
	f.write('G1 X%f Y%f F%f\n' % (x + length_x, y,               speed)) #RIGHT
	f.write('G1 X%f Y%f F%f\n' % (x + length_x, y + delta,       speed)) #UP
	f.write('G1 X%f Y%f F%f\n' % (x,            y + delta,       speed)) #LEFT
	f.write('G1 X%f Y%f F%f\n' % (x,            y + (2 * delta), speed)) #UP
	y = y + (2 * delta)

f.write('G4 P0\n')      # Block
f.write('M42 S0 P47\n') # Disable syringe press

f.close()
