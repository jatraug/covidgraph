STATFILE= ../html/Covid_Status_2022-03-25.txt

RM = /bin/rm

summary.html : sumhead.html sumpart.html end.html
	cat sumhead.html sumpart.html end.html > summary.html

sumpart.html :  mkstatus.py $(STATFILE) 
	python mkstatus.py $(STATFILE) > sumpart.html

clean:
	$(RM) summary.html sumpart.html



