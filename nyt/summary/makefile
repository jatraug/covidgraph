

RM = /bin/rm -f

../html/summary.html : sumhead.html sumpart.html end.html
	cat sumhead.html sumpart.html end.html > ../html/summary.html

sumpart.html :  FORCE
	python mkstatus.py  > sumpart.html

clean: FORCE
	$(RM) summary.html sumpart.html



FORCE:

.PHONY: FORCE clean
