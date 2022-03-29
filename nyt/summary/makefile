

RM = /bin/rm -f

../html/summary.html : FORCE #sumhead.html sumpart.html end.html
	cat sumhead.html sumpart.html end.html > ../html/summary.html

sumpart.html :  mkstatus.py
	python mkstatus.py  > sumpart.html

clean:
	$(RM) summary.html sumpart.html



FORCE:

.PHONY: FORCE
