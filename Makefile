VENV_NAME=venv
SRCS= srcs/main.py
COM=pynishell
ARG=

test:
	python3 -m assertions.assertion
env:
	python3 -m venv ${VENV_NAME}

run:
	venv/bin/python3 ${SRCS}

clean:
	rm -rf ${VENV_NAME}

re: clean env run

git: clean
	git add .
	git commit -m ${COM}
	git push origin ${shell git branch --show-current}