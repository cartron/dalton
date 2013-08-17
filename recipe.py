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
	grainList=[]
	#This will hold all of the grain objects that are created
	
	def __init__(self):
		Recipe.count += 1
		
	def addGrain(self, type= 'generic', lb = 1, oz = 0, ppg = 25, degreesL = 1, sugarType="grain", use="mashed"):
		
		#Add a grain object to the grainList--this might make more sense outside of the class
		Recipe.grainList.append(grains.Grain(type, lb, oz, ppg, degreesL, sugarType))
		return Recipe.grainList
		
		
	
	#def calculateTotalOG(self, volume, efficiency):
	#	vol = volume
	#	efficient = efficiency
	#	for grain in grainlist
	#		ogN= self.calculatePoints(vol, efficient)
	
#test main
#grain = grains.Grain(ppg=30)
#grainlb = grains.Grain(oz=8)

print('pringing grains.Grain.count:',grains.Grain.count)

recipe = Recipe()
print('printing recipe.grainList:',recipe.grainList)
added=Recipe().addGrain(ppg=9001)
print('printing added:',added)
print('printing added[0].ppg:',added[0].ppg)

input('/nExit')
