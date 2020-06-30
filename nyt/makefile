RM=/bin/rm
DB=/Users/jimt/Dropbox/work/covid/
COV=/Users/jimt/work/covid/nyt
IMG=$(COV)/images
CP=/bin/cp
PY=/Users/jimt/anaconda/envs/py38/bin/python


doall: clean
	$(PY) cases.py -n -s Washington
	$(PY) cases.py -n -s Oregon
	$(PY) counties.py -n -s Washington -c Snohomish
	$(PY) counties.py -n -s Oregon -c Douglas
	$(PY) counties.py -n -s Washington -c Spokane
	$(PY) counties.py -n -s Texas -c Harris

	$(CP) $(COV)/images/Washington*.png $(DB)
	$(CP) $(COV)/images/Oregon*png $(DB)

clean:
	-$(RM) -f $(IMG)/*png
	-$(RM) -f $(DB)/*png		

.PHONY: clean doall 
