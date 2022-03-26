

RM = /bin/rm

summary.html : sumhead.html sumpart.html end.html
	cat sumhead.html sumpart.html end.html > summary.html

sumpart.html :  mkstatus.py
	python mkstatus.py  > sumpart.html

clean:
	$(RM) summary.html sumpart.html



