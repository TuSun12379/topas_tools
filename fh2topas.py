#!/usr/bin/env python

import re
pat = re.compile('[a-zA-Z]+')

import sys
args = sys.argv[1:]

moltotal = 1
if args:
	moltotal = int(args[0])
molnum = 1

fin = open('/Users/smeets/Desktop/output.fh','r')


lines = fin.readlines()

molnum = 1
while molnum <= moltotal:
	if moltotal == 1:
		molnum = ''

	number = None
	n = 0
	d = {}
	all_atoms = []
	
	print '      rigid'
	
	for line in lines:
		inp = line.split()
	
		if not inp:
			continue
		if not number:
			number = int(inp[0])
			continue
		n += 1
	
		print '         z_matrix ',
	
	
		if n > 0:
			tpe = inp[0]
			
			atom = '{}{}'.format(tpe,n)
			d[str(n)] = atom
			all_atoms.append(atom)
			
			scatterer = re.findall(pat,atom)[0]
			atom = atom.replace(scatterer,scatterer+str(molnum))
			print '{:6s}'.format(atom),
	
		if n > 1:
			bonded_with,bond = inp[1:3]
			bonded_with = d[bonded_with]
			scatterer = re.findall(pat,bonded_with)[0]
			bonded_with = bonded_with.replace(scatterer,scatterer+str(molnum))
			print '{:6s} {:7s}'.format(bonded_with,bond),
		if n > 2:
			angle_with,angle = inp[3:5]
			angle_with = d[angle_with]
			scatterer = re.findall(pat,angle_with)[0]
			angle_with = angle_with.replace(scatterer,scatterer+str(molnum))
			print '{:6s} {:7s}'.format(angle_with,angle),
		if n > 3:
			torsion_with,torsion = inp[5:7]
			torsion_with = d[torsion_with]
			scatterer = re.findall(pat,torsion_with)[0]
			torsion_with = torsion_with.replace(scatterer,scatterer+str(molnum))
			print '{:6s} {:>7s}'.format(torsion_with,torsion),
	
		print
	
	print """
         Rotate_about_axies(@ 0.0 randomize_on_errors,
                            @ 0.0 randomize_on_errors, 
                            @ 0.0 randomize_on_errors)
         Translate(         @ 0.0 randomize_on_errors,
                            @ 0.0 randomize_on_errors,
	                        @ 0.0 randomize_on_errors)
	"""
	

	if molnum == '':
		break
	else:
		molnum += 1


import re
pat = re.compile('[a-zA-Z]+')

molnum = 1
while molnum <= moltotal:
	if moltotal == 1:
		molstr = ''
	else:
		molstr = str(molnum)
	print
	print "      prm !occ{} 0.5 min 0.0 max  1.0".format(molnum)
	print "      prm !beq{} 3.0 min 1.0 max 10.0".format(molnum)
	print

	for atom in all_atoms:
		scatterer = re.findall(pat,atom)[0]
		atom = atom.replace(scatterer,scatterer+molstr)
		print '      site {:6s} x 0.0 y 0.0 z 0.0 occ {:2s} =occ{}; beq =beq{};'.format(atom,scatterer,molnum,molnum)
	molnum += 1






