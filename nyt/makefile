RM=/bin/rm
DB=/Users/jimt/Dropbox/work/covid/
COV=/Users/jimt/work/covid/nyt
IMG=$(COV)/images
CP=/bin/cp
PY=/Users/jimt/anaconda/envs/py38/bin/python


doall:
	-$(RM) -f $(DB)/*png
	$(RM) -f $(IMG)/*png
	$(PY) cases.py -n -s Washington
	$(PY) cases.py -n -s Oregon
	$(PY) counties.py -n -s Washington -c Snohomish
	$(PY) counties.py -n -s Oregon -c Douglas
	$(CP) $(COV)/images/Washington*.png $(DB)
	$(CP) $(COV)/images/Oregon*png $(DB)


.PHONY: doall
