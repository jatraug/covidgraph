PY = /Users/jimt/anaconda/envs/py38/bin/python

index.html: head.html body.html
	cat head.html body.html > $@

body.html: ./mkbody.py
	$(PY) $< > $@


mkbody.py: DOIT


DOIT:


.PHONY:
	DOIT	

try : fubar
	echo $@
	echo $<

fubar:
