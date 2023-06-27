setup:
	pip3 install virtualenv
	python3 -m venv ~/demoImage
	. ~/demoImage/bin/activate
install:
	pip3 install --upgrade pip
	pip3 install -r requirements.txt
 