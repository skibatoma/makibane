import sys
import logging


cell = getid1('/Cell:/').cellType
sys.path.append('../common')
sys.path.append('../DISTRIBUTED')
sys.path.append('../%s', % cellType)
sys.path.append('../%s', % sys.argv[0])
try:
#	import topology
print "Helo Mat"
except:
	print ('"No module was found')
#	senslog = logging.getLogger('sneistive')
#	senslog.exceptio('problem with topology')	
#	sys.exit(1)
print sys.argv[0]


#if hasChanges():
#	save()
#	sync()
#declare vars
#wdr.tools.importConfigurationManifest('topology.wdr')
#wdr.tools.importApplicationManifest('defApp.wdra',v)
#wdr.tools.importApplicationManifest('defApp.wdra',topology.variables)
#	@import jdbc.wdrc
