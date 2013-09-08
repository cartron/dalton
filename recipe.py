#	This will eventually perform a few calculations and hold the bulk of the recipe data
#
#	-Settings should be imported from a CONFIG type of module
#		-in addition to settings things like recipe name and author should probably
#			be pulled
#	-The class should then import GRAIN and HOP and create a new instance of the objects
#		at the user's command
#	-It should use these to calculate overall recipe OG, SRM, and IBUs
#	-Data should be stored somehow (dic?)
#
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
		
		volume = settings.FinalVolume
		efficiency = settings.Efficiency
	
		#self.grainList=[]		This will be the real one-- using multiple list items to test calculations
		self.grainList=[grains.Grain(),grains.Grain(ppg=20)]
			#This will hold all of the grain objects that are created
		#self.hopList=[]		This will be the real one-- using multiple list items to test calculations
		self.hopList=[hops.Hop(min=15), hops.Hop(aa=7, min=5), hops.Hop(aa=14, min=60)]
			#This will hold all of the hop objects that are created
		
		
		#Store and calculate COLOR, PPG and OG
		
		totalPoints = 0
		totalColor = 0
		
		pointList = []
		colorList = []
		
			#loop through the grain list and perform some calculations
		for grain in range(len(self.grainList)):
			pointList.append(self.grainList[grain].points)
			totalPoints += pointList[grain]
			
			colorList.append(self.grainList[grain].color)
			totalColor += colorList[grain]
			
		self.ogDict.update({'pointList':pointList,'totalPoints':totalPoints})
		
		OG = self.ogDict['totalPoints']
		OG = 1 + (OG / 1000)
		self.ogDict.update({'OG': OG})

		totalMCUs = totalColor / volume
		moreyColor = 1.4922 * totalMCUs**0.6859
		
		
		self.statisticalDict.update({'OG':self.ogDict['OG'], 'SRM': moreyColor})
		
		
		#Store and calculate total AAUs and IBUs
		
		aauList = []
		ibuList = []
		
		totalIBU = 0
		
			#Loop through the hop list, pull out AAUs (solely for storage at this point) and calculate IBU
				#Only does Tinseth IBU calculations right now
		for hop in range(len(self.hopList)):
			aauList.append(self.hopList[hop].aau)
			ibuList.append((1.65 * 0.000125 **(self.statisticalDict['OG'] - 1)) * 
				((1 - math.exp(-0.04 * self.hopList[hop].minutes)) / 4.15) * 
				(((self.hopList[hop].aa / 100) * self.hopList[hop].weight * 7490) / volume))
			totalIBU += ibuList[hop]
		
		self.statisticalDict.update({'IBU':totalIBU})
			
		
		
	
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
