#	This will eventually hold all of the hop definitions and functions or methods or whatever python calls them
#
#
#	The basic hop class should be fed hop, lb, oz, AA, time (minutes), and form
#		Default to generic,0,1,10,0,pellet
#
#		update() methods should allow the user to select hop type, lb, oz, AA, time, and form
#			the user should be able to name their own hop type (and fill in the rest of the data)
#		get() methods should pull AA from a database/xml for a given hop
#		a weight conversion method should convert lb and oz to a common unit (which ever works best for calculations)
#		an IBU calculation method should pull OG and volume as well as time, AA and weight in order to calculate Tinseth IBUs (some day add Rager)
#			perhaps getOG() and getVolume() methods should facilitate this
#		a AAU conversion method should be fed time, AA and weight (?) and output the AAUs from the particular hop
#
#		the class should return return a (single unit) weight value, AA, time (minutes), form, IBU and AAU
#
#		hop attributes wiill be:
#			displayed: (multi-unit) weight, AA, time (minutes) and form
#				(multi-unit) weight, time (minutes) and form will feed the brew day tasks (this is not thought out yet)
#			fed to aggregate IBU calculations
#			AAU converter to plan for audibles
#			probably other things?


class Hop(object):
	def __init__(self, type, lb, oz, AA, min, form):
		self.type = type
		self.lb = lb
		self.oz = oz
		self.AA = AA
		self.minutes = min
		self.form = form

		
#test main
hop = Hop("generic", 0, 1, 10, 0, "pellet")
print('print', hop.type)
input("\nExit")