PY = python
CP = /bin/cp

all: index.html indexDB.html

index.html: head.html body.html
	cat head.html body.html > $@

body.html: ./mkbody.py 	DOIT

	$(PY) $< > $@

## And now Dropbox:
indexDB.html: head.html bodyDB.html
	cat head.html bodyDB.html > $@
	$(CP) indexDB.html ~/Dropbox/Work/covid/html/index.html

bodyDB.html: ./mkbodyDB.py 	DOIT
	./mkDB.sh
	$(PY) $< > $@


mkbody.py: DOIT
mkbodyDB.py: DOIT


DOIT:


.PHONY:
	DOIT	

try : fubar
	echo $@
	echo $<

fubar:

clean:
	$(RM) index.html indexDB.html bodyDB.html body.html summary.html

