############################################################
# ZIGZAG PATTERN GCODE GENERATOR
# Andrew Jajack
############################################################

f = open('zigzag.gcode','w')

f.write('M42 S0 P47\n')
f.write('M42 S255 P47\n')

f.write('G1 X50 Y100 F150000\n')

for y in range(100, 200, 2):
	f.write('M42 S0 P47\n')
	f.write('G1 X50 Y%d F15000\n' % (y)) #Return
	f.write('G4 P0\n')
	f.write('M42 S255 P47\n')
	f.write('G4 P100\n')
	f.write('G1 X150 Y%d F15000\n' % (y)) #Print
	f.write('G4 P0\n')

f.write('M42 S0 P47\n')
f.close()
