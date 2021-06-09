default: help

covid:
	cd work/covid/nyt && $(MAKE)

vaccine:
	cd work/covid/vacc && python vaccine.py

help:
	@echo Some things to try:
	@echo make covid
	@echo make vaccine
	@echo _____________

.PHONY : covid help default
