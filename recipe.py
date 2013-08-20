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


import grains
import hops
import water


class Recipe(object):
#The umbrella class that will contain all of the recipe components
	
	count = 0
		#A count might come in handy for save logs or having a recipe book
	ogDict = {}

	statisticalDic = {'OG':0, 'IBUs':0, 'SRM':0, 'ABV':0}
	
	#grainList=[]		This will be the real one-- using multiple list items to test calculations
	grainList=[grains.Grain(),grains.Grain(ppg=20)]
		#This will hold all of the grain objects that are created
	
	def __init__(self):
		Recipe.count += 1
		
	def addGrain(self, type= 'generic', lb = 1, oz = 0, ppg = 25, degreesL = 1, sugarType="grain", use="mashed"):
		#Add a grain object to the grainList--this might make more sense outside of the class
		Recipe.grainList.append(grains.Grain(type, lb, oz, ppg, degreesL, sugarType))
		return Recipe.grainList
		
	def calculateTotalPoints(self, volume, efficiency):
		#This will calculate the points of the entire recipe
		#-this should eventually take no inputs, but rather pull directly
		#	from a CONFIG module
		
		totalPoints = 0
		pointList = []
		
		for grain in range(len(Recipe.grainList)):
			pointList.append(Recipe.grainList[grain].calculatePoints(volume, efficiency))
			totalPoints += pointList[grain]
			
		Recipe.ogDict.update({'pointList':pointList,'totalPoints':totalPoints})
			#It might be useful to store it in a dictionary in case
			#	we ever need to access the grain list (which may be
			#	unlikely)
		return Recipe.ogDict
		
	def returnTotalOG(self, volume, efficiency):
		#Calculates the OG of the recipe
		#-this should eventually take no inputs, but rather pull directly
		#	from a CONFIG module
		
		OG = Recipe.ogDict['totalPoints']
		OG = 1 + (OG / 1000)

		Recipe.ogDict.update({'OG': OG})
		return Recipe.ogDict		

	def returnTotalColor(self, volume):
		#Estimates the recipe's SRM
		#-this should eventually take no inputs, but rather pull directly
		#	from a CONFIG module
		
		totalColor = 0
		colorList = []
		
		for grain in range(len(Recipe.grainList)):
			colorList.append(Recipe.grainList[grain].calculateColor())
			totalColor += colorList[grain]
		totalMCUs = totalColor / volume
		moreyColor = 1.4922 * totalMCUs**0.6859
		return moreyColor
	
#test main

print('pringing grains.Grain.count:',grains.Grain.count)

recipe = Recipe()

print('printing recipe.grainList:',recipe.grainList)
added=Recipe().addGrain(ppg=35)
print('printing added:',added)

print('printing added[0].ppg:',added[0].ppg)
print('testing calculateTotalPoints:',recipe.calculateTotalPoints(2,.75)['totalPoints'])
print('testing returnTotalOG:',recipe.returnTotalOG(2,.75)['OG'])

print('testing returnTotalColor:', recipe.returnTotalColor(2))

input('/nExit')
