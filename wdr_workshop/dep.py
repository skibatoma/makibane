#declare vars
try:
	v = {
		'webServers':'',
		'deploymentsTargets':'WebSphere:cell=vagrant,node=vagrant,server=server1',
		'virtualHost':'default_host',
	}	

	wdr.tools.importApplicationManifest('defApp.wdra',v)
#	@import jdbc.wdrc
finally:
      reset()
