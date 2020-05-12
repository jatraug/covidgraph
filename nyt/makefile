RM=/bin/rm
DB=/Users/jimt/Dropbox/work/covid/
COV=/Users/jimt/work/covid/nyt
CP=/bin/cp
PY=/Users/jimt/anaconda/envs/py38/bin/python


doall:
	-$(RM) -f $(DB)/*png
	$(PY) cases.py -n -s Washington
	$(PY) cases.py -n -s Oregon
	$(CP) $(COV)/images/Washington*.png $(DB)
	$(CP) $(COV)/images/Oregon*png $(DB)


.PHONY: doall
