RM=/bin/rm
DB=/Users/jimt/Dropbox/work/covid/
COV=/Users/jimt/work/covid/nyt
IMG=$(COV)/images
CP=/bin/cp
PY=/Users/jimt/anaconda/envs/py38/bin/python


doall: clean

	$(MAKE) exprt

	$(CP) $(COV)/images/Washington*.jpg $(DB)
	$(CP) $(COV)/images/California*.jpg $(DB)
	$(CP) $(COV)/images/Oregon*jpg $(DB)
	$(CP) $(COV)/images/Texas*jpg $(DB)
#	#$(CP) $(COV)/images/US*jpg $(DB)
	$(MAKE) html

clean:
	-$(RM) -f $(IMG)/*jpg
	-$(RM) -f $(DB)/*jpg		

html:
	cd html && $(MAKE)

exprt:
	export LOCALCSV=True && ./dolatest.sh

.PHONY: clean doall html
