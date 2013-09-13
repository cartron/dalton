#	This will eventually perform a few calculations and hold the bulk of the recipe data
#
#	-Settings should be imported from a CONFIG type of module
#		-in addition to settings things like recipe name and author should probably
#			be pulled
#
#	Other thoughts:
#	-this might be a good place to compare to style guidelines
#	-as an "other" group is developed, it should probably also be included to keep
#		data in the same place(it probably makes sense for the yeast strain to be
#		in here even though it's pretty much superficial
#

import math

import settings
import grains
import hops
import water


class Recipe(object):
#The umbrella class that will contain all of the recipe components
	
	count = 0
		#A count might come in handy for save logs or having a recipe book
	
	def __init__(self):
		Recipe.count += 1
		
		self.ogDict = {}
		self.statisticalDict = {'OG':0, 'IBU':0, 'SRM':0, 'ABV':0}
	
		#These lists will hold all of the related objects that are created (to be looped through)
		self.grainList=[grains.Grain(),grains.Grain(ppg=20)]
		self.hopList=[hops.Hop(min=15), hops.Hop(aa=7, min=5), hops.Hop(aa=14, min=60)]
		#self.grainList=[]		This will be the real one-- using multiple list items to test calculations
		#self.hopList=[]		This will be the real one-- using multiple list items to test calculations
		
		self.updateGravity()
		self.updateIBU()
		self.updateColor()
		
		
	def updateGravity(self):
		#This will update the recipe points and gravity.
		
		totalPoints = 0
		pointList = []
		
		#loop through the grain list and add up the points
		for grain in range(len(self.grainList)):
			pointList.append(self.grainList[grain].points)
			totalPoints += pointList[grain]
			
		self.ogDict.update({'pointList':pointList,'totalPoints':totalPoints})
		
		OG = self.ogDict['totalPoints']
		OG = 1 + (OG / 1000)
		self.ogDict.update({'OG': OG})

		self.statisticalDict.update({'OG':self.ogDict['OG']})
		
		
	def updateIBU(self):
		#This will update the recipe IBU.
		
		ibuList = []
		
		totalIBU = 0
		
		#loop through the hop list and calculate IBU (Tinseth)
		for hop in range(len(self.hopList)):
			ibuList.append((1.65 * 0.000125 **(self.statisticalDict['OG'] - 1)) * 
				((1 - math.exp(-0.04 * self.hopList[hop].minutes)) / 4.15) * 
				(((self.hopList[hop].aa / 100) * self.hopList[hop].weight * 7490) / settings.FinalVolume))
			totalIBU += ibuList[hop]
		
		self.statisticalDict.update({'IBU':totalIBU})
	
	
	def updateColor(self):
		#This will update the recipe color.
		
		totalColor = 0
		colorList = []
		
		#loop through the grain list and add calculate total color (Morey)
		for grain in range(len(self.grainList)):
			colorList.append(self.grainList[grain].color)
			totalColor += colorList[grain]
			
		totalMCUs = totalColor / settings.FinalVolume
		srm = 1.4922 * totalMCUs**0.6859
		
		self.statisticalDict.update({'SRM':srm})
			
		
		
	
#test main

print('printing grains.Grain.count:',grains.Grain.count)
print('printing hops.Hop.count:',hops.Hop.count)

recipe = Recipe()

print('printing recipe.grainList:',recipe.grainList)
print('testing ogDict:',recipe.ogDict)
print('testing OG calcs:',recipe.statisticalDict['OG'])

print('printing recipe.hopList:',recipe.hopList)

print('testing stats:',recipe.statisticalDict)

input('/nExit')



#This could be useful for later, but I don't need it for now
#def addGrain(self, type= 'generic', lb = 1, oz = 0, ppg = 25, degreesL = 1, sugarType="grain", use="mashed"):
		#Add a grain object to the grainList--this might make more sense outside of the class
#		self.grainList.append(grains.Grain(type, lb, oz, ppg, degreesL, sugarType, use))
#		return self.grainList
