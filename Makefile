VENV_NAME=venv
COM=pynishell

env:
	python3 -m venv ${VENV_NAME}
	source ${VENV_NAME}/bin/activate

clean:
	rm -rf ${VENV_NAME}

git: clean
	git add .
	git commit -m ${COM}
	git push origin ${shell git branch --show-current}