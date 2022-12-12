DEFAULT_PORT = 8000

clean:
	rm -rf venv

deploy:
	./bin/deploy

run:
	./bin/run $(DEFAULT_PORT)

generate:
	./bin/generate

all: clean deploy

.DEFAULT_GOAL := all
