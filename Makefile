# Comandos para automatización
install:
	pip install -r requirements.txt

train:
	python src/train.py

clean:
	powershell -Command "Remove-Item -Recurse -Force mlruns, mlartifacts, src/__pycache__"