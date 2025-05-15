# Makefile for automating setup and run
.PHONY: run

run:
	cp .env.example .env
	chmod +x deploy.sh
	./deploy.sh
