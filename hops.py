#	This will eventually hold all of the hop definitions and functions or methods or whatever python calls them
#
#
#	The basic hop class should be fed hop, lb, oz, AA, time (minutes), and form
#		Default to generic,0,1,10,0,pellet
#
#		-update() methods should allow the user to select hop type, lb, oz, AA, time, and form
#			the user should be able to name their own hop type (and fill in the rest of the data)
#		-get() methods should pull AA from a database/xml for a given hop
#		-a weight conversion method should convert lb and oz to a common unit (which ever works best for calculations)
#
#		the class should return return a (single unit) weight value, AA, time (minutes), form, IBU and AAU
#
#		an add hop function should create an instance of Hop, count and keep track of them, and do aggregate IBU calculations
#
#		hop attributes will be:
#			displayed: (multi-unit) weight, AA, time (minutes) and form
#				(multi-unit) weight, time (minutes) and form will feed the brew day tasks (this is not thought out yet)
#			fed to aggregate IBU calculations
#			AAU converter to plan for audibles
#			probably other things?


import settings
import math


class Hop(object):
	
	count = 0
	totalIBU = 0

	def __init__(self, type= 'generic', lb = 0, oz = 1, aa = 10, min = 0, form = 'pellet', og = 1.05):
		
		Hop.count += 1
			#This might need to live outside of the Hop class at some point (in a Recipe class 
			#that aggregates hops and stuff (and does the total IBU calculations?))
		
		self.type = type
		self.lb = lb
		self.oz = oz
		self.weight = (lb * 16) + oz
		self.aa = aa
		self.minutes = min
		self.form = form
		self.og = og
		
		volume = settings.FinalVolume

		self.aau = self.aa * self.weight
		#self.tinsethIBU = (1.65 * 0.000125 **(self.og - 1)) * ((1 - math.exp(-0.04 * self.minutes)) / 4.15) * (((self.aa / 100) * self.weight * 7490) / volume)
		
#test main
#hop = Hop(min=60)
#
#print('type:', hop.type)
#print('weight:', hop.weight, 'oz')
#print('AAUs:', hop.aau)
#print('IBU:', hop.tinsethIBU)
#print('count:', hop.count)
#print('count:', Hop.count)
#input("\nExit")
