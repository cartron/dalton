#	This will eventually hold all of the grain definitions and functions or methods or whatever python calls them
#
#
#	The basic hop class should be fed grain, lb, oz, ppg, degreesL, sugar type, and use
#		Default to generic,1,0,1.025,1,grain, other
#
#		-update() methods should allow the user to select grain, lb, oz, ppg, degreesL, sugar type, and method
#			the user should be able to name their own grain type (and fill in the rest of the data)
#		-get() methods should pull attributes from a database/xml for a given grain
#		-a weight conversion method should convert lb and oz to a common unit (which ever works best for calculations)
#		-an extract calculation method should pull weight, ppg, efficiency, and volume in order to calculate og per grain
#			perhaps getOG() and getVolume() methods should facilitate this
#		-color calculation should return color based on some stuff
#		-a points to (something--OG?) calculation should convert ppg to the proper display (50 ppg to 1.050)
#
#		other stuff will happen


class Grain(object):
#The basic class that all fermentables fall under

	count = 0
	
	def __init__(self, type= 'generic', lb = 1, oz = 0, ppg = 25, degreesL = 1, sugarType="grain", use="mashed"):
	
		Grain.count += 1
			#This might need to live outside of the Grain class at some point (in a Recipe class 
			#that aggregates grains and stuff (and does the total OG/color calculations?))
		
		#establish the main attributes
		self.type = type
		self.lb = lb
		self.oz = oz
		self.weight = (lb * 16) + oz
		self.pounds = self.weight / 16
		self.ppg = ppg
		self.degreesL = degreesL
		self.sugarType = sugarType
		self.use = use
		
	def calculatePoints(self, volume, efficiency):
		#returns the points added from a single fermentable
		#this might not work for extract--look into that
		pts = ((self.ppg * self.pounds) / volume) * efficiency
		return pts
			#I'm not certain that this is correct--might have to do some Qbrew testing

	def returnOG(self, volume, efficiency):
		#return the gravity contribution of a single fermentable addition
		vol = volume
		efficient = efficiency
		pt = self.calculatePoints(vol, efficient)
		OG = 1 + (pt / 1000)
		return OG
	
	def calculateColor(self):
		#calculates the color contriution of a single fermentable addition
		#the color from all additions should be divided by the total volume
			#and fed through a color estimating formula (initially just Morey)
		#this might not be the most effective way to do things
		color = self.pounds * self.degreesL
		return color
		
		
		
#test main
#grain = Grain(ppg=30)
#grainlb = Grain(oz=8)
#points = grain.calculatePoints(5, 0.75)
#og = grain.returnOG(5, 0.75)
#color = grain.calculateColor()

#print('type:', grain.type)
#print('weight:', grain.weight, 'oz')
#print('weight:', grainlb.pounds, 'lb')
#print('points:', points)
#print('OG:', og)
#print('count:', grain.count)
#print('Count:', Grain.count)
#print('Color:',color)
#print('Color:',grainlb.calculateColor())
#input("\nExit")
