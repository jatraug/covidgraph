RM=/bin/rm
DB=/Users/jimt/Dropbox/work/covid/
COV=/Users/jimt/work/covid/nyt
IMG=$(COV)/images
CP=/bin/cp
PY=/Users/jimt/anaconda/envs/py38/bin/python


doall: clean
#	#$(PY) cases.py -n -s Washington
#	#$(PY) cases.py -n -s Oregon
	$(PY) counties.py -n -s Washington -c Snohomish
	$(PY) counties.py -n -s Oregon -c Douglas
	$(PY) counties.py -n -s Washington -c Spokane
	$(PY) counties.py -n -s Texas -c Harris
	$(PY) counties.py -n -s California -c "Los Angeles"
	$(PY) states.py -n -s California
	$(PY) states.py -n -s Washington
	$(PY) states.py -n -s Oregon

#	#$(PY) us.py -n

	$(CP) $(COV)/images/Washington*.jpg $(DB)
	$(CP) $(COV)/images/California*.jpg $(DB)
	$(CP) $(COV)/images/Oregon*jpg $(DB)
	$(CP) $(COV)/images/Texas*jpg $(DB)
#	#$(CP) $(COV)/images/US*jpg $(DB)

clean:
	-$(RM) -f $(IMG)/*jpg
	-$(RM) -f $(DB)/*jpg		

.PHONY: clean doall 
