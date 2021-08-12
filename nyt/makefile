

ifneq (,$(wildcard ./.env))
    include .env
    export
endif




RM=/bin/rm
DB=/Users/jimt/Dropbox/work/covid/html/images
COV=$(COVWORK)

IMG=$(IMGPATH)

CP=/bin/cp
PY=python


doall: clean

	$(MAKE) dolatest

	$(CP) $(COVWORK)/images/*.jpg $(DB)
	#$(CP) $(COVWORK)/images/California*.jpg $(DB)
	#$(CP) $(COVWORK)/images/Oregon*jpg $(DB)
	#$(CP) $(COVWORK)/images/Texas*jpg $(DB)
#	#$(CP) $(COVWORK)/images/US*jpg $(DB)
	$(MAKE) html
	$(MAKE) web



web:
	cd web && $(MAKE)

clean:
	-$(RM) -f $(IMG)/*jpg
	-$(RM) -f $(DB)/*jpg		

html:
	cd html && $(MAKE)  ##  $(PY) mkbody.py

dolatest:
#	conda init bash
#	conda activate py38
	mkdir -p images
	mkdir -p datasets
	export LOCALCSV=True && ./dolatest.sh

.PHONY: clean doall html web
