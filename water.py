#	This will eventually perform most or all of the basic water calculations. It will hit a config file for user
#	equipment and other settings
#
#
#	It probably doesn't make sense to create a water class-- all of the calculations will be performed once
#	per brew.
#
#	There should be as many water-related functions as possible to facilitate display
#

import settings
import grains
#import recipe


#Import settings. They will be used instead of the defaults (user override)

finalVolume = settings.FinalVolume
efficiency = settings.Efficiency
grainAbsorb = settings.GrainAbsorbtion
mashThickness = settings.MashThickness
tunLoss = settings.LossToTun
boilEvap = settings.BoilEvaporation
trubLoss = settings.LossToTrub
wortShrinkage = settings.WortShrinkage

#grainWeight = SOME STUFF
#boilTime = SOME THINGS

def updateWater(self):
	kettleLoss = (finalVolume + trubLoss) / wortShrinkage / (boilEvap * (boilTime/60))