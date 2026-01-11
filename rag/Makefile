.PHONY: help install run freeze clean

PYTHON := python

help:
	@echo "Available commands:"
	@echo "  make install   Install dependencies"
	@echo "  make run       Run demo"
	@echo "  make freeze    Export full requirements.txt"
	@echo "  make clean     Remove cache files"

install:
	pip install -r requirements.txt

run:
	$(PYTHON) new_demo.py

freeze:
	pip freeze > requirements.lock.txt

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
